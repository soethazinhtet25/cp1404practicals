"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    """Get scores and display the results. """
    score = float(input("Enter score: "))
    result = determine_score_status(score)
    print(f"User score {score} is {result}")

    if result == "Excellent":
        print("You get a prize!")

    random_score = random.randint(1, 100)
    print(f"Random: {random_score} = {determine_score_status(random_score)}")

def determine_score_status(score):
    """Determine the score status based on the score given."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()

