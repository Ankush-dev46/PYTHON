name = input("ENTER YOUR NAME:")
lenght = len(name)
print(lenght)

#FIND METHOD (RETURNS THE INDEX OF STRING)
fin=name.find("k")
print(fin)

#CAPITALIZE,UPPER_CASE,LOWER_CASE,IS_DIGIT,IS_ALPHABETS.
name_1 = input("ENTER A NAME1:").capitalize()
print(name_1)
name_2 = input("ENTER A NAME2:").upper()
print(name_2)
name_3 = input("ENTER A NAME3:").lower()
print(name_3)

num = input("ENTER ONLY NUMBERS:").isdigit()
print(num)

alp = input("ENTER SOMETHING:").isalpha()
print(alp)

#COUNT,REPLACE

phone_number = input("ENTER A PHONE NUMBER: ")
print("Original phone number:", phone_number)

colon_count = phone_number.count(":")
print("Number of colons:", colon_count)

phone_number1 = input("ENTER A PHONE NUMBER: ")
modified_phone_number = phone_number1.replace(":", "-")
print("Modified phone number:", modified_phone_number)

# Validation User Input Exercise 
user_name = input("ENTER A NAME:")
leng = user_name.find(" ")

if len(user_name) > 12:
    print("TOO MUCH // YOU HAVE A BIG NAME")
elif leng != -1:  # Check if a space was found (find returns -1 if not found)
    print("NO SPACING IS NEED")
elif not user_name.isalpha():
    print("ENTER ONLY LETTERS")
else:
    print(user_name)