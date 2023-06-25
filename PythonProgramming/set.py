set1 = {1, 2, 3, 9, 4, 5}
set2 = {2, 7, 8, 9}

set3 = set1.union(set2)
print(set3)

set4 = set1.intersection(set2)
print(set4)


fruit1 = {"Apple", "Banana", "Cherry"}
fruit2 = {"Mango", "Blueberry", "kiwi"}

# newfruit = fruit1+fruit2

fruit1.update(fruit2)

print(fruit1)
print(fruit2)
# print(newfruit)
