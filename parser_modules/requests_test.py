# Testing request w/ web_parser module
# Author: William S.
# Date: 03/14/22


import requests
import web_parser

# Making a GET request
r = requests.get('https://inlandempire.craigslist.org/cto/d/rialto-2013-ford-550/7457997884.html')
 
# check status code for response received
# success code - 200
print(r)

num = web_parser.find_phone_number_from_HTML(r.text)
print(num)



