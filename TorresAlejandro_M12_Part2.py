
#Importing tkinter
from tkinter import *
import tkinter.messagebox

#tk window
root = Tk()

#define the function and logs of of window
def function():
    root.destroy()  
# Calcualte
def response():
        # Display an info dialog box.
    tkinter.messagebox.showinfo('Response',\
                                'Order sent.')
def calculate():
#SETS the price and tac rate    
    SALES_CHARGE_RATE=0.07
    HOT_DOG_PRICE=1.99
    #textbox values
    value1 = int(BeefDogAmount.get())
    value2 = int(PorkDogsAmount.get())
    value3 = int(TurkeyDogsAmount.get())
    #Calculation part
    NumTotalDog= (value1+value2+value3)
    SubTotal = (NumTotalDog * HOT_DOG_PRICE)
    SalesTax = (SubTotal*SALES_CHARGE_RATE)
    TotalCost = (SubTotal + SalesTax)
    #Set display values
    sub_total = "SubTotal: $" + str(int(SubTotal))
    tax_value = "SalesTax: $" + str(format(SalesTax,',.2f'))
    totallabel = "Total: $" + str(format(TotalCost,',.2f'))
    #grid position
    Label(root, text=sub_total).grid(row = 7)
    Label(root, text=tax_value).grid(row = 8)
    Label(root, text=totallabel).grid(row = 9)
#Set window shows name and orderform
root.title('Alejandro Torres Drone Dogs Order Form')
#Creating variables

BeefDogAmount = StringVar()
PorkDogsAmount = StringVar()
TurkeyDogsAmount = StringVar()
sub_total = StringVar()
tax_value = StringVar()
totallabel = StringVar()
#entry point for vairiables
BeefDogsProductAmount= Entry(root, textvariable = BeefDogAmount).grid(row = 0, column=1)
PorkDogsProductAmount= Entry(root, textvariable = PorkDogsAmount).grid(row = 1, column=1)
TurkeyDogsProductAmount= Entry(root, textvariable = TurkeyDogsAmount).grid(row = 2, column=1)
#Is the asking part to user
Label(root, text = "Enter how many Beef Dogs you want :").grid(row=0,column = 0)
Label(root, text = "Enter how many Pork Dogs you want:").grid(row=1,column = 0)
Label(root, text = "Enter how many Turkey Dogs you want:").grid(row=2,column = 0)
#sets buttons up calculate quit and submit
Button(root, text = ("Quit"), command= function).grid(row=6, column = 2)
Button(root, text = ("Submit Order"), command= response ).grid(row=6, column = 1)
Button(root, text = ("Calculate Total"), command= calculate).grid(row=6 ,column =0)
# main window.
root.mainloop()
