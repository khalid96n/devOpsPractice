dict1 = {
    "firstname": "ravi",
    "lastname": "kr",
    "salary": 5000,
    "role": "developer"
}

print(dict1)

x = dict1.keys()
y = dict1.values()

print(x)
print(y)

print(dict1["lastname"])

dict1["lastname"] = "singh"
print(dict1)

z = dict1.items()

print(z)

dict1.clear()
print(dict1)

dict1["brand"] = "ford"
dict1["price"] = 40000
dict1["model"] = "f15"
print(dict1)

dict1.pop("price")
print(dict1)

# del (dict1)
# print(dict1)
