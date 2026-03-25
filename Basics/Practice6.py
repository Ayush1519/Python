my_list = [1, 2, 3, 4, 4, 5]

print("Count:", len(my_list))
#-----------------------------------------------------------------------------------------------
mul = 1
for i in my_list:
    mul *= i
print(mul)
#-----------------------------------------------------------------------------------------------
temp_list = my_list.copy()
temp_list.remove(max(temp_list))
print("Second Largest:", max(temp_list))
#-----------------------------------------------------------------------------------------------
reverse_list = []
for i in my_list:
    reverse_list.insert(0, i)
print("Reversed List:", reverse_list)
#-----------------------------------------------------------------------------------------------
element = int(input("Enter element to check: "))
if element in my_list:
    print("Element is present.")
else:
    print("Element is not present.")
#-----------------------------------------------------------------------------------------------
element = int(input("Enter element to find frequency: "))
print("Frequency:", my_list.count(element))
#-----------------------------------------------------------------------------------------------
list_with_zeroes = [0, 1, 0, 3, 12]
non_zeroes = [x for x in list_with_zeroes if x != 0]
zeroes = [x for x in list_with_zeroes if x == 0]
print(non_zeroes + zeroes)
#-----------------------------------------------------------------------------------------------
shifted_list = my_list[-2:] + my_list[:-2]
print(shifted_list)
#-----------------------------------------------------------------------------------------------
missing_list = [1, 2, 3, 5, 6, 7, 8, 9, 10]
n = len(missing_list) + 1
total_sum = n * (n + 1) // 2
actual_sum = sum(missing_list)
missing_element = total_sum - actual_sum
print("Missing element:", missing_element)
