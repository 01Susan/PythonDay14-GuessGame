from art import logo, vs
import random
from game import data
import os

# Printing the raw data in printable format
def print_account(account):
    account_name = account["name"]
    account_des = account["description"]
    account_country = account["country"]
    formated = f"{account_name}, a {account_des}, from {account_country}"
    return formated


def check_answer(user_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return user_guess == "A"
    else:
        return user_guess == "B"


print(logo)
score = 0
account_b = random.choice(data)
# Generating the random account from the game.py
while score >= 0:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {print_account(account_a)}")
    print(vs)
    print(f"Against B: {print_account(account_b)}")

    # Asking the user for the guess
    user_guess = input("Who has more folloers? Type 'A' or 'B': ").upper()

    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]

    is_correct = check_answer(
        user_guess=user_guess, a_follower=a_follower, b_follower=b_follower
    )
    os.system("cls")
    if is_correct:
        print(logo)
        score += 1
        print(f"You're right!, current score: {score}")
    else:
        final_score = score
        score = -1
        print(f"You're wrong, Final score: {final_score}")
