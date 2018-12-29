import random
import string

print("*" * 5 + "Welcome To Password Picker" + "*" * 5)

while True:
    adjectives = ['sleepy', 'funky', 'tired', 'wow', 'purple', 'crazy', 'proud']
    nouns = ['apple', 'table', 'goat', 'car', 'stuff']

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0,100)
    special_char = random.choice(string.punctuation)
                    
    password = adjective + noun + str(number) + special_char
                    
    print(f"Your new password is: {password}")
    
    user = input("Would you like to see a password? \n Y/N \n").lower()
    if user == "n":
        break



