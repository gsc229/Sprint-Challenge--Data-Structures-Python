import time
from binary_search_tree import BinarySearchTree as BsT


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
duplicates_2 = []

print("========================FASTER====================================")

# convert names_1.txt to a bst

names_two = BsT(names_2[0])
print(f"HEAD {names_two.value}")

# Replace the nested for loops below with your improvements

for name in names_2:
    names_two.insert(name)

# print(names_one.in_order_print(names_one))

# runtime 2 n log n --> n log n
for name in names_1:
    if names_two.contains(name):
        duplicates_2.append(name)

end_time = time.time()
print(f"{len(duplicates_2)} duplicates:\n\n{', '.join(duplicates_2)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


print("========================SLOWER====================================")

for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# initial commit
