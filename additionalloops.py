fruits = ["apple", "mango", "orange", "banana", "grapes"]

for i, items in enumerate(fruits):
    print(f"{i+1}. items")



list = [1, 2, 3, 4, 5, 6]
list2 = [i*i for i in list]
print(list2)

list2 = [i*i for i in list if i>3]
print(list2)
