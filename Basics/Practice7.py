tuple = (1, 2, 2, 3, 4, 5)

print("Maximun:", max(tuple))
print("Minimum:", min(tuple))

n=int(input("Enter n:"))
a= tuple.count(n)
print(a)

list = [1, 2, 3, 4, 5]       
tuple2 = tuple(list)
print(tuple2)

tuple3=(1, 2, 3, 4, 5)
list2 = list(tuple3)
print(list2)

tuple4 = (1, 2, 3, 4, 5)
n=int(input("Enter n: "))

if n in tuple4:
    print("Present")
else:
    print("Not present")

tuple5 = ("Ayush", 10, 2006)
Name, marks, year = tuple5
print(Name)
print(marks)  
print(year)

tuple6 = (1, 2, 3, 4, 5)
a, b, c, d, e = tuple6
print(e, d, c, b, a)

tuple7 = input("Enter tuple values (comma-separated): ")
tuple7 = tuple(map(int, tuple7.split(',')))
reverse_tuple = tuple7[::-1]
print(reverse_tuple)

tuple8 = (1, 2, 3, 4, 5)
a, b, c, d, e = tuple8
print("Before swapping:")
print(a)
print(b)
temp = a
a=b
b=temp
print("After swapping:")
print(a)
print(b)
