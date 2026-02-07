import random

print('welcome to the dice rolling game!')
while True:
    choice = input("press 'enter' to roll the dice or 'q' to quit) ")
    if choice == 'q':
        print('thanks for playing!')
        break
    elif choice=='':
        number = random.randint(1, 6)
        print(f'you rolled a {number}')
    else:
        print("invalid input, please try again.")

