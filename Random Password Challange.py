import random
letters = 'abcdefghijklmnopqrstuvwxyz'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

numbers = '0123456789'

num_letters = int(input("How many lowercase letters would you like in your password?"))
num_upper = int(input("How many uppercase letters would you like?"))
num_numbers = int(input("How many numbers would you like?"))
# Create a list to hold password characters

password_list = []

for _ in range(num_letters):
    password_list.append(random.choice(letters))

for _ in range(num_upper):
    password_list.append(random.choice(upper_letters))

for _ in range(num_numbers):
    password_list.append(random.choice(numbers))


random.shuffle(password_list)
password = "".join(password_list)

print(f"Your random password is: {password}")