marks = int(input("Enter Marks"))

if marks >= 80 and marks <= 100:
    print("you have an A")
elif marks >= 60 and marks <= 79:
    print("You have B")
elif marks >= 40 and marks <= 59:
    print("You have C")
elif marks >= 0 and marks <= 39:
    print("You have terrebly failed")
else:
    print("Wrong input")
