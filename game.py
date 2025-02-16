import random

# Print multiline instruction
print('To remind you, the rules of this game are:\n'
      + "Rock vs Paper -> Paper wins\n"
      + "Rock vs Scissors -> Rock wins\n"
      + "Paper vs Scissors -> Scissors wins\n")

while True:
    print("What is your choice?\n 1 - Rock \n 2 - Paper\n 3 - Scissors \n")

    choice = int(input("What is your choice? Enter the number please: "))

    # Loop until the user makes a valid input
    while choice > 3 or choice < 1:
        choice = int(input("Invalid choice. Please enter one of the numbers 1-3: "))

    # Initialize value of choice_name variable corresponding to the choice value
    if choice == 1:
        choice_name = "Rock"
        print("You chose Rock")
        print("Now it is the computer's turn!")
    elif choice == 2:
        choice_name = "Paper"
        print("You chose Paper")
        print("Now it is the computer's turn!")
    else:
        choice_name = "Scissors"
        print("You chose Scissors")
        print("Now it is the computer's turn!")

    # Generate random choice for computer
    computer_choice = random.randint(1, 3)

    # Initialize value of computer_choice_name variable corresponding to the computer's choice value
    if computer_choice == 1:
        computer_choice_name = "Rock"
        print("Computer chose Rock")
    elif computer_choice == 2:
        computer_choice_name = "Paper"
        print("Computer chose Paper")
    else:
        computer_choice_name = "Scissors"
        print("Computer chose Scissors")

    print(choice_name, 'vs', computer_choice_name)

    # Compare choices and declare the winner
    if choice == computer_choice:
        print("It's a tie!")
    elif (choice == 1 and computer_choice == 3) or (choice == 2 and computer_choice == 1) or (choice == 3 and computer_choice == 2):
        print("You win!")
    else:
        print("Computer wins!")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again != 'y':
        break

print("Thank you for playing!")
