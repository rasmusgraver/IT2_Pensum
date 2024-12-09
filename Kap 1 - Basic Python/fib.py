
tot = 0

def fib(n):
	global tot
	tot +=1
	if n <= 1:
		return 1

	return fib(n-1) + fib(n-2)


for i in range(10):
	print(f"{fib(i)}", end=" ")

print()
print(f"Totalt: {tot}")
