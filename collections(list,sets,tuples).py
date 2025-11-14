# COLLECTION = SINGLE "VARIABLE" used to store multiple values.
# List = [] Ordered and changeable,Duplicates Ok
# Set =  {} Unordered and Immutable,but Add/Remove ok,No Duplicates.
# Tuple = () Ordered and Unchangeable.Duplicate ok,Faster.

# LISTS []
fruits = ["apple","banana","pienapple","strawberry","berry"]
print(fruits)
print()
print(fruits[0])
print(fruits[3])
print(fruits[2])
print(fruits[1])

for x in fruits:
    print(x,end=",")

print()

for x in fruits:
    print(x,end=" ")

fruits = ["apple","banana","pienapple","strawberry","berry"]
print(fruits)

# print(dir(fruits))
# print(help(fruits))
print(len(fruits))
print("apple" in fruits)
fruits.append("apple1")
fruits.append("banana")
print(fruits)
print(fruits.count("banana"))
print(fruits.index("banana"))
fruits.insert(0,"apple1")
print(fruits)
fruits[0]="orange"
print(fruits)
fruits.remove("apple1")
print(fruits)
print(fruits.sort())
print(fruits)
print(fruits.reverse())
print(fruits)

# SET METHODS.

fruits = {"apple","banana","pineapple","strawberry"}
print(fruits)
fruits.add("orange")
print(fruits)
fruits.remove("orange")
print(fruits)
fruits.pop() # Removes items from index:'0'
print(fruits)
fruits.clear()
print(fruits)

# Tuple Methods

fruits = ("apple","banana","strawberry","berry","apple","apple")
print(fruits)

print(fruits.count("apple"))
print(fruits.index("apple"))

for x in fruits:
    print(x,end=",")