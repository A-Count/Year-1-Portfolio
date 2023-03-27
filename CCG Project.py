import random
user_score = 0
comp_score = 0

def user_choice():
    global user_colour
    menu = int(input("""Choose from:
Yellow - 1
Red - 2
Blue - 3
Green - 4
Purple - 5
"""))
    while menu < 1 or menu > 5:
        menu = int(input("Enter a valid number"))
    if menu == 1:
        user_colour = "Yellow"
    elif menu == 2:
        user_colour = "Red"
    elif menu == 3:
        user_colour = "Blue"
    elif menu == 4:
        user_colour = "Green"
    elif menu == 5:
        user_colour = "Purple"
    
def comp_choice():
    global comp_colour
    x = random.randint(1,5)
    if x == 1:
        comp_colour = "Yellow"
    elif x == 2:
        comp_colour = "Red"
    elif x == 3:
        comp_colour = "Blue"
    elif x == 4:
        comp_colour = "Green"
    elif x == 5:
        comp_colour = "Purple"

def start_func():
    global current_round
    global start
    global user_score
    global comp_score
    current_round = 0
    user_score = 0
    comp_score = 0

    start = int(input("""Welcome to the Colour Choice Game!
Press 1 for player start (Easy),
Press 2 for computer start (Hard),
Press 3 to exit
"""))
    
start_func()
while start != 3:
    if start > 3 or start < 1:
        print("Please enter a valid number")
        start_func()
    else:
        rounds = int(input("How many rounds do you want?"))
        while current_round < rounds:
            if start == 1:
                user_choice()
                comp_choice()
                if comp_colour == user_colour:
                    comp_score = comp_score + 1
                else:
                    user_score = user_score + 1
                print("You chose " + user_colour + " and the computer chose " + comp_colour)
                print("Your Score:" + str(user_score))
                print("Computer Score:" + str(comp_score))
                current_round = current_round + 1
            elif start == 2:
                comp_choice()
                user_choice()
                if user_colour == comp_colour:
                    user_score = user_score + 1
                else:
                    comp_score = comp_score + 1
                print("You chose " + user_colour + " and the computer chose " + comp_colour)
                print("Your Score:" + str(user_score))
                print("Computer Score:" + str(comp_score))
                current_round = current_round + 1
        if user_score > comp_score:
            print("""You Win!
Play Again?
""")
            start_func()
        elif user_score < comp_score:
            print("""You lose
Play Again?""")
            start_func()
        elif user_score == comp_score:
            print("""You Tied
Play Again?""")
            start_func()
        
