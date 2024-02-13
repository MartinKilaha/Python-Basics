# arithmetic operators
nambari = 67
nambari2 = 29
print(nambari + nambari2)
print(nambari - nambari2)
print(nambari * nambari2)
print(nambari / nambari2)
print(nambari % nambari2)
# nambari=int(input(nambari))

# comparison operator
nambari3 = int(input("Enter First number :"))
nambari4 = int(input("Enter Second number :"))
print(f"{nambari3} is equal to {nambari4} : {nambari3 == nambari4}")
print(f"{nambari3} is not equal to {nambari4} : {nambari3 != nambari4}")
print(f"{nambari3} is less than {nambari4} : {nambari3 < nambari4}")
print(f"{nambari3} is greater than {nambari4} : {nambari3 > nambari4}")
print(f"{nambari3} is less than or equals to {nambari4} : {nambari3 > nambari4}")
print(f"{nambari3} is greater than or equals to {nambari4} : {nambari3 > nambari4}")

# logical operators
nambari5 = int(input("Bonyeza nambari:"))
nambari6 = int(input("Bonyeza Pili:"))

print(f"{nambari5} and {nambari6} are both false: {nambari5 == nambari6 and nambari5 > nambari6}")
print(f"{nambari5} and {nambari6} one is true: {nambari5 == nambari6 or nambari5 > nambari6}")
