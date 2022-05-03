import search_retrieval

def search(starting_post=200, link_max=10):
	phone_numbers = search_retrieval.retrieve_phone_nums(starting_post=int(starting_post), link_max=int(link_max))
	search_retrieval.create_csv_file(phone_numbers)

def prompt():
	while(True):
		print("How many Craigslist posts would you like to search for phone numbers?")
	
		num_posts = input()
		try:
			int(num_posts)
			print("Searching " + num_posts + " posts...")
			search(link_max=num_posts)

			print("Finished search. Any retrieved phone numbers have been written to phone_numbers.csv")
			return


		except ValueError:
			print("Error: Input must be an integer")


prompt()

