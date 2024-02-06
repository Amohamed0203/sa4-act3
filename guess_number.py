number = '10'

print("I'm thinking of a number...")
guess = str(input("What number am I thinking of? "))

while guess != number and guess != 'q':
    if int(guess) > int(number):
        print("Try lower. I'm thinking of a number...")
        guess = str(input("What number am I thinking of? ")) 
    else:
        print("Try higher. I'm thinking of a number...")
        guess = str(input("What number am I thinking of? ")) 

if guess == 'q':
    print(f"Sorry! The number was {number}.")   
elif guess == number:
    print("Congratulations! You guessed the right number.")
