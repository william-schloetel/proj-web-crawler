import requests
import web_parser

 
# Making a GET request
r = requests.get('https://inlandempire.craigslist.org/cto/d/chino-hills-1968-ford-mustang-v8-very/7457995866.html')
 
# check status code for response received
# success code - 200
print(r)
 
num = web_parser.find_phone_number_from_HTML(r.text)
print(num)



