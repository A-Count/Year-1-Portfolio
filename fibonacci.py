start = 1
fib = [0,1]
length = int(input("How many places?"))
for x in range(length - 2):
    new = fib[-1] + fib[-2]
    fib.append(new)
    print(fib)

reverse = []
z = -1
total = 0
for x in range(len(fib)):
    total = total + fib[z]
    reverse.append(fib[z])
    z = z -1
    print(reverse)

print("The total value is " + str(total))
