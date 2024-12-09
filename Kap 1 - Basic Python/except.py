
def f(x):
    return x**2

inp = input("Tast et tall (x for avslutt): ")
while inp != "x":
    t = int(inp)
    print(f"f({t}) = {f(t)}")
    print("Prøv igjen!")

    inp = input("Tast et tall (x for avslutt): ")


print()
print("Takk for meg")
