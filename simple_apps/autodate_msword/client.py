import datetime
from tkinter import *
from tkinterdnd2 import *
from tkinter.ttk import Combobox
from tkinter import filedialog as fd
from tkcalendar import Calendar
from playsound import playsound
from PIL import Image, ImageTk
import msword_handler

date = datetime.date.today()

window = Tk()
window.title("Календарь Фiмы")
window.geometry('1280x720')
frame = Frame(window)
frame.pack()
doc = None

save_icon = Image.open(r'img/save.png')
save_icon = save_icon.resize((50, 50), Image.ANTIALIAS)
save_icon = ImageTk.PhotoImage(save_icon)

load_icon = Image.open(r'img/download.png')
load_icon = load_icon.resize((50, 50), Image.ANTIALIAS)
load_icon = ImageTk.PhotoImage(load_icon)

delete_icon = Image.open(r'img/delete.png')
delete_icon = delete_icon.resize((50, 50), Image.ANTIALIAS)
delete_icon = ImageTk.PhotoImage(delete_icon)

WEEKDAYS = {0: 'Понедельник',
            1: 'Вторник',
            2: 'Среда',
            3: 'Четверг',
            4: 'Пятница',
            5: 'Суббота',
            6: 'Воскресенье'}


def dragged(event):
    global doc
    doc = msword_handler.Column(event.data.format('utf-8'))
    textbox.destroy()
    comboBox(doc)
    place_button_plus()
    place_textbox()
    place_restricted_date_button()
    place_date_textbox()
    place_save_button()
    place_load_button()
    place_clear_last_r_date_button()
    Label(frame,
          text='Выберите столбец',
          font=('Arial Bold', 10)).place(x=60,
                                         y=0)
    Label(frame,
          text='Дни недели',
          font=('Arial Bold', 10)).place(x=360,
                                         y=70)
    Label(frame,
          text='Даты каникул',
          font=('Arial Bold', 10)).place(x=800,
                                         y=70)
    Label(frame,
          text='Сохранить в файл',
          font=('Arial Bold', 10)).place(x=1080,
                                         y=170)
    Label(frame,
          text='Загрузить из файла',
          font=('Arial Bold', 10)).place(x=1080,
                                         y=420)
    Label(frame,
          text='Удалить последнюю дату',
          font=('Arial Bold', 10)).place(x=1080,
                                         y=290)
    print("Читается")


textbox = Text(frame,
               height=22,
               width=50,
               font=('Arial Bold', 40))
textbox.insert(END, 'Drag and Drop Here')
textbox.pack(side=LEFT)
textbox.drop_target_register(DND_FILES)
textbox.dnd_bind('<<Drop>>', dragged)

restricted_textbox = Text(frame,
                          height=12,
                          width=10,
                          font=('Arial Bold', 10))
date_textbox = Text(frame,
                    height=12,
                    width=10,
                    font=('Arial Bold', 10))

combo = Combobox(frame)
calendar_dict = {}
restricted_calendar = []


def save_r_date_to_file():
    with open('restricted_dates.txt', 'w') as file:
        file.write('### RESTRICTED DATES DOCUMENT ###' + '\n')
        file.write('### DO NOT DELETE THIS LINE ###' + '\n')
        output = restricted_textbox.get('1.0', END).split('\n')
        for cal_date in output:
            file.write(cal_date + '\n')
        file.close()
    playsound(u'mp3/ohshit.mp3', block=False)


def open_r_from_file():
    playsound(u'mp3/fuckyou.mp3', block=False)
    global restricted_calendar, restricted_textbox
    restricted_calendar = []
    restricted_textbox.delete('1.0', END)
    with fd.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')]) as file:
        input = file.readlines()
        if input[0] != '### RESTRICTED DATES DOCUMENT ###\n' or input[1] != '### DO NOT DELETE THIS LINE ###\n':
            playsound(u'mp3/durak.mp3')
        else:
            for line in input[2:-1]:
                restricted_textbox.insert('end', line)
                line = line.split(' : ')
                restricted_calendar.append((Calendar(
                    selectmode='day',
                    year=int(line[0].split(' - ')[2].replace('\n', '')),
                    month=int(line[0].split(' - ')[1]),
                    day=int(line[0].split(' - ')[0])),
                                            Calendar(
                                                selectmode='day',
                                                year=int(line[1].split(' - ')[2].replace('\n', '')),
                                                month=int(line[1].split(' - ')[1]),
                                                day=int(line[1].split(' - ')[0]))))

def clear_last_line():
    if not restricted_calendar:
        playsound(u'mp3/durak.mp3', block=False)
    else:
        restricted_textbox.delete('end-2l', 'end-1l')
        restricted_textbox.update()
        restricted_calendar.pop(-1)


def comboBox(doc):
    combo['values'] = doc.get_list_of_columns()
    combo.current(0)
    combo.place(x=50,
                y=30)
    place_gachi_button()


def place_gachi_button():
    btn = Button(frame,
                 text="Давай, нажимай, блять",
                 bg='red', fg='white',
                 command=start)
    btn.place(x=50,
              y=100)


def place_button_plus():
    btn = Button(frame,
                 text='Добавить дни недели',
                 font=("Arial Bold", 10),
                 bg='white',
                 command=place_calendar)
    btn.place(x=300,
              y=520)


def place_textbox():
    restricted_textbox.place(x=750,
                             y=100,
                             height=400,
                             width=200)


def place_date_textbox():
    date_textbox.place(x=300,
                       y=100,
                       height=400,
                       width=200)


def place_restricted_date_button():
    btn = Button(frame,
                 text='Добавить даты каникул',
                 font=("Arial Bold", 10),
                 bg='white',
                 command=newRdateWindow)
    btn.place(x=750,
              y=520)


def place_calendar():
    newWindow()


def place_save_button():
    Button(frame,
           text='Сохранить в файл',
           font=('Arial Bold', 10),
           image=save_icon,
           bg='white',
           command=save_r_date_to_file).place(x=1000,
                                              y=150)


def place_load_button():
    Button(frame,
           text='Загрузить из файла',
           font=('Arial Bold', 10),
           image=load_icon,
           bg='white',
           command=lambda: open_r_from_file()
           ).place(x=1000,
                   y=400)

def place_clear_last_r_date_button():
    Button(frame,
           text='Удалить последнюю дату',
           image=delete_icon,
           font=('Arial Bold', 10),
           bg='white',
           command=clear_last_line).place(x=1000,
                                          y=280)


def get_dates_from_calendar(cal_dict):
    return [cal.get_date() for cal in cal_dict.items]


def place_date_to_cal_dict(calendar, top_window):
    calendar_dict['cal' + str(len(calendar_dict))] = calendar
    date = calendar.get_date().split('/')
    date_textbox.insert('end', '%02d' % int(date[1]) + ' - ' + '%02d' % int(date[0]) + ' - ' + WEEKDAYS[
        datetime.datetime.strptime(
            str(calendar.get_date()), '%m/%d/%y').weekday()] + '\n')
    top_window.destroy()
    top_window.update()
    playsound(u'mp3/spank.mp3', block=False)


def place_date_to_rest_cal_dict(calendar_pair, top_window):
    restricted_calendar.append(calendar_pair)
    date_pair = [calendar.get_date().split('/') for calendar in calendar_pair]
    restricted_textbox.insert('end',
                              ' - '.join(('%02d' % int(date_pair[0][1]), '%02d' % int(date_pair[0][0]),
                                          '20' + date_pair[0][2]))
                              + ' : ' + ' - '.join(('%02d' % int(date_pair[1][1]), '%02d' % int(date_pair[1][0]),
                                                    '20' + date_pair[1][2])))
    top_window.destroy()
    top_window.update()


def newWindow():
    new_w = Toplevel(frame)
    new_w.title('Календарь')
    new_w.geometry('300x300')
    Label(new_w,
          text='Выберите дату').pack()
    calendar = Calendar(new_w,
                        selectmode='day',
                        year=date.year,
                        month=date.month,
                        day=date.day)
    calendar.pack()
    Button(new_w,
           text='OK',
           font=('Arial Bold', 10),
           bg='green',
           command=lambda: place_date_to_cal_dict(calendar, new_w)).pack()
    playsound(u'mp3/woo.mp3', block=False)


def newRdateWindow():
    new_res_d_w = Toplevel(frame)
    two_calendars = [Calendar(new_res_d_w,
                              selectmode='day',
                              year=date.year,
                              month=date.month,
                              day=date.day),
                     Calendar(new_res_d_w,
                              selectmode='day',
                              year=date.year,
                              month=date.month,
                              day=date.day)]
    new_res_d_w.title('Каникулы')
    new_res_d_w.geometry('400x500')
    Label(new_res_d_w, text='Добавьте даты каникул', font=('Arial Bold', 10)).pack()
    for calendar in two_calendars:
        calendar.pack()
    Button(new_res_d_w, text='OK', font=('Arial Bold', 10),
           command=lambda: place_date_to_rest_cal_dict(two_calendars, new_res_d_w)).pack()


def start():
    restricted_list = []
    if not calendar_dict:
        playsound(u'mp3/durak.mp3', block=False)
    else:
        for date in calendar_dict.values():
            doc.add_new_datetime(datetime.datetime.strptime(str(date.get_date()), '%m/%d/%y'))
        for calendar in restricted_calendar:
            restricted_list.append((datetime.datetime.strptime(str(calendar[0].get_date()), '%m/%d/%y'),
                                    datetime.datetime.strptime(str(calendar[1].get_date()), '%m/%d/%y')))
        doc.set_restricted_dates(restricted_list)
        playsound(u'mp3/spank.mp3', block=False)
        doc.column_fill(combo.get())


window.mainloop()
