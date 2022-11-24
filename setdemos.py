mySet= {1, 2, 3}
mySet.add(4)
mySet.add("2")

print(len(mySet))
print(mySet)

mySet.remove(1)
print(mySet)

mySet.pop()
print(mySet)

mySet.clear()
print(mySet)

mySet.add(5)
mySet.add(4)
mySet.add(3)
mySet.add("3")
mySet.add(4)

print(mySet)

newSet=mySet.union({1,2})
print(newSet)

newSet=mySet.intersection({1,2,3,4})
print(newSet)