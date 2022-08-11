import datetime

from docx.api import Document

WEEKDAYSMAPPING = ["Понедельник", "Вторник",
                   "Среда", "Четверг", "Пятница",
                   "Суббота", "Воскресенье"]


class Column:
    def __init__(self, document_path):
        self._document = Document(document_path)
        self._datetime_list = []

    def get_column(self, col_name):
        for table in self._document.tables:
            for col in table.columns:
                if col_name == col.cells[0].text or col.cells[1].text:
                    return col

    def add_new_datetime(self, new_datetime):
        self._datetime_list.append(new_datetime)

    def sort_datetime_list(self, sort_array):
        if len(sort_array) > 1:
            left_arr = sort_array[:len(sort_array) // 2]
            right_arr = sort_array[len(sort_array) // 2:]

            self.sort_datetime_list(left_arr)
            self.sort_datetime_list(right_arr)

            left_index, right_index, merged_index = 0, 0, 0

            while left_index < len(left_arr) and right_index < len(right_arr):
                if left_arr[left_index] < right_arr[right_index]:
                    sort_array[merged_index] = left_arr[left_index]
                    left_index += 1
                else:
                    sort_array[merged_index] = right_arr[right_index]
                    right_index += 1
                merged_index += 1

            while left_index < len(left_arr):
                sort_array[merged_index] = left_arr[left_index]
                left_index, merged_index = left_index + 1, merged_index + 1
            while right_index < len(right_arr):
                sort_array[merged_index] = right_arr[right_index]
                right_index, merged_index = right_index + 1, merged_index + 1

            if merged_index == len(self._datetime_list):
                self._datetime_list = sort_array

    def get_list_of_columns(self):
        col_names_list = []
        for table in self._document.tables:
            for column in table.columns:
                if len(column.cells[0].text) < 10:
                    col_names_list.append(column.cells[0].text)
                if len(column.cells[1].text) < 10:
                    col_names_list.append(column.cells[1].text)
        return list(set(col_names_list))

    def get_list_of_datetime(self):
        return self._datetime_list

    def column_fill(self, col_name):
        column = self.get_column(col_name)
        index_of_date_list = 0
        for cell in column.cells:
            if cell.text:
                cell.text = ('.'.join(('%02d' % self._datetime_list[index_of_date_list].day,
                                       '%02d' % self._datetime_list[index_of_date_list].month)))
                self._datetime_list[index_of_date_list] += datetime.timedelta(days=7)
                index_of_date_list += 1
                index_of_date_list %= len(self._datetime_list)

    def save_document(self):
        self._document.save('doc' + str(datetime.date.today()) + ".docx")





# dayOfTheWeek = WEEKDAYSMAPPING[datetime.date(2022, 5, 3).weekday()]
# date = datetime.date(2022, 5, 3)
# print(dayOfTheWeek)

# for row_idx in range(len(doc_table.rows)):
#     for cell in doc_table.row_cells(row_idx):
#         if cell.text == '':
#             date += datetime.timedelta(days=7)
#             cell.text = (' - '.join(('%02d' % date.day, '%02d' % date.month, weekDaysMapping[date.weekday()])))
#             break
#     row_idx += 1

# document.save('test2.docx')
