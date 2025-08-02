'''
1. Create an empty list named my_list
'''

my_list = []

'''
2. Append a number to the list: 10, 20, 30, 40
'''
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"Initial my_list: {my_list}")

'''
3. Insert the value 15 at the second position in the list.
'''
my_list.insert(1, 15)
print(f"my_list after inserting 15 at index 1: {my_list}")

'''
4. Extend my_list with another list: [50, 60, 70].
'''
my_list2 = [50, 60, 70]
my_list.extend(my_list2)
print(f"my_list after extending with my_list2: {my_list}")

'''
5. Remove the last element from my_list.
'''
my_list.pop()
print(f"my_list after removing the last element: {my_list}")

'''
6. Sort my_list in ascending order.
'''
my_list.sort()
print(f"my_list after sorting: {my_list}")

'''
7. Find and print the index of the value 30 in my_list.
'''
index_of_30 = my_list.index(30)
print(f"The index of 30 in my_list is: {index_of_30}")