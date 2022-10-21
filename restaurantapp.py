import API_test
import tkinter
from tkinter import *
import random
import requests
from tkinter.ttk import *




##root for Tkinter app
root = tkinter.Tk()
root.title("Tkinterpractice")
root.geometry("800x400")
with open('inputfile.txt', 'w') as fp:
    fp.truncate(0)
###takes input to add to inputfile
def inputfile():
   
    locvarentry = input('Enter location ')
    catvarentry = input('Enter cuisine ')
    with open('inputfile.txt', 'w') as fw:
        fw.write(str(locvarentry)+ ",")
        fw.write(str(catvarentry)+ ",")


    

inputfile()
###deletes existing text from file
with open('varfile.txt', 'w') as fp:
    fp.truncate(0)
###calls the API call function from API module
API_test.API_call()
###pritns the text from the file after API call
with open('varfile.txt', 'r') as newfile:
    var1 = newfile.readlines()


##SPLITS var1 result into 3 different variables
var1split = (var1[0].split(','))


###Takes location

location = (var1split[0])


###Takes cuisine

cuisine=(var1split[1])

###Takes number of restaurants from var1
numberofrestaurants = (var1split[2])

##Genarates tkinter labels


##Tkinter labels

labeltitle = tkinter.Label(root, text="Restaurant app",font=("Helvetica",40)).pack()
label  = tkinter.Label(root, text="The number of "+ cuisine +  " restaurants in " + location+ " is " +numberofrestaurants,
font=("Arial",24)).pack()



###mainloop for Tkinter window
root.mainloop()




