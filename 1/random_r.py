
import random

# Define the set of letters to choose from
letters = 'abcdefghijklmnopqrstuvwxyz'

# Split the password components into individual variables
digit = random.randint(0, 9)
letter1 = random.choice(letters)
letter2 = random.choice(letters)
number = random.randint(80, 99)
letter3 = random.choice(letters)

password = str(digit) + letter1 + letter2 + str(number) + letter3


print(password)



wybzd=random.randrange(1000, 2000,50)
print(f'{wybzd}')


low = int(input("Enter a low value: "))
high = int(input("Enter a high value: "))
total = random.randint(low, high)
print(total)
