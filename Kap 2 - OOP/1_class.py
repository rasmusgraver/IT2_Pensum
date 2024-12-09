class Person:
    def __init__(self, navn):
        self.navn = navn

    def __str__(self) -> str:
        return f"En person ved navn {self.navn}"


per = Person("Rasmus")
per2 = Person("Jon")

print(per)
print(per2)
print(per.navn)

