num1 = int(input("Enter the number to check prime : "))

flag = False

if num1 == 1:
    print(num1, "not a prime number")
elif num1 > 1:
    for i in range(2, num1):
        if (num1 % i) == 0:
            flag = True
            break


if flag:
    print(num1, "Not a prime number")
else:
    print(num1, "is a prime number")
