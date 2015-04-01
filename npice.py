def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

def summ(n):
	if n==0:
		return 0
	else:
		return n+summ(n-1)

print(summ(6))


