a ={1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a|b)


c=len(a)
print(c)

my_dict = {
    "name": "Ayush",
    "age": 20,
    "city": "Delhi"
}

for key in my_dict.keys():
    print(key)


key1 = input("Enter key: ")
if key1 in my_dict:
    print("Exists")
else:
    print("Not exist")


for key in my_dict.keys():
    print(key)
    
for value in my_dict.values():
    print(value)



d= [1, 2, 3, 4, 5]
e= [4, 5, 6, 7, 8]  
uniqueElements = set(d)|set(e)
print(uniqueElements)


logs= ["u1", "u2", "u3", "u1", "u2", "u5"]
uniqueUsers = set(logs)
print(uniqueUsers)


Inventory = {"Mango": 10, "Banana": 4, "Grapes": 0}

for item, quantity in Inventory.items():
    if quantity == 0:
        print(item, "-> Out of stock")
    elif quantity < 5:
        print(item, "-> Less stock")
    else:
        print(item, "-> In stock")


user1 = {'A', 'B', 'C', 'D', 'E'}
user2 = {'D', 'E', 'F', 'G', 'H'}
mutual_users = user1 & user2

s = user2 - user1

print("Mutual users:", mutual_users)
print("Suggested users for user1:", s)
