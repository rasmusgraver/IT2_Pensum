def head():
	linje(1, True)
	print("   ", "-"*4*kolonner)

def linje(n, head=False):
	if head:
		print(f"    ", end="")
	else:
		print(f"{n:2} |", end="")
	for i in range(1, kolonner+1):
		print(f"{i*n:4}", end="")
	print()

kolonner = 12
head()
for i in range(1, kolonner+1):
	linje(i)

print()
