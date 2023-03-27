digit1 = input("Enter first digit")
digit2 = input("Enter second digit")
digit3 = input("Enter third digit")
digit4 = input("Enter fourth digit")

sequence = input("Enter correct sequence")

check = [digit1,digit2,digit3,digit4]

while "".join(check) != sequence:
    print(check)
    check = [digit1,digit3,digit2,digit4]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit1,digit3,digit4,digit2]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit1,digit2,digit4,digit3]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit1,digit4,digit2,digit3]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit1,digit4,digit3,digit2]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit2,digit1,digit3,digit4]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit2,digit1,digit4,digit3]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit2,digit3,digit1,digit4]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit2,digit3,digit4,digit1]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit2,digit4,digit1,digit3]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit2,digit4,digit3,digit1]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit3,digit1,digit2,digit4]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit3,digit1,digit4,digit2]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit3,digit2,digit1,digit4]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit3,digit2,digit4,digit1]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit3,digit4,digit1,digit2]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit3,digit4,digit2,digit1]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit4,digit1,digit2,digit3]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit4,digit1,digit3,digit2]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit4,digit2,digit1,digit3]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit4,digit2,digit3,digit1]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit4,digit3,digit1,digit2]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
    print(check)
    check = [digit4,digit3,digit2,digit1]
    if "".join(check) == sequence:
        print("".join(check) + " is the correct sequence")
        break
