from tkinter import *

def btn(numbers):
    global operator
    operator = operator + str(numbers)
    txt_input.set(operator)

def clear():
    global operator
    sumup = 

screen = Tk()
screen.title('Kalkulator')

operator = ''
txt_input = StringVar(value='Start Calculating')

Display = Entry(screen, font=('arial', 30, 'bold'), fg="white", bg="blue",
                justify="right", bd=50, textvariable=txt_input)
Display.grid(columnspan=4)

btn7 = Button(screen, padx=30, pady=15, bd=8, fg="black",
              font=("arial", 30, "bold"), text="7" ).grid(row=1, column=0)
btn8 = Button(screen, padx=30, pady=15, bd=8, fg="black",
              font=("arial", 30, "bold"), text="8" ).grid(row=1, column=1)
btn9 = Button(screen, padx=30, pady=15, bd=8, fg="black",
              font=("arial", 30, "bold"), text="9" ).grid(row=1, column=2)
btnC = Button(screen, padx=30, pady=15, bd=8, fg="black",
              bg="yellow", font=("arial", 30, "bold"), text="C", ).grid(row=1,
                                                                        column=3)
btn4 = Button(screen, padx=30, pady=15, bd=8, fg="black",
              font=("arial", 30, "bold"), text="4" ).grid(row=2, column=0)
btn5 = Button(screen, padx=30, pady=15, bd=8, fg="black",
              font=("arial", 30, "bold"), text="5" ).grid(row=2, column=1)
btn6 = Button(screen, padx=30, pady=15, bd=8, fg="black",
              font=("arial", 30, "bold"), text="6" ).grid(row=2, column=2)
btnP = Button(screen, padx=32, pady=15, bg = "yellow", bd=8, fg="black",
              font=("arial", 30, "bold"), text="+" ).grid(row=2, column=3)
btn1 = Button(screen, padx=30, pady=15, bd=8, fg="black",
              font=("arial", 30, "bold"), text="1" ).grid(row=3, column=0)
btn2 = Button(screen, padx=30, pady=15, bd=8, fg="black",
              font=("arial", 30, "bold"), text="2").grid(row=3, column=1)
btn3 = Button(screen, padx=30, pady=15, bd=8, fg="black",
              font=("arial", 30, "bold"), text="3" ).grid(row=3, column=2)
btnM = Button(screen, padx=36, pady=15, bd=8, fg="black",
              font=("arial", 30, "bold"), text="-", bg= "yellow" ).grid(row=3,
                                                                        column=3)
btn0 = Button(screen, padx=30, pady=15, bd=8, fg="black",
              font=("arial", 30, "bold"), text="0").grid(row=4, column=0)
btnE = Button(screen, padx=30, pady=15, bd=8, fg="black",
              font=("arial", 30, "bold"), text="=", bg="yellow").grid(row=4, column=1)
btnx = Button(screen, padx=30, pady=15, bd=8, fg="black",
              font=("arial", 30, "bold"), text="x", bg="yellow").grid(row=4, column=2)
btnD = Button(screen, padx=37, pady=15, bd=8, fg="black",
              font=("arial", 30, "bold"), text="/", bg="yellow").grid(row=4, column=3)

screen.mainloop()
