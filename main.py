import tkinter.ttk as ttk
from tkinter.ttk import Combobox, Checkbutton,Radiobutton,Notebook, Frame,Button,Label,Entry
from tkinter import *
import datetime

window = Tk()
window.title("Конвертер валют")
window.geometry("500x500")

tab_control = Notebook(window)
tab1 = Frame(tab_control)

#tab_control.add(tab1, text="Калькулятор валют")

combo1 = ttk.Combobox(tab1)
combo1["values"]=[]
combo1.grid(column=0,row=0)

combo2 = ttk.Combobox(tab1)
combo2["values"]=[]
combo2.grid(column=0,row=1)

button1 = Button(tab1, text="Конвертировать")
button1.grid(column=2,row=0)

label1 = Label(tab1, text="")
label1.grid(column=1,row=1)

entry1 = Entry(tab1, text="")
entry1.grid(column=1,row=1)






tab2 = Frame(tab_control)
tab_control.add(tab2, text="Динамика курса")

radio_state = IntVar()
radio_state.set(4)

def clicked():
  timecut=radio_state.get()
  if (timecut==1):
    combotime = ttk.Combobox(tab2)
    combotime['value']=[((datetime.datetime.now().day),('/'),(datetime.datetime.now().month),('/'),(datetime.datetime.now().year)),((datetime.datetime.now().day-1),('/'),(datetime.datetime.now().month),('/'),(datetime.datetime.now().year)),((datetime.datetime.now().day-2),('/'),(datetime.datetime.now().month),('/'),(datetime.datetime.now().year)),((datetime.datetime.now().day-3),('/'),(datetime.datetime.now().month),('/'),(datetime.datetime.now().year))]
    combotime.grid(column=2,row=1)

  elif (timecut==2):
    combotime = ttk.Combobox(tab2)
    combotime['value']=[(datetime.datetime.now().day)+('/')+(datetime.datetime.now().month)+('/')+(datetime.datetime.now().year),(datetime.datetime.now().day)+('/')+(datetime.datetime.now().month-1)+('/')+(datetime.datetime.now().year),(datetime.datetime.now().day)+('/')+(datetime.datetime.now().month-2)+('/')+(datetime.datetime.now().year),(datetime.datetime.now().day)+('/')+(datetime.datetime.now().month-3)+('/')+(datetime.datetime.now().year)]
    combotime.grid(column=2,row=2)

  elif (timecut==3):
    combotime = ttk.Combobox(tab2)
    combotime['value']=[(datetime.datetime.now().day)+('/')+(datetime.datetime.now().month)+('/')+(datetime.datetime.now().year),(datetime.datetime.now().day)+('/')+(datetime.datetime.now().month)+('/')+(datetime.datetime.now().year),(datetime.datetime.now().day)+('/')+(datetime.datetime.now().month)+('/')+(datetime.datetime.now().year),(datetime.datetime.now().day)+('/')+(datetime.datetime.now().month)+('/')+(datetime.datetime.now().year)]
    combotime.grid(column=2,row=3)

  elif (timecut==4):
    combotime = ttk.Combobox(tab2)
    combotime['value']=[(datetime.datetime.now().day)+('/')+(datetime.datetime.now().month)+('/')+(datetime.datetime.now().year),(datetime.datetime.now().day)+('/')+(datetime.datetime.now().month)+('/')+(datetime.datetime.now().year-1),(datetime.datetime.now().day)+('/')+(datetime.datetime.now().month)+('/')+(datetime.datetime.now().year-2),(datetime.datetime.now().day)+('/')+(datetime.datetime.now().month)+('/')+(datetime.datetime.now().year-3)]
    combotime.grid(column=2,row=4)

radiobutton1 = Radiobutton(tab2, text = "Неделя",
value = 1, variable = radio_state,command=clicked)
radiobutton1.grid(row = 1, column = 1)
radiobutton2 = Radiobutton(tab2, text = "Месяц",
value = 2, variable = radio_state,command=clicked)
radiobutton2.grid(row = 2, column = 1)
radiobutton3 = Radiobutton(tab2, text = "Квартал",
value = 3, variable = radio_state,command=clicked)
radiobutton3.grid(row = 3, column = 1)
radiobutton4 = Radiobutton(tab2, text = "Год",
value = 4, variable = radio_state,command=clicked)
radiobutton4.grid(row = 4, column = 1)

combo3 = ttk.Combobox(tab2)
combo3["values"]=[]
combo3.grid(column=0,row=1)

label2 = Label(tab2, text="Валюта")
label2.grid(column=0,row=0)

label3 = Label(tab2, text="Период")
label3.grid(column=1,row=0)

label4 = Label(tab2, text="Выбор периода")
label4.grid(column=2,row=0)

button2 = Button(tab2, text="Построить график")
button2.grid(column=0,row=4)

#tab_control(expand=1, fill='both')
window.mainloop()
