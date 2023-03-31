import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
answer = random.choice(colors)

print("Guess the color I'm thinking of!")
guess = ""

while guess != answer:
    guess = input("Enter a color guess: ")
    guess = guess.lower()
    
    if guess == answer:
        print("You got it! The color was", answer)
    elif guess not in colors:
        print("That's not a valid color. Try again.")
    elif colors.index(guess) > colors.index(answer):
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
