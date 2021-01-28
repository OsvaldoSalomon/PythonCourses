import random


def welcome():
    '''This function creates the welcome page for the gaming application.'''
    for i in range(0, 20):
        print("*\t", end="")
    print()
    print("*", end="")
    for i in range(0, 19):
        print("\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 19):
        print("\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 8):
        print("\t", end="")
    print("WELCOME", end="")
    for i in range(0, 10):
        print("\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 19):
        print("\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 19):
        print("\t", end="")
    print("*")
    for i in range(0, 20):
        print("*\t", end="")
    print()

    input("Press any key to start: ")


def mainmenu():
    '''This function creates the main menu for the gaming application.'''
    print("1. Rock Paper Scissors\n2. Cows and Bulls\n3. Exit")
    choice = int(input("Enter your choice number: "))
    if choice == 1:
        rockPaperScissorsMenu()
    elif choice == 2:
        cowsAndBullsMenu()
    elif choice == 3:
        exit()
    else:
        print("Invalid choice!")
        mainmenu()


def rockPaperScissorsMenu():
    '''This function creates the rock paper scissors menu for the gaming application.'''
    print("1. Play\n2. Rules\n3. Return to Main menu")
    choice = int(input("Enter your choice number: "))
    if choice == 1:
        rockPaperScissors()
    elif choice == 2:
        rockPaperScissorsRules()
    elif choice == 3:
        mainmenu()
    else:
        print("Invalid choice!")
        rockPaperScissorsMenu()


def cowsAndBullsMenu():
    '''This function creates the cows and bulls menu for the gaming application.'''
    print("1. Play\n2. Rules\n3. Return to Main menu")
    choice = int(input("Enter your choice number: "))
    if choice == 1:
        cowsAndBulls()
    elif choice == 2:
        cowsAndBullsRules()
    elif choice == 3:
        mainmenu()
    else:
        print("Invalid choice!")
        cowsAndBullsMenu()


def rockPaperScissors():
    '''This function creates the rock paper scissors game for the gaming application.'''
    print("Welcome to Rock Paper Scissors")
    print(
        "You will be competing against the computer. The player that scores 5 points first will be declared the winner.")
    print("If your choice is rock, please enter 0")
    print("If your choice is paper, please enter 1")
    print("If your choice is scissors, please enter 2")
    print("If you wish to exit, please enter -1")
    user = 0
    computer = 0
    cnt = 0
    choices = ["Rock", "Paper", "Scissors"]
    while (user < 5 and computer < 5 and cnt < 25):
        cnt += 1
        userChoice = int(input("Enter you choice:"))
        if userChoice == -1:
            print("Thank you")
            return
        computerChoice = random.choice([0, 1, 2])
        if userChoice == 0 and computerChoice == 1:
            computer += 1
        elif userChoice == 0 and computerChoice == 2:
            user += 1
        elif userChoice == 1 and computerChoice == 0:
            user += 1
        elif userChoice == 1 and computerChoice == 2:
            computer += 1
        elif userChoice == 2 and computerChoice == 0:
            computer += 1
        elif userChoice == 2 and computerChoice == 1:
            user += 1
        print("You:", choices[userChoice])
        print("Computer:", choices[computerChoice])
        print("Your score:", user, "\t Computer's Score:", computer)
    if (user > computer):
        print("Congratulations! You win!")
    elif (computer > user):
        print("Oops! Sorry you lose. Better luck next time!")
    else:
        print("Match Draw")
    mainmenu()


def cowsAndBulls():
    words = ["rate", "fail", "cake", "sore", "tear", "calm", "rage", "time", "face", "swan"]
    rand = random.randrange(0, 10)
    word = words[rand]
    cnt = 0
    while (cnt < 15):
        s = input("Enter string: ")
        if s == "-1":
            print("Thank you!")
            return
        cows = 0
        bulls = 0
        # seal calm
        chars = 0
        for c in s:
            if c in word:
                chars += 1
        for i in range(0, 4):
            if s[i] == word[i]:
                bulls += 1
        cows = chars - bulls
        print("Cows:", cows, "\tBulls:", bulls)
        if bulls == 4:
            print("Congratulations! You win!")
            mainmenu()
        cnt += 1
    print("Oops! Maximum guess limit reached!")
    mainmenu()


welcome()
print("\n" * 100)
mainmenu()
