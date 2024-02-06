number = '10'
cap = 9

print("10 tries. I'm thinking of a number...")
guess = str(input("What number am I thinking of? "))

while guess != number and guess != 'q' and cap != 0:
    if int(guess) > int(number):
        print(f"{cap} more tries. Try lower. I'm thinking of a number...")
        guess = str(input("What number am I thinking of? "))
        cap -= 1
    else:
        print(f"{cap} more tries. Try higher. I'm thinking of a number...")
        guess = str(input("What number am I thinking of? ")) 
        cap -= 1

if cap == 0:
    print(f"Sorry! The number was {number}.")  
if guess == 'q':
    print(f"Sorry! The number was {number}.")   
elif guess == number:
    print("Congratulations! You guessed the right number.")
