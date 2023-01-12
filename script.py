# UPDATED search using Selenium and BeautifulSoup library
#
# Author: William S.
# Date: 01/11/23


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support import expected_conditions as EC 
#import time

from webdriver_manager.chrome import ChromeDriverManager

import number_finder as n
from bs4 import BeautifulSoup
import requests
import pandas as pd 

chrome_options = Options()
chrome_options.add_argument("--headless")

page_url = 'https://sfbay.craigslist.org/search/sss#search=1~gallery~0~0'


# def find_phone_numbers_from_craigslist_posts(page_url, num_urls=20):
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.implicitly_wait(20)
#     driver.get(page_url)
#     list_of_elems = driver.find_elements(By.CLASS_NAME, 'titlestring')
#     urls = [elem.get_attribute('href') for elem in list_of_elems]
#     phone_numbers = []
#     for url in urls:
#         driver.get(url)
#         posting_body = driver.find_element(By.ID, 'postingbody')
#         phone_number = n.find_number(posting_body.text)
#         if phone_number:
#             phone_numbers.append(phone_number)
#     driver.quit()   
#     return phone_numbers

def find_phone_numbers_bs4(page_url, num_urls=20):
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)


    driver.implicitly_wait(20)
    driver.get(page_url)
    list_of_elems = driver.find_elements(By.CLASS_NAME, 'titlestring')
    urls = [elem.get_attribute('href') for elem in list_of_elems]
    driver.quit()
    phone_numbers = search_urls_for_phone_numbers(urls)
    create_csv_file(phone_numbers) 
    return phone_numbers

def search_urls_for_phone_numbers(urls):
    phone_numbers = []
    for url in urls:
        post_soup = generate_soup(url)
        posting_body_text = post_soup.find("section", id="postingbody").text.strip()
        phone_number = n.find_number(posting_body_text)
        if phone_number:
            phone_numbers.append(phone_number)
    print(phone_numbers)
    return phone_numbers

def generate_soup(url):
	r = requests.get(url)
	post_soup = BeautifulSoup(r.content, 'html.parser')
	return post_soup

def create_csv_file(phone_numbers):
	data_frame = pd.DataFrame(phone_numbers)
	data_frame.to_csv('phone_numbers.csv')