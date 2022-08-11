import datetime
from tkinter import *
from tkinterdnd2 import *
from tkinter.ttk import Combobox
from tkcalendar import Calendar
from playsound import playsound
import msword_handler

window = Tk()
window.title("Календарь Фiмы")
window.geometry('900x400')
frame = Frame(window)
frame.pack()
doc = None


def dragged(event):
    global doc
    doc = msword_handler.Column(event.data.format('utf-8'))
    textbox.destroy()
    comboBox(doc)
    place_button_plus()
    print("Читается")


textbox = Text(frame, height=22, width=50, font=('Arial Bold', 40))
textbox.insert(END, 'Drag and Drop Here')
textbox.pack(side=LEFT)
textbox.drop_target_register(DND_FILES)
textbox.dnd_bind('<<Drop>>', dragged)
combo = Combobox(frame)
calendar_dict = {}


def comboBox(doc):
    combo['values'] = doc.get_list_of_columns()
    combo.current(0)
    combo.grid(column=0, row=0)
    place_gachi_button()


def place_gachi_button():
    btn = Button(frame, text="Давай, нажимай, блять", bg='red', fg='white', command=start)
    btn.grid(column=0, row=3)


def place_button_plus():
    btn = Button(frame, text='+', font=("Arial Bold", 20), bg='blue', command=place_calendar)
    btn.grid(column=1, row=2)


def place_calendar():
    date = datetime.datetime.today()
    calendar_dict['cal' + str(len(calendar_dict))] = Calendar(frame, selectmode='day',
                                                              year=date.year, month=date.month,
                                                              day=date.day)
    calendar_dict['cal' + str(len(calendar_dict) - 1)].grid(row=len(calendar_dict) + 2, column=4)
    playsound(u'mp3/woo.mp3', block=False)


def get_dates_from_calendar(cal_dict):
    return [cal.get_date() for cal in cal_dict.items]


def start():
    for date in calendar_dict.values():
        doc.add_new_datetime(datetime.datetime.strptime(str(date.get_date()), '%m/%d/%y'))
    playsound(u'mp3/spank.mp3', block=False)
    doc.column_fill(combo.get())


window.mainloop()
