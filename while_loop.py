#WHILE LOOP : EXECUTE SOME CODE WHITH SOME CONDITION IS REMAINS TRUE. 
name = input("ENTER YOUR NAME:")
print(name)
age = int(input("ENTER YOUR AGE:"))
print(age)

while name == "":
    print("YOU DID NOT ENTER YOUR NAME:")
    name = input("ENTER YOUR NAME:")
    print(name)

while age<18 :
    print("YOU ARE CHILD,YOU SHOULD BE 18+")
    age = int(input("ENTER YOUR AGE:"))
    print(age)

food = input("WHAT FOOD YOU WANT TO EAT('Q'/'q' for Exit):")
print(f"YOU LIKE TO EAT {food}")

while not (food == "Q" or food == "q"):
    food = input("WHAT FOOD YOU WANT TO EAT('Q'/'q' for Exit):")
    print(f"YOU LIKE TO EAT {food}")

print("BYE")

num = int(input("ENTER A NUMBER FROM 1 TO 10:"))
print(num)
while not (num > 0 and num < 10):
    num = int(input("ENTER A NUMBER FROM 1 TO 10:"))
    print(num)