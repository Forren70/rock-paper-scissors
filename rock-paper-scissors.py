# Rock, Paper, Scissors Game Program
# The user can choose between Paper (P), Scissors (S), and Rock (R)
# Paper beats Rock, Rock beats Scissors, Scissors beat Paper
# Compares user choice and computer choice
# Prints updated score and asks the user if they want to play again

import random

# Global variables
rounds_played = 0
user_score = 0
pc_score = 0


def welcome():
    """Asks the user for their name and shows a welcome message."""
    user_name = input("\nHi, please enter your name: ").strip()
    print(f"\nOk, {user_name.capitalize()}. Let's play Rock, Paper, Scissors. Do you know the rules?")
    
    user_response = input("\nAnswer Yes or No: ").lower()
    if user_response not in ("yes", "y", "yeah", "yep", "sì", "si", "s"):
        print(
            "\nHere are the rules: choose between Rock, Paper, and Scissors, then we compare with my choice."
            "\nPaper beats Rock, Rock beats Scissors, Scissors beat Paper."
        )
    
    return user_name


def get_pc_move():
    """Randomly generates the computer's move."""
    possible_moves = ["Paper", "Scissors", "Rock"]
    return random.choice(possible_moves)


def compare_moves(pc_move, user_name, user_choice, user_score, pc_score, rounds_played):
    """Compares user and computer choices and updates scores and round count."""
    
    rounds_played += 1
    user_name = user_name.capitalize()  # Capitalize first letter

    if user_choice == "S": # Scissors
        if pc_move == "Scissors":
            print(f"\nIt's a Tie! We both chose Scissors.")
        elif pc_move == "Paper":
            user_score += 1
            print(f"\nYou won, {user_name}! I chose Paper and you chose Scissors!")
        else:  # Rock
            pc_score += 1
            print(f"\nYou lost, {user_name}! I chose Rock and you chose Scissors!")
    
    elif user_choice == "P": # Paper
        if pc_move == "Paper":
            print(f"\nIt's a Tie! We both chose Paper.")
        elif pc_move == "Rock":
            user_score += 1
            print(f"\nYou won, {user_name}! I chose Rock and you chose Paper!")
        else:  # Scissors
            pc_score += 1
            print(f"\nYou lost, {user_name}! I chose Scissors and you chose Paper!")
    
    elif user_choice == "R": # Rock
        if pc_move == "Rock":
            print(f"\nIt's a Tie! We both chose Rock.")
        elif pc_move == "Scissors":
            user_score += 1
            print(f"\nYou won, {user_name}! I chose Scissors and you chose Rock!")
        else:  # Paper
            pc_score += 1
            print(f"\nYou lost, {user_name}! I chose Paper and you chose Rock!")

    print(f"\nUser Score: {user_score} - Computer Score: {pc_score}")

    return user_score, pc_score, rounds_played



def print_final_result(user_name, user_score, pc_score):
    """Prints the final result of the game."""
    if user_score > pc_score:
        print(f"\nCongratulations {user_name}! You won the game with {user_score} points against my {pc_score}!")
    elif user_score == pc_score:
        print(f"\nIt's a draw, {user_name}! We both scored {user_score} points!")
    else:
        print(f"\nI'm sorry {user_name}! You lost the game with {user_score} points against my {pc_score}!")


# --- MAIN PROGRAM ---

player_name = welcome()

while rounds_played < 10:
    user_choice = input("\nMake your choice - P for Paper, S for Scissors, and R for Rock: ").strip().upper()
    
    # Valid input check
    if user_choice not in ("P", "S", "R"):
        print("Invalid choice! Please try again.")
        continue

    pc_move = get_pc_move()  # Computer move for this round

    user_score, pc_score, rounds_played = compare_moves(
        pc_move, player_name, user_choice, user_score, pc_score, rounds_played
    )

    print(f"\nRounds played: {rounds_played}")

# Final result printout
print_final_result(player_name, user_score, pc_score)

print("\nThanks for playing! See you next time!")
            

    

