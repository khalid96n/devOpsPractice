
n = int(input("enter the no of elements to be inserted in list : "))

l = []


for i in range(1, n):
    l.append(i)

print(l)

evenNum = list(filter(lambda x: x % 2 == 0, l))
oddNum = list(filter(lambda x: x % 2 != 0, l))
print(evenNum)
print(oddNum)


squared = list(map(lambda x: x**2, l))
print(squared)
