"""
CP1404/CP5632 - Practical

Score menu program
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars 
(Q)uit"""

def main():
    """Score menu program."""
    score = get_valid_score()
    print(MENU)
    choice = input("Enter your choice: ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_status(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")

        print(MENU)
        choice = input("Enter your choice: ").upper()

    print("Farewell")

def get_valid_score():
    """Determine the score is valid."""
    score = float(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter your score: "))
    return score

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

def show_stars(score):
    """Show stars based on the score given."""
    print("*" * int(score))


main()
