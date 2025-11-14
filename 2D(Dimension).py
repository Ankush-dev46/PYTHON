# 2D(Dimensions) List
# 2D list = [list1,list2,list3] it is a collection of lists.

fruits = ["apple","banana","pineapple","orange"]
vegetables = ["carrots","potatos","lady's_Fringer"]
meat = ["chicken","fish","prok"]

groceries = [fruits,vegetables,meat]

print(groceries)
print(groceries[1])
print(groceries[0][0])

for x in groceries:
    print(x,end=",")

print()
for x in groceries:
    for y in fruits:
      print(y,end=",")
      
