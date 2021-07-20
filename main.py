#подключаем библиотеки
from tkinter import * #библиотека tk

#функция вставки чисел с кнопки
def add_num(num):
    if message_entry.get() == "0":
        message_entry.delete(0, END)
        # print(message_entry.get())
        message_entry.insert(0, num)
        # print(message_entry.get())
    else:
        insert = message_entry.get() + str(num)
        # print(insert)
        message_entry.delete(0, END)
        # print(message_entry.get())
        message_entry.insert(0,insert)
        # print(message_entry.get())

#функция очистки окна
def clear():
    message_entry.delete(0, END)
    message_entry.insert(1, "0")

#функция математических операций
def math(operation):
    value = message_entry.get()
    if value[-1] in "+/*-":
        value = value[:-1]
    elif "+" in value or "/" in value or "*" in value or "-" in value:
        calculate()
        value= message_entry.get()
    message_entry.delete(0, END)
    message_entry.insert(0, value + operation)

    # value1 = message_entry.get()
    # message_entry.delete(0, END)
    # message_entry.insert(1, value1+"+")
    # value1 = value1+message_entry.get()
    # message_entry.delete(0, END)
    # message_entry.insert(1, value1 + "+")

#функция расчета
def calculate():
    try:
        string = message_entry.get()
        if string[-1] in "+/*-": #если последний знак один из перечисленных
            string = string+string[:-1] #то заменяем его на введеный другой знак
        calc = eval(string) #калькулятор
        message_entry.delete(0, END)
        message_entry.insert(0,calc)
    except ValueError: #обработка ошибок
        message_entry.delete(0, END)
        message_entry.insert(0,"Преобразование неудачно")
    except ZeroDivisionError:
        message_entry.delete(0, END)
        message_entry.insert(0,"Делить на 0 нельзя!")
    except Exception:
        message_entry.delete(0, END)
        message_entry.insert(0,"Общее исключение")


#функция описывающая действия при нажатии кнопки
def press_key(event):
    #print(repr(event.char))
    if event.char.isdigit():
        calculate()
    elif event.char in "+/*-":
        math(event.char)
    elif event.char == "\r":
        calculate()

#удаляет последний введенный элемент
def delete_last():
    message_entry.delete(len(message_entry.get())-1)

#вставляет запятую (число с плавающей запятой)
def double():
    message_entry.insert(len(message_entry.get()), ".")


#графическое окно
root = Tk() #создание графического окна
root.title("Calculate") #заголовок графического окна
root.geometry("280x250") #размер окна при открытии
root.resizable(False, False)

#минимальный размер колонки
root.grid_columnconfigure(0,minsize=70)
root.grid_columnconfigure(1,minsize=70)
root.grid_columnconfigure(2,minsize=70)
root.grid_columnconfigure(3,minsize=70)

#что отображает экран при нажатии клавиш
root.bind("<Key>", press_key)

#размер строки
root.grid_rowconfigure(0,minsize=40)
root.grid_rowconfigure(1,minsize=40)
root.grid_rowconfigure(2,minsize=40)
root.grid_rowconfigure(3,minsize=40)
root.grid_rowconfigure(4,minsize=40)
root.grid_rowconfigure(5,minsize=40)

#размещение кнопок на рабочей панели

#поле ввода
message_entry = Entry(justify=RIGHT, width=15, font=15) #создаем поле ввода
message_entry.insert(1, "0") #устанавливаем значение по умолчанию
message_entry.place(relx=.5, rely=.1, anchor="c", height=30, width=230) #позиционируем элемент
message_entry.grid(row=0, column=0, columnspan=4, sticky=W+E, padx=10, pady=10) #расставляем в нужной позиции элемент


#кнопки
btn_clear = Button(text="C", width="5", height="1", command=clear).grid(row=1, column=3)
#btn_clear.pack(fill = NONE, side = BOTTOM)
btn_one = Button(text="1", width="5", height="1", command=lambda : add_num(1)).grid(row=1, column=0)
#btn_one.pack()
btn_two = Button(text="2", width="5", height="1", command=lambda : add_num(2)).grid(row=1, column=1)
# btn_two.pack()
btn_three = Button(text="3", width="5", height="1", command=lambda : add_num(3)).grid(row=1, column=2)
# btn_three.pack()
btn_four = Button(text="4", width="5", height="1", command=lambda : add_num(4)).grid(row=2, column=0)
# btn_four.pack()
btn_five = Button(text="5", width="5", height="1", command=lambda : add_num(5)).grid(row=2, column=1)
# btn_five.pack()
btn_six = Button(text="6", width="5", height="1", command=lambda : add_num(6)).grid(row=2, column=2)
# btn_six.pack()
btn_seven = Button(text="7", width="5", height="1", command=lambda : add_num(7)).grid(row=3, column=0)
# btn_six.pack()
btn_eight = Button(text="8", width="5", height="1", command=lambda : add_num(8)).grid(row=3, column=1)
# btn_six.pack()
btn_nine = Button(text="9", width="5", height="1", command=lambda : add_num(9)).grid(row=3, column=2)
# btn_six.pack()
btn_zero = Button(text="0", width="5", height="1", command=lambda : add_num(0)).grid(row=4, column=0)
# btn_six.pack()
btn_sum = Button(text="+", width="5", height="1", command=lambda : math("+")).grid(row=3, column=3)
# btn_six.pack()
btn_min = Button(text="-", width="5", height="1", command=lambda : math("-")).grid(row=4, column=3)
# btn_six.pack()
btn_mult = Button(text="*", width="5", height="1", command=lambda : math("*")).grid(row=4, column=2)
# btn_six.pack()
btn_div = Button(text="/", width="5", height="1", command=lambda : math("/")).grid(row=4, column=1)
# btn_six.pack()
btn_out = Button(text="=", width="25", height="1", command=calculate).grid(row=5, column=1, columnspan="3")
# btn_six.pack()
btn_double = Button(text=".", width="5", height="1", command=double).grid(row=5, column=0)
btn_onedel = Button(text="<-", width="5", height="1", command=delete_last).grid(row=2, column=3)

root.mainloop()