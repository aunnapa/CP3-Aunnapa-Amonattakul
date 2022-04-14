from tkinter import *
import math

def leftclickButton(event):
    print(float(textboxWeight.get())/math.pow((float(textboxHeight.get())/100),2))
    BMI = float(textboxWeight.get())/math.pow((float(textboxHeight.get())/100),2)
    if BMI > 30.0 :
        textResult.configure(text='อ้วนมาก',fg='red')
    elif BMI >= 25 :
        textResult.configure(text='อ้วน',fg='red')
    elif BMI >= 23 :
        textResult.configure(text='น้ำหนักเกิน',fg='red')
    elif BMI >= 18.6 :
        textResult.configure(text='น้ำหนักปกติ เหมาะสม',fg='green')
    else:
        textResult.configure(text='ผอมเกินไป',fg='red')



mainWindow = Tk()
labelHeight = Label(mainWindow,text ='ส่วนสูง (cm.)')
labelHeight.grid(row=0,column=0)
textboxHeight = Entry(mainWindow)
textboxHeight.grid(row=0,column=1)
labelWeight = Label(mainWindow,text = 'น้ำหนัก (Kg.)')
labelWeight.grid(row=1,column=0)
textboxWeight = Entry(mainWindow)
textboxWeight.grid(row=1,column=1)
CalculateButton = Button(mainWindow, text='คำนวณ')
CalculateButton.grid(row=3)
CalculateButton.bind('<Button-1>',leftclickButton)
textResult = Label(mainWindow, text ='ผลลัพธ์')
textResult.grid(row=3,column=1)

mainWindow.mainloop()