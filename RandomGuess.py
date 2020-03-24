# This is a guess the number game
import random
print('Hello, what is your name?')
name = input()

print('Well, ' + name + ', I have a number between 1 and 20')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess was too low')
    elif guess > secretNumber:
        print('Your guess was too high')
    else:
        break # This condition is for the correct guess

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Actually, the number I was taking of was ' + str(secretNumber))
