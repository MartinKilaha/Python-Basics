nambari = int(input("Enter number"))

if nambari % 2 == 0:
    print(f"{nambari} is even number")
else:
    print(f"{nambari} is odd number")

age = int(input("Enter age"))

if age <= 18 and age >= 100:
    print(f"{age} is no voter")
else:
    print(f"{age} is voter")
