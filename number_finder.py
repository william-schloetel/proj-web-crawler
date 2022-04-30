# Number parsing function.
# Extracts integer array from string of char and int
# Author: William S.
# Date: 03/14/22


def find_number(text_str):
	i, length = 0, len(text_str) - 1
	while(i < length):
		if text_str[i:i+4] == 'http':					#if you find hyperlink
			while(text_str[i] != ' ' and i < length):
				i += 1
		num = translate_number(text_str[i:length])
		if len(num) == 10:
			return num
		i += 1
	return 


def translate_number(num_string, max_length=10):
	"""Returns an int array of num_string. 
	Parses until it finds a non-number entity, and then returns the array. 
	Ignores "-", ")", "(", and " "

	>>> parse_number("Sixsix1 6two3 51one6")
	[6, 6, 1, 6, 2, 3, 5, 1, 1, 6]

	>>> parse_number("One23 Four56 Seventy9one")
	[1, 2, 3, 4, 5, 6, 7, 0, 9, 1]

	>>> parse_number("1 805 four three three three three four sixty", 12)
	[1, 8, 0, 5, 4, 3, 3, 3, 3, 6, 8]

	>>> parse_number("1 2 twee")
	[1, 2]

	>>> parse_number("1  FoUR-67    2 SHIT")
	[1, 4, 6, 7, 2]

	"""
	num_string = num_string.lower()			# make letters lower case
	arr = []
	while(len(num_string) > 0):
		if len(arr) >= max_length:
			return arr
		try:								# found integer 
			k = int(num_string[0])
			arr.append(k)
			num_string = num_string[1:]
		except ValueError:					# found typed number
			if num_string[0] == ' ' or num_string[0] == "-":
				num_string = num_string[1:]
			elif num_string[0] == "(" or num_string[0] == ")":
				num_string = num_string[1:]
			elif num_string[:4] == "zero":
				arr.append(0)
				num_string = num_string[4:]
			elif num_string[:3] == "one":
				arr.append(1)
				num_string = num_string[3:]
			elif num_string[0] == "t":
				if num_string[:3] == "ten":
					arr.append(1)
					arr.append(0)
					num_string = num_string[3:]
				elif num_string[:6] == "twenty":
					arr.append(2)
					arr.append(0)
					num_string = num_string[6:]
				elif num_string[:3] == "two":
					arr.append(2)
					num_string = num_string[3:]
				elif num_string[:6] == "thirty":
					arr.append(3)
					arr.append(0)
					num_string = num_string[6:]
				elif num_string[:5] == "three":
					arr.append(3)
					num_string = num_string[5:]		
				else:
					return arr
			elif num_string[0] == "f":
				if num_string[:6] == "fourty":
					arr.append(4)
					arr.append(0)
					num_string = num_string[6:]
				elif num_string[:4] == "four": 
					arr.append(4)
					num_string = num_string[4:]
				elif num_string[:4] == "five":
					arr.append(5)
					num_string = num_string[4:]
				elif num_string[:5] == "fifty":
					arr.append(5)
					arr.append(0)
					num_string = num_string[5:]
				else:
					return arr
			elif num_string[0] == "s":
				if num_string[:5] == "sixty":
					arr.append(6)
					arr.append(0)
					num_string = num_string[5:]
				elif num_string[:3] == "six":
					arr.append(6)
					num_string = num_string[3:]
				elif num_string[:7] == "seventy":
					arr.append(7)
					arr.append(0)
					num_string = num_string[7:]
				elif num_string[:5] == "seven":
					arr.append(7)
					num_string = num_string[5:]	
				else:
					return arr
			elif num_string[:6] == "eighty":
				arr.append(8)
				arr.append(0)
				num_string = num_string[6:]
			elif num_string[:5] == "eight":
				arr.append(8)
				num_string = num_string[5:]
			elif num_string[:6] == "ninety":
				arr.append(9)
				arr.append(0)
				num_string = num_string[6:]
			elif num_string[:4] == "nine":
				arr.append(9)
				num_string = num_string[4:]
			else:
				return arr	
	return arr


