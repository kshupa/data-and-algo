# Check if string has all unique characters and return True, otherwise False

def unique_check(s):
	

	string = ''

	for i in s:
		if i not in string:
			string = string + i 
	
	return len(s) == len(string)
	






print(unique_check('chekjgutoslngle'))