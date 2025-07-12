import random

# --- Color Settings ---
R = "\033[31m"  # Red
G = "\033[32m"  # Green
Y = "\033[33m"  # Yellow
B = "\033[34m"  # Blue
C = "\033[36m"  # Cyan
W = "\033[37m"  # White
RESET = "\033[0m" # Resets all formatting

# --- Game Rules & Constants ---
# Storing game choices and the logic for winning.
GAME_CHOICES = ["ROCK", "PAPER", "SCISSORS"]
WIN_LOGIC = {
    ("ROCK", "SCISSORS"): "win",
    ("PAPER", "ROCK"): "win",
    ("SCISSORS", "PAPER"): "win",
}

# --- Game Dialogue & Messages ---
# All messages displayed during the game are stored here for clarity.
MESSAGES = {
    "intro": f"{C}>>> Welcome to the Arena: Rock, Paper, Scissors! <<<{RESET}",
    "prompt_rounds": f"{Y}How many points are needed to win? {RESET}",
    "prompt_choice": f"{C}Enter your move ({'/'.join(GAME_CHOICES)}) or 'Q' to quit: {RESET}",
    "invalid_round": f"{R}Invalid input! Please enter a number greater than 0.{RESET}",
    "invalid_choice": f"{R}Not a valid move. Please choose from {', '.join(GAME_CHOICES)}.{RESET}",
    "tie": f"{Y}This round is a tie!{RESET}",
    "win": f"{G}You won this round!{RESET}",
    "lose": f"{R}The computer won this round!{RESET}",
    "player_reveals": f"You played: {B}",
    "computer_reveals": f"Computer played: {R}",
    "final_score": f"{W}--- FINAL SCOREBOARD ---{RESET}",
    "player_won_game": f"{G}VICTORY! You are the undisputed champion!{RESET}",
    "computer_won_game": f"{R}DEFEAT! The computer is the champion this time.{RESET}",
    "game_quit": f"{Y}Game has been stopped. See you next time!{RESET}",
    "thanks": f"{C}Thanks for playing!{RESET}"
}

# ___ Core Game Functions ___

def get_valid_int_input(prompt):
    # Gets a valid positive integer input from the user.
    while True:
        try:
            target = int(input(prompt).strip())
            if target > 0:
                return target
            print(MESSAGES["invalid_round"])
        except ValueError:
            print(MESSAGES["invalid_round"])

def get_player_move(valid_moves):
    # Prompts the player for their move and validates it.
    while True:
        player_choice = input(MESSAGES["prompt_choice"]).strip().upper()
        if player_choice == 'Q' or player_choice in valid_moves:
            return player_choice
        print(MESSAGES["invalid_choice"])

def determine_round_result(player_action, computer_action):
    # Determines the winner of the current round based on WIN_LOGIC.
    if player_action == computer_action:
        return "tie"
    if (player_action, computer_action) in WIN_LOGIC:
        return "win"
    # If it's not a tie and not a player win, it must be a loss.
    return "lose"

def display_scores(player_points, computer_points, winning_score):
    # Displays the current scores on the screen.
    print(f"{W}SCORE:{RESET} Player {G}{player_points}{RESET} | Computer {R}{computer_points}{RESET} (Target: {winning_score})")

# *** Main Game Loop ***

def play_game():
    # This function controls the main game flow from start to finish.
    print(MESSAGES["intro"])

    player_score = 0
    computer_score = 0
    target_score = get_valid_int_input(MESSAGES["prompt_rounds"])

    while player_score < target_score and computer_score < target_score:
        display_scores(player_score, computer_score, target_score)

        player_move = get_player_move(GAME_CHOICES)
        if player_move == 'Q':
            break

        computer_move = random.choice(GAME_CHOICES)

        print(f"{MESSAGES['player_reveals']}{player_move}{RESET}")
        print(f"{MESSAGES['computer_reveals']}{computer_move}{RESET}")

        outcome = determine_round_result(player_move, computer_move)
        print(MESSAGES[outcome]) # Prints the result message, e.g., "You won this round!"

        if outcome == "win":
            player_score += 1
        elif outcome == "lose":
            computer_score += 1
        
        print("~" * 40) # Round separator

    # *** End of Game Summary ***
    print(f"\n{MESSAGES['final_score']}")
    display_scores(player_score, computer_score, target_score)

    if player_score >= target_score:
        print(MESSAGES["player_won_game"])
    elif computer_score >= target_score:
        print(MESSAGES["computer_won_game"])
    else: # This block runs if the loop was broken by 'Q'
        print(MESSAGES["game_quit"])

    print(MESSAGES["thanks"])

# *** Run the Game ***
if __name__ == '__main__':
    play_game()