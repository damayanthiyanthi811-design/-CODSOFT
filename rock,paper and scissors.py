import random
def display_welcome_message():
    print("\nwelcome to the Rock,paper,scissors Game!")
    print("Rules:")
    print(" - Rock beats scissors")
    print(" - scissors beats paper")
    print(" - paper beats Rock")
    print("Type 'quite' anytime to exit the game.\n")
def get_user_choice():
    while True:
        user_input=input("enter your choice(rock,paper,scissors):").lower()
        if user_input in ["rock","paper","scissors"]:
            return user_input
        elif user_input == "quit":
            return "quit"
        else:
            print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
def get_computer_choice():
    return random.choice(["rock","paper","scissors"])
def determine_winner(user,computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer =="scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"
def print_round_result(user,computer,winner):
    print("\n you chose:",user)
    print("computer chose:",computer)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("you win this round!")
    else:
        print("computer wins the round!")
def print_final_result(user_score,computer_score):
    print("\n---Final Result---")
    print("your score:",user_score)
    print("computer's score:",computer_score)
    if user_score > computer_score:
        print("you are the overall winner!")
    elif computer_score > user_score:
        print("The computer wins overall. Better luck next time!")
    else:
        print("It's a draw overall!")
def main():
    user_score=0
    computer_score=0


    display_welcome_message()

    while True:
        user_choice = get_user_choice()
        if user_choice =="quit":
            break

        computer_choice=get_computer_choice()
        winner= determine_winner(user_choice,computer_choice)
        print_round_result(user_choice,computer_choice,winner)
        if winner =="user":
            user_score+=1
        elif winner=="computer":
            computer_score+=1
        print(f"current score -> you:{user_score} | computer: {computer_score}\n")
    print_final_result(user_score,computer_score)
if __name__=="__main__":
    main()
