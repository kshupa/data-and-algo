def large_cont_sum(arr):

	if len(arr) < 1:
		return None

	max_sum = current_sum = arr[0]

	for num in arr[1:]:
		current_sum = max(current_sum+num, num)
		max_sum = max(current_sum, max_sum)

	return max_sum





print(large_cont_sum([10,-1,5,-1,2,10,-5]))
