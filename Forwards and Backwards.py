word = input("Enter a word")
letters = ([*word])
print(letters)
palindrome = []
num = 0
minus = -1
for x in letters:
    num = num + 1
for x in range(num):
    palindrome.append(letters[minus])
    print(palindrome)
    print(minus)
    minus = minus - 1
palindrome = "".join(palindrome)
if palindrome == word:
    print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")
