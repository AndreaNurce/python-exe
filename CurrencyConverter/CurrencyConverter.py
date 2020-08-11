from tkinter import *
import math
from pynput.keyboard import Controller

keyboard = Controller()

options = [
    "Lek",
    "Euro",
    "Dollar",
    "Pound"
]
def testVal(inStr,acttyp):
    if acttyp == '1': #insert
        if not inStr.isdigit():
            return False
    return True

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def m():
    item = active.get()
    try :
        value=int(val.get())
        if item == options[0] and value > 0:
            try :
                label1['text'] = options[0] +" : "+ str(value) +" L"
                label2['text'] = options[1] + " : "+ str(round_up(value *0.0079, 3)) + " EUR"
                label3['text'] = options[2] + " : "+ str(round_up(value*0.0086, 3)) + " USD"
                label4['text'] = options[3] + " : "+ str(round_up(value *0.0069, 3)) + " GBP"
            except ValueError :
                pass

        if item == options[1] and value > 0:
            label1['text'] = options[0] + " : " + str(round_up(value * 126.27, 3)) + " L"
            label2['text'] = options[1] + " : " +str(value) + " EUR"
            label3['text'] = options[2] + " : " + str(round_up(value * 1.09, 3)) + " USD"
            label4['text'] = options[3] + " : " + str(round_up(value * 0.87, 3)) + " GBP"

        if item == options[2] and value > 0:
            label1['text'] = options[0] + " : " + str(round_up(value * 115.75, 3)) + " L"
            label2['text'] = options[1] + " : " + str(round_up(value * 0.92, 3)) + " EUR"
            label3['text'] = options[2] + " : " + str(value )+ " USD"
            label4['text'] = options[3] + " : " + str(round_up(value * 0.80, 3)) + " GBP"
        if item == options[3] and value > 0:
            label1['text'] = options[0] + " : " + str(round_up(value * 144.66, 3)) + " L"
            label2['text'] = options[1] + " : " + str(round_up(value * 1.15, 3)) + " EUR"
            label3['text'] = options[2] + " : " + str(round_up(value * 1.25, 3)) + " USD"
            label4['text'] = options[3] + " : " + str(value) + " GBP"
    except ValueError:
        pass

def callback(event):
    m()


root = Tk()
root.bind('<Return>',callback)
root.iconbitmap(r'\Users\Personal\PycharmProjects\CurrencyConverter\icon.ico')

root.title("Currency Converter")
root.geometry("500x700")
background = Canvas(root, height="200", width="200", bg="#000000")
background.pack(fill="both", expand=True)

val = Entry(background, font="arial", width=15, bg="#FEA680", validate="key")
val['validatecommand'] = (val.register(testVal),'%P','%d')
val.place(x=121, y=70, height=68)
active = StringVar()
active.set(options[0])

dropDown = OptionMenu(background, active, *options)
dropDown.config(bg="#FEDC3D", font="arial")
dropDown.place(width=500)

label1 = Label(background, text="Lek", font="arial", bg="#01ABAA")
label1.place(x=120, y=250, width=239, height=70)
label2 = Label(background, text="Euro", font="arial", bg="#01ABAA")
label2.place(x=120, y=350, width=239, height=70)
label3 = Label(background, text="Dollar", font="arial", bg="#01ABAA")
label3.place(x=120, y=450, width=239, height=70)
label4 = Label(background, text="Pound", font="arial", bg="#01ABAA")
label4.place(x=120, y=550, width=239, height=70)

inp = Button(background, font="arial", width=5, height=2, bg="#FEA680", bd=FALSE, text="Check!", padx=5, pady=5, command=m)
inp.place(x=290, y=70)
root.resizable(width=False, height=False)
root.mainloop()
