import random

# initializing the pseudorandom number generator
random.seed()

print("Password Generator")
password_length = int(input("How many characters would you like your password to be? "))
password = ''
counter = 0

while counter < password_length:
    random_char = chr(random.randrange(48, 123))
    password += random_char
    counter += 1
print(password)