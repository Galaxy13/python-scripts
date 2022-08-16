import os
from os.path import exists

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


class Test:
    def __init__(self, question='', test_answers={}):
        self._question = question
        self._test_answers = test_answers

    def __len__(self):
        return len(self._test_answers)

    def __del__(self):
        print('Вопрос удалён')

    def __str__(self):
        what_is_shown = self._question
        for answer_index in range(len(self._test_answers.items())):
            what_is_shown += '\n' + str(answer_index + 1) + '. ' + str(list(self._test_answers.keys())[answer_index])
        return what_is_shown

    def __getitem__(self, key_of_answer):
        return list(self._test_answers.keys())[key_of_answer]

    def set_wrong_answer(self, answer):
        self._test_answers[answer] = False

    def set_right_answer(self, answer):
        self._test_answers[answer] = True

    def set_answer(self, answer, value):
        if value == 'True':
            self._test_answers[answer] = True
        else:
            self._test_answers[answer] = False

    def __iter__(self):
        return self._test_answers.items()

    def get_answer_value(self, answer_num):
        return self._test_answers[self[answer_num - 1]]

    def get_question(self):
        return self._question

    def get_answers_dict(self):
        return self._test_answers

    def get_right_answer(self):
        for key, value in self._test_answers.items():
            if not value:
                return key


class Lesson:
    def __init__(self):
        self._tests = []
        self._file_opened = False

    def __len__(self):
        return len(self._tests)

    def __getitem__(self, key_of_test):
        return self._tests[key_of_test]

    def __iter__(self):
        return self._tests

    def start_lesson(self):
        clear()
        if not self._file_opened and not len(self._tests) and exists('lesson.txt'):
            self.lesson_open()
        print('Количество вопросов: ' + '[' + str(len(self._tests)) + ']')
        print('Добро пожаловать!' + '\n' + "Выберите вариант:")
        start_construct = {
            1: self.start_test,
            2: self.add_new_test_user
        }
        choice = int(input("1 - Начать тест" + '\n' + '2 - Добавить свой вопрос' + '\n'))
        start_construct[choice]()

    def lesson_save(self):
        with open('lesson.txt', 'w', encoding='utf-8') as file:
            for test in self._tests:
                file.write('q' + test.get_question() + '\n')
                for key, value in test.get_answers_dict().items():
                    file.write('a' + key + ' >>> ' + str(value) + '\n')
        file.close()

    def lesson_open(self):
        clear()
        with open('lesson.txt', 'r', encoding='utf-8') as file:
            while 1:
                line = file.readline()
                if line:
                    if line[0] == 'q':
                        self._tests.append(Test(question=line[1:], test_answers={}))
                    elif line[0] == 'a':
                        self._tests[-1].set_answer(line.split(' >>> ')[0][1:], bool(line.split(' >>> ')[1]))
                else:
                    break
        file.close()
        self._file_opened = True

    def start_test(self):
        clear()
        test_index = 0
        while test_index < len(self._tests):
            print(str(self._tests[test_index]))
            choice = input('Выберите вариант ответа: (' + '1-' + str(len(self._tests[test_index])) +
                           ' ; для выхода выберите 0)' + '\n')
            if choice:
                try:
                    if self._tests[test_index].get_answer_value(int(choice)):
                        input("Правильно! Для продолжения нажмите Enter ")
                    else:
                        input("Ответ неверен! Правильный ответ: " + self._tests[test_index].get_right_answer() +
                              ' .Для продолжения нажмите Enter')
                    test_index += 1
                except:
                    input('Такого варианта нет. Попробуй ещё, блять!')
                clear()
            elif choice == 0:
                self.start_lesson()
            else:
                input('Такого варианта нет. Попробуй ещё, блять!')
        self.start_lesson()

    def add_new_test_user(self):
        clear()
        question = input("Введите вопрос ... ")
        new_test = Test(question=question, test_answers={})
        right_wrong_dict = {
            1: new_test.set_wrong_answer,
            2: new_test.set_right_answer,
            0: False
        }
        while 1:
            clear()
            choise = input("Выберите значение:" + '\n' + '1. Добавить неправильный вариант' + '\n' +
                               '2. Добавить правильный вариант' + '\n' + '0. Назад' + '\n')
            if choise:
                try:
                    choise = int(choise)
                    right_wrong_dict[choise](input("Введите ответ и нажмите Enter: " + '\n'))
                except KeyError or ValueError:
                    input('Неправильный выбор. Нажмите Enter')
            elif choise == '':
                input('Неправильный выбор. Нажмите Enter')
            else:
                self._tests.append(new_test)
                self.lesson_save()
                self.start_lesson()


lesson = Lesson()
lesson.start_lesson()
