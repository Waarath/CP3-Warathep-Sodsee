from tkinter import *
import math

def LeftButtonClick(event):
    ResultBMI = (round(float(TextBoxWeight.get())/math.pow(float(TextBoxHeight.get())/100,2),2))
    if ResultBMI >= 30:
        TextResult = "Super Fat"
    elif ResultBMI >= 25:
        TextResult = "Fat"
    elif ResultBMI >= 23:
        TextResult = "OverWeight"
    elif ResultBMI >= 18.6:
        TextResult = "Normal"
    else:
        TextResult = "Too Thin"
    labelResult.configure(text=TextResult)
    labelResultFloat.configure(text=ResultBMI)



MainWindow = Tk()

#Height
labelHeight = Label(MainWindow,text="Height (Cm.)",font=40).grid(row=0,column=0)
TextBoxHeight = Entry(MainWindow)
TextBoxHeight.grid(row=0,column=1)
#Weight
labelWeight = Label(MainWindow,text="Weight (Kg.)",font=40).grid(row=1,column=0)
TextBoxWeight = Entry(MainWindow)
TextBoxWeight.grid(row=1,column=1)

#Calculate
CalculateButton = Button(MainWindow,text="Cal",font=10,width=5,height=2)
CalculateButton.bind('<Button-1>',LeftButtonClick)
CalculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text='Result',font=40)
labelResult.grid(row=2,column=1)

labelResultFloat = Label(MainWindow,text='BMI',font=40)
labelResultFloat.grid(row=3,column=1)

MainWindow.mainloop()