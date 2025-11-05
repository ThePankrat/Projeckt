import random

#Generate a random secret code between 1 and 10
secret_code = random.randint(1, 10)

# Welcome message
print("🎮 Welcome to the Code Guessing Game!🎮")
print("I'm thinking of a number between 1 and 10. You have 3 attempts to guess it!")

for attempt in range(1, 4):
    guess = int(input(f"Attempt {attempt}: Think Harder : "))

    if guess == secret_code:
        print("✅ Correct! You guessed the code! 🏆🏆🏆")
        break
    elif guess < secret_code:
        print("📉 Too low!")
    else:
        print("📈 Too high!")
# out of attempt
else:
    print("💀 💀 💀 GAME OVER ! Out of attempts. The correct code was:", secret_code)