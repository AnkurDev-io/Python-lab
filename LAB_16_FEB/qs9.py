## Write a python code to check repeated numbers

t = (10, 20, 30, 10, 40, 20, 50)

repeated = []

for item in t:
    if t.count(item) > 1 and item not in repeated:
        repeated.append(item)

print("Repeated items:", repeated)