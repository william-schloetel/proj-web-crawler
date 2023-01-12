# Web crawler for retrieving Craigslist data.
#
# Author: William S. 
# Date: 03/14/22

import script as sp

page_url = 'https://sfbay.craigslist.org/search/sss#search=1~gallery~0~0'

def search(num_urls=20):
	phone_numbers = sp.find_phone_numbers_bs4(page_url=page_url, num_urls=20)
	sp.create_csv_file(phone_numbers)

def main():
	while(True):
		print("How many Craigslist posts would you like to search for phone numbers?")	
		num_posts = input()
		try:
			int(num_posts)
			print("Searching " + num_posts + " posts...")
			search(num_urls=num_posts)
			print("Finished search. Any retrieved phone numbers have been written to phone_numbers.csv")
			return
		except ValueError:
			print("Error: Input must be an integer")


if __name__ == "__main__":
	main()

