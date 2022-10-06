import requests
import json
import sys
import urllib

locationvar =input("Enter Location ")
categoryvar =input("Enter Cuisine ")

api_key='T5r046Ko4ZGfX41i6KSz6YJglwp4UriL44HumY_8KATjldfs-VGDls5OSB4hOUNVv-t1H7Ks8P5xY0RbzZzeVb5kCFbyjscNn_Fb-JO1y-0N0sStkiPquAAMTlA9Y3Yx'
headers = {'Authorization': 'Bearer %s' % api_key}
params = {'location':locationvar, 'categories':categoryvar}

url='https://api.yelp.com/v3/businesses/search'

req=requests.get(url, params=params, headers=headers)


newvar = json.loads(req.text)

print(newvar['total'])



