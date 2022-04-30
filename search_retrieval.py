from bs4 import BeautifulSoup
import requests
import pandas as pd
import number_finder


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 \
				(KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
headers = {'User-Agent' : user_agent}


# ***************************************************************************** #
# 					   		 Phone Number Retrieval 						    #
# ***************************************************************************** #

def retrieve_phone_nums(starting_post, link_max):
	links = search_page_find_links(search_page_generate_soup(starting_post), link_max)
	text_db = create_list_of_post_text(links)
	phone_numbers = []
	for text in text_db:
		num = number_finder.find_number(text)
		if num != None:
			phone_numbers.append(num)
	return phone_numbers

def create_csv_file(phone_numbers):
	data_frame = pd.DataFrame(phone_numbers)
	data_frame.to_csv('phone_numbers.csv')


# ***************************************************************************** #
# 					   	        Helper Functions						        #
# ***************************************************************************** #

# ------------------ Craigslist 'SEARCH PAGE' Link Extraction ----------------- #

def search_page_generate_soup(starting_post):
	url = f'https://sfbay.craigslist.org/search/sss?s={starting_post}'
	r = requests.get(url)
	search_page_soup = BeautifulSoup(r.content, 'lxml')
	return search_page_soup

def search_page_find_links(search_page_soup, link_max=None):
	post_list = search_page_soup.find_all("a", class_="result-image gallery", limit=link_max)
	links = []
	for post in post_list:
		links.append(post['href'])
	return links


# --------------------- Craigslist 'POST' Text Generation --------------------- #

def generate_post_soup(url):
	r = requests.get(url)
	post_soup = BeautifulSoup(r.content, 'html.parser')
	return post_soup

def find_post_text(post_soup):
	text = post_soup.find("section", id="postingbody").text.strip()
	return text

def create_list_of_post_text(links):
	text_db = []
	for url in links:
		post_soup = generate_post_soup(url)
		text_db.append(find_post_text(post_soup))
	return text_db



