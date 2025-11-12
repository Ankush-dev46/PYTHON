# INDEXING : Accessing elements of a Sequence using "[] = indexing operator",
# [START : END : STEP]

credit_num = "7894-5646-546-646-5455"

print(credit_num[0:5])
print(credit_num[::])
print(credit_num[-1])
print(f"CREDIT CARD NUMBER IS(XXXX-XXXX-XXX-XXX-{credit_num[-4:]})")
print(credit_num[::-1])
print(credit_num[::2])
print(credit_num[::3])

print(help(str))