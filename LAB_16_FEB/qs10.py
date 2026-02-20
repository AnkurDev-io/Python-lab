## Remove an item from the tupple

t = (10, 20, 30, 40, 50)

temp = list(t)
temp.remove(30)

t = tuple(temp)

print("Updated tuple:", t)