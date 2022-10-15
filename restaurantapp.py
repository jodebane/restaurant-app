import API_test
import tkinter
from tkinter import *
import random
import requests
from tkinter.ttk import *

##root for Tkinter app
root = tkinter.Tk()
root.title("Tkinterpractice")
root.geometry("600x400")

###deletes existing text from file
with open('varfile.txt', 'w') as fp:
    fp.truncate(0)
###calls the API call function from API module
API_test.API_call()
###pritns the text from the file after API call
with open('varfile.txt', 'r') as newfile:
    var1 = newfile.readlines()
print(var1)

##SPLITS var1 result into 3 different variables
var1split = (var1[0].split(','))

###Takes number of restaurants from var1
print(var1split[2])

##Genarates tkinter labels
def size_2():
   text.config(font=('Helvetica bold',40))

##Tkinter labels

labeltitle = tkinter.Label(root, text="Restaurant app").pack()
label  = tkinter.Label(root, text=var1).pack()

###mainloop for Tkinter window
root.mainloop()


