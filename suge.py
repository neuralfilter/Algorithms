def doSearch (array, targetValue):
	min = 1
	max = len(array)-1
	guess = None

	while(max>min):
		guess = max+min/2
		if(array[guess]==targetValue):
			return guess;
		if(array[guess] < targetValue):
			min = guess+1
		else:
			max = guess-1
	return -1;

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
		41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
result = doSearch(primes, 73)
print(result)