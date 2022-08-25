"""
Random Password Generator Using Python
"""
import random
import string

print("Welcome to password generator :) ")

# Input for the length of password
length = int(input("\nEnter the length of password: "))

# All lower case letters
lower = string.ascii_lowercase
# All upper case letters
upper = string.ascii_uppercase
# The string '0123456789'
num = string.digits

# A long string of ASCII letters that C locale interprets as punctuation
symbols = string.punctuation

# Merge the data
all = lower + upper + num + symbols

# Use random
temp = random.sample(all, length)

# Creating the password
password = "".join(temp)


print(password)
