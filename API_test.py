import requests
import tkinter
from tkinter import *
import json
import sys
import urllib

##master = Tk()

##root = tkinter.Tk()
##root.title("Tkinterpractice")
##root.geometry("600x400")
locationvar = [""]
categoryvar=[""]
newvar = [""]
totalvar =[""]
###API call
def API_call():

    global locationvar
    global categoryvar
    global newvar
    global totalvar

    ##API call asking for the location and category of restaurants

    locationvar =input("Enter Location ")
    categoryvar =input("Enter Cuisine ")
    ###API key, headers, params
    api_key='T5r046Ko4ZGfX41i6KSz6YJglwp4UriL44HumY_8KATjldfs-VGDls5OSB4hOUNVv-t1H7Ks8P5xY0RbzZzeVb5kCFbyjscNn_Fb-JO1y-0N0sStkiPquAAMTlA9Y3Yx'
    headers = {'Authorization': 'Bearer %s' % api_key}
    params = {'location':locationvar, 'categories':categoryvar}

    ###url

    url='https://api.yelp.com/v3/businesses/search'

    ###requests

    req=requests.get(url, params=params, headers=headers)

###total number of restaurants in city
    newvar = json.loads(req.text)
    totalvar = newvar['total']
###writes variables to file
    f= open('varfile.txt', 'a')
    f.write(str(locationvar)+", ",)
    f.write(str(categoryvar)+ ", ",)
    f.write(str(totalvar)+ ", ",)
    f.close()


    
   
##API_call()
###API call

def API_totalbylocation():

    ##API call asking for the total number of restaurants in a specific location

    locationvar =input("Enter Location ")
    
    ###API key, headers, params
    api_key='T5r046Ko4ZGfX41i6KSz6YJglwp4UriL44HumY_8KATjldfs-VGDls5OSB4hOUNVv-t1H7Ks8P5xY0RbzZzeVb5kCFbyjscNn_Fb-JO1y-0N0sStkiPquAAMTlA9Y3Yx'
    headers = {'Authorization': 'Bearer %s' % api_key}
    params = {'location':locationvar}

    ###url

    url='https://api.yelp.com/v3/businesses/search'

    ###requests

    req=requests.get(url, params=params, headers=headers)

###total number of restaurants in city
    newvar = json.loads(req.text)
    totalvar = newvar['total']
###writes variables to file
    f= open('varfile.txt', 'a')
    f.write(str(locationvar)+", ",)
    f.write(str(totalvar)+ ", ",)
    f.close()

    return totalvar



