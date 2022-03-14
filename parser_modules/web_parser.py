import number_parser

# Finds a phone number located within a Craigslist post.


def find_phone_number_from_file_name(file_name):
	"""Returns a phone number array if a phone number exists within HTML file, 
	else prints an error statement

	"""
	with open(file_name, 'r') as fileObject:
		file_str = fileObject.read()
		return find_phone_number_from_HTML(file_str)
		

def find_phone_number_from_HTML(file_str):
	try:
		start = file_str.index('<section id="postingbody">')
		start = file_str.index('</div>', start) + 5
		end = file_str.index('</section>', start)
	except:
		return print('File does not contain <section id="postingbody">')

	while(start < end):
		num = number_parser.parse_number(file_str[start:end])
		if len(num) >=7  and len(num) <= 11:
			return num
		start += 1
	return print("No number found")


def print_phone_number(arr):
	"""Returns a string of the arr printed in the format ###-###-####, if len(arr) == 11. 
	
	>>> num_print([8,0,5,1,2,3,4,5,6,7])
	"(805)-123-4567"

	"""
	if len(arr) == 10:
		print("(" + str(arr[0]) + str(arr[1]) + str(arr[2]) + ")" + "-" + \
			str(arr[3]) + str(arr[4]) + str(arr[5]) + "-" + str(arr[6]) + \
			str(arr[7]) + str(arr[8]) + str(arr[9]))
	else:
		print("Not phone number")











