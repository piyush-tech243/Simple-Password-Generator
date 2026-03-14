import random
import string
print("password generator:")
length=int(input("Enter password length:"))
letters=input("Include letters? (yes/no):")
numbers=input("Include numbers? (yes/no):")
symbols=input("Include symbols? (yes/no):")

characters=""

if letters=="yes":
    characters+=string.ascii_letters
if numbers=="yes":
    characters+=string.digits
if symbols=="yes":
    characters+=string.punctuation

if characters=="":
    print('please select at least one option!')
else:
    password=""
    for i in range(length):
        password+=random.choice(characters)
    print("Generated Password:",password)        
