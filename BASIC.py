#VARIABLES = A CONTAINER FOR STORING DATA VALUES(STRINS,INTEGERS,FLOATS,BOOLEANS).
#A VARIABLE BEHAVES AS A CONTAINER FOR DATA VALUES.

#F-STRING = A STRING LITERALS THAT IS PREFACED WITH THE LETTER 'F' OR 'f'.IT IS USED TO EMBED EXPRESSIONS INSIDE STRING LITERALS, USING A MINIMAL SYNTAX.

#string
name = "BRO CODE" 
FOOD = 'PIZZA'
EMAIL = "CODE_Gmail@123.com"

print(name)
print(FOOD)
print(EMAIL)
print(f"HELLO {name}, YOUR FAVORITE FOOD IS {FOOD} AND YOUR EMAIL IS {EMAIL}")
print("HELLO {}, YOUR FAVORITE FOOD IS {} AND YOUR EMAIL IS {}".format(name,FOOD,EMAIL))

#integer
age = 25
quntity = 6
price = 56

print(age)
print(quntity)
print(price)
print(f"YOUR AGE IS {age}, YOU WANT {quntity} PIZZAS AND EACH PRICE IS {price}")
print("your age is {},you want {} pizzas and each cost is {}".format(age,quntity,price))

#float 
gpa = 7.04
total = 584.8545
distance = 78.425

print(gpa)
print(total)
print(distance)
print(f"YOUR GPA IS {gpa}, YOUR TOTAL AMOUNT IS {total} AND DISTANCE IS {distance}")
print("your gpa is {}, your total amount is {} and distance is {}".format(gpa,total,distance))


#boolean
isStudent  = True
is_for_sale = False

print(isStudent)
print(is_for_sale)
print(f"ARE YOU A STUDENT? {isStudent}, IS IT FOR SALE? {is_for_sale}")
print("are you a student? {}, is it for sale? {}".format(isStudent,is_for_sale))
#boolean = A DATA TYPE WITH TWO POSSIBLE VALUES: TRUE OR FALSE.
