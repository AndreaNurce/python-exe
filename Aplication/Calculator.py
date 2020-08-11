from tkinter import *


root = Tk()
root.iconbitmap(r'C:\Users\Personal\PycharmProjects\Aplication\icon.ico')


def add(number):

    curr = e.get()
    e.delete(0, END)
    e.insert(0, str(curr) + str(number))


def equal():
    point = "."
    second_num = str(e.get())
    str(second_num)
    str(fr_num)
    if type == "plus":
        if point in fr_num or point in second_num :
            math = float(fr_num) + float(second_num)
            e.delete(0, END)
            e.insert(0, math)
        else :
            math = int(fr_num) + int(second_num)
            e.delete(0, END)
            e.insert(0, math)
    if type == "minus":
        if point in fr_num or point in second_num:
            math = float(fr_num) - float(second_num)
            e.delete(0, END)
            e.insert(0, math)
        else:
            math = int(fr_num) - int(second_num)
            e.delete(0, END)
            e.insert(0, math)
    if type == "divide":
        if point in fr_num or point in second_num:
            math = float(fr_num) / float(second_num)
            e.delete(0, END)
            e.insert(0, math)
        else:
            math = int(fr_num) / int(second_num)
            e.delete(0, END)
            e.insert(0, math)
    if type == "sub":
        if point in fr_num or point in second_num:
            math = float(fr_num) * float(second_num)
            e.delete(0, END)
            e.insert(0, math)
        else:
            math = int(fr_num) * int(second_num)
            e.delete(0, END)
            e.insert(0, math)
    if type == "percent":
        if point in fr_num or point in second_num:
            math = float(fr_num) % float(second_num)
            e.delete(0, END)
            e.insert(0, math)
        else:
            math = int(fr_num) % int(second_num)
            e.delete(0, END)
            e.insert(0, math)


def plus_minus():
    point = "-"
    curr = str(e.get())

    if point in curr:
        curr.translate({ord('-'): None})
        newst = curr.replace("-", "")
        e.delete(0, END)
        e.insert(0, newst)
    else:
        point += curr
        e.delete(0, END)
        e.insert(0, point)


def percent():
    first_number = e.get()
    global fr_num
    global type
    type = "percent"
    fr_num = str(first_number)
    e.delete(0, END)


def divide():
    first_number = e.get()
    global fr_num
    global type
    type = "divide"
    fr_num = str(first_number)
    e.delete(0, END)


def sub():
    first_number = e.get()
    global fr_num
    global type
    type = "sub"
    fr_num = str(first_number)
    e.delete(0, END)


def plus():
    first_number = e.get()
    global fr_num
    global type
    type = "plus"
    fr_num = str(first_number)
    e.delete(0 , END)


def minus():
    first_number = e.get()
    global fr_num
    global type
    type = "minus"
    fr_num = str(first_number)
    e.delete(0, END)


def flo():
    point = "."
    curr = e.get()

    if point not in curr:
        curr = e.get()
        e.delete(0, END)
        e.insert(0,curr + ".")
    else :
        pass


def clear():
    e.delete(0 , END)


root.title("Calculator")
root.geometry("350x285")
root.resizable(0, 0)
e = Entry(root, width =53, borderwidth = 15 )

buttonC = Button(root, text = "C" , height = 2 ,width = 10, borderwidth = 5 , command = clear )
buttonValue = Button(root, text = "+/-", height = 2,width = 10, borderwidth = 5,command = plus_minus)
buttonPercent = Button(root, text = "%", height = 2 ,width = 10, borderwidth = 5,command = percent)
button_divide = Button(root, text = "/", height = 2 ,width = 10, borderwidth = 5,command = divide)

button1  = Button(root, text = "1" , height = 2 ,width = 10, borderwidth = 5, command =lambda : add(1))
button2 = Button(root, text = "2", height = 2 ,width = 10, borderwidth = 5, command =lambda : add(2))
button3 = Button(root, text = "3", height = 2 ,width = 10, borderwidth = 5, command =lambda : add(3))
button_sub = Button(root, text = "x", height = 2 ,width = 10, borderwidth = 5 ,command = sub)

button4 = Button(root, text = "4", height = 2 ,width = 10, borderwidth = 5, command =lambda : add(4) )
button5 = Button(root, text = "5", height = 2 ,width = 10, borderwidth = 5, command =lambda : add(5) )
button6 = Button(root, text = "6", height = 2 ,width = 10, borderwidth = 5, command =lambda : add(6) )
button_minus = Button(root, text = "-", height = 2 ,width = 10, borderwidth = 5 ,command  = minus)

button7 = Button(root, text = "7", height = 2 ,width = 10, borderwidth = 5, command =lambda : add(7) )
button8 = Button(root, text = "8", height = 2 ,width = 10, borderwidth = 5, command =lambda : add(8) )
button9 = Button(root, text = "9", height = 2 ,width = 10, borderwidth = 5, command =lambda : add(9) )
button_plus = Button(root, text = "+", height = 2 ,width = 10, borderwidth = 5,command = plus)

button0 = Button(root, text = "0", height = 2 ,width = 23, borderwidth = 5, command =lambda : add(0) )
button_dot = Button(root, text = ".", height = 2 ,width = 10, borderwidth = 5,command = flo)
button_equal = Button(root, text = "=", height = 2 ,width = 10, borderwidth = 5,command = equal)

e.grid( row=0,column= 0 ,columnspan = 4)

button3.grid( row= 4 , column = 2)
button2.grid( row= 4, column = 1)
button1.grid( row= 4 ,column = 0)
button_sub.grid(row= 2 , column = 3)

button4.grid( row= 3 , column = 0)
button5.grid( row= 3 , column = 1)
button6.grid( row= 3 , column =2)
button_minus.grid( row= 3 , column =3)

button7.grid( row= 2 , column = 0)
button8.grid( row= 2 , column = 1)
button9.grid( row= 2 , column = 2)
button_plus.grid(row= 4 , column = 3)

button0.grid( row= 5 , column = 0 , columnspan= 2)
button_dot.grid(row= 5 , column = 2)
button_equal.grid(row= 5, column = 3)

buttonC.grid(row= 1 , column = 0)
buttonValue.grid(row= 1 , column = 1)
buttonPercent.grid(row= 1 , column = 2)
button_divide.grid(row= 1 , column = 3)

root.mainloop()
