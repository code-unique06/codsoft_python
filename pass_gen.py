import random
import string

combo = string.ascii_letters + string.digits + string.punctuation

def generate_password(len):
    password = ''.join(random.choice(combo) for _ in range(len))
    return password


len = int(input("Enter the desired password length: "))

if len == 1:
    print("Week passoword generated due to less length")
    password = generate_password(len)
    print("Generated Password:",password)

elif len == 2:
    print("Week password generated due to less length")
    password = generate_password(len)
    print("Generated Password:",password)

elif len == 3:
    print("Moderate strength password generated")
    password = generate_password(len)
    print("Generated Password:",password)

else:
    print("Strong password generated")
    password = generate_password(len)
    print("Generated Password:",password)