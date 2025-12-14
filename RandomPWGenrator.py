import random
import string
pass_len=int(input("enter the length of password"))
charval=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(pass_len):
    password+=random.choice(charval)
print("your random password is",password)