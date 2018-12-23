num = int(raw_input("what is your number: "))


if num % 2 != 0:
    print("your number is odd")
elif num % 4 == 0:
    print("number is multipul of 4")
else:
    print("this is an even number")

num = int(raw_input("what is your number: "))
check = int(raw_input("enter number to check if first input is equally divisable by this number:"))

div = num % check

if div == 0:
    print("number divided evenly")
else:
    print("remainder of numbers is: " + str(div))
