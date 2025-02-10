import random 

# Available choices
char = ["rock", "paper", "scissor"]

print("\n🎮 WELCOME TO ROCK PAPER SCISSORS GAME 🎮\n")

# Get number of rounds
while True:
    try:
        winning_score = int(input("Enter how many rounds you want to play:\n"))
        if winning_score > 0:
            break
        else:
            print("❌ Please enter a positive number.")
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")

# Initialize scores
com_score = 0
play_score = 0

# Game loop
for _ in range(winning_score):
    while True:
        player = input("\nChoose Rock, Paper, or Scissor:\n").strip().lower()
        if player in char:
            break
        else:
            print("❌ Invalid choice! Please choose Rock, Paper, or Scissor.")

    # Computer makes a random choice
    computer = random.choice(char)
    print(f"🤖 Computer chose: {computer}")

    # Game logic
    if player == computer:
        print("⚖️ It's a Draw!")
    elif (player == "rock" and computer == "scissor") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissor" and computer == "paper"):
        print("🎉 You Win!")
        play_score += 1
    else:
        print("💻 Computer Wins!")
        com_score += 1

    # Display scores
    print(f"\n🏆 Your Score: {play_score} | 🤖 Computer Score: {com_score}")

# Final Result
print("\n🎯 Final Result:")
if play_score > com_score:
    print("🎉 You have WON the game! 🏅")
elif play_score < com_score:
    print("💻 Computer has WON the game! 🏆")
else:
    print("⚖️ The game is a DRAW!")

print("\n-------------- GAME OVER --------------")
