def menu_():#Menu systems for repeated use
    global menu
    menu = input("""Press 1 to enter member
Press 2 to read members
Press 3 to search members
Press 4 to exit""")

menu_()
while int(menu) != 4:
    
    if int(menu) == 1:#Entering membership details
        member = []
        name = input("Enter name of member")
        age = input("Enter age of member")
        gender = input("Enter gender of member")
        card = input("Loyalty Card? Y/N")
        print("Name = " + name)#Repeating details and checking them with user
        print("Age = " + age)
        print("Gender = " + gender)
        print("Card = " + card)
        log = int(input("Press 1 if this information is correct?"))
        if int(log) == 1:#Storing details in file
            member.append(name)
            member.append(age)
            member.append(gender)
            member.append(card)
            f = open("RockClimbing.txt","a")
            f.write(str(member))
            f.close()
        menu_()
    if int(menu) == 2:#Reading all membership details
        f = open("RockClimbing.txt","r")
        print(f.readline())
        f.close()
        menu_()
    if int(menu) == 3:#Searching for memberships
        f = open("RockClimbing.txt","r")
        
