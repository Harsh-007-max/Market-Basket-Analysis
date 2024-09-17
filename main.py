from tkinter import *

import Data_cleaning
import groceries_mining

bg="#FFFFFF"
fg="#000000"
font = ("Courier",12,"bold")

# function to call
def onSubmit():
    support = float(inputSupport.get())
    confidence = float(inputConfidance.get())
    tableName = Data_cleaning.cleanData()
    finalTableName = groceries_mining.associationRuleMining(support,confidence,tableName=tableName)
    print(f"final Table Name: {finalTableName}")
    with open(finalTableName) as f:
        data = f.readlines()
        for i in data:
            output.insert(END,i)
        if len(data)==0:
            output.insert(END,"No rules found")

#Tkinter config
window = Tk()
window.title("Association Rule mining")
window.minsize(width=500,height=500)

#labels
labelSupport = Label(text="Enter Support:")
labelConfidance = Label(text="Enter Confidence:")

#input
inputSupport = Entry(width=20)
inputConfidance = Entry(width=20)

# output listbox
output = Listbox(window,width=50,height=20)

submit = Button(text="Submit",bg=bg,fg=fg,font=font,command=onSubmit)

labelSupport.grid(row=0,column=0)
inputSupport.grid(row=0,column=1)
labelConfidance.grid(row=1,column=0)
inputConfidance.grid(row=1,column=1)
output.grid(row=3,column=1,columnspan=2,padx=10,pady=10)
submit.grid(row=2,column=1)
window.mainloop()
