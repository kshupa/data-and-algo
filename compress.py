def compress(s):
	result = ''
	length = len(s)
	counter = 1
	i = 1

	if length == 0:
		return ''

	if length == 1:
		return s+'1'

	while i < length:

		if s[i] == s[i-1]:
			counter += 1
		
		else:
			result = result + s[i-1] + str(counter)
			counter = 1
		
		i += 1 

	result = result + s[i-1] + str(counter)

	return result


print(compress('aaBBAAccccGGn'))
