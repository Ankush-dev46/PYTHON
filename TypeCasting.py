#type casting = CONVERTING THE DATA TYPE OF A VALUE TO ANOTHER DATA TYPE.
name = "BRO CODE"
age = "25"
gpa = "4.04"
isStudent = "False"

print(name)
print(type(name))

print(isStudent)
print(type(isStudent))

print(age)
age  = int(age)  #type casting
age += 1
print(age)
print(type(age))

print(gpa)
gpa = float(gpa)  #type casting
gpa += 3.0
print(gpa)
print(type(gpa))

