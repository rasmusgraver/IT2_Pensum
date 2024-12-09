
def f(x):
    return x**2

print("  x | f(x)")
print("-"*10)
for x in range(-3, 4, 1):
    print(f"{x:3} | {f(x):2}")

