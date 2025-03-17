import random 
import string

print("Aditya's Random Password Generator 2025")

def myPass():
    length = int(input("Enter length of Password: "))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    number = string.digits
    special = string.punctuation

    combine = lower + upper + number + special

    # always return new value
    x = random.sample(combine, length)

    # convert list to string
    password ="".join(x)
    
    print(password)
    
    myPass()            
myPass()
