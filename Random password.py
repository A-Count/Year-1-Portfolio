import random

while more == "1":
    new_pass = []
    old_pass = input("Enter your password")
    integer = False
    more = "1"

    for x in old_pass:
        if isinstance(i, int) == True:
            integer = True
        elif x == "a":
            choose = input("Choose 4 or @")
            if choose == "@":
                new_pass.append("@")
            else:
                new_pass.append("4")
        elif x == "i" or x == "l":
            choose = input("Choose 1 or !")
            if choose == "1":
                new_pass.append("1")
            else:
                new_pass.append("!")
        elif x == "s":
            new_pass.append("5")
        elif x == "e":
            new_pass.append("3")
        else:
            new_pass.append(x)


    if integer == False:
        new_pass.append(str(random.randrange(1,10)))
        new_pass.append(str(random.randrange(1,10)))

    new_pass.append(" ")

    print("Your new password is " + "".join(new_pass))

    f = open("PasswordsNew.txt", "a")
    f.write("".join(new_pass))
    f.close()

    f = open("PasswordsNew.txt", "r")
    print(f.read())
    f.close()

    more = input("Press 1 to enter another password")
