import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Generating Simple password
simple_password =""

for letter in range (1,nr_letters+1):
    simple_password += random.choice(letters)
for symbol in range (1,nr_symbols+1):
    simple_password += random.choice(symbols)
for number in range (1,nr_numbers):
    simple_password += random.choice(numbers)
print(f"simple_password is {simple_password}")

#Generating complex password

complex_password =[]
complex_pass = ""

for letter in range (1,nr_letters+1):
    complex_password += random.choice(letters)
for symbol in range (1,nr_symbols+1):
    complex_password += random.choice(symbols)
for number in range (1,nr_numbers):
    complex_password += random.choice(numbers)
random.shuffle(complex_password)
for item in complex_password:
    complex_pass += item
print(f"complex_password is {complex_pass}")