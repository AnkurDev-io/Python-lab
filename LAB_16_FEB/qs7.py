# Write a Python program to combine two dictionary by adding values for common keys. 
# d1 = {'a': 100, 'b': 200, 'c':300} 
# d2 = {'a': 300, 'b': 200, 'd':400} 
dict1 = {
    'a':100,
    'b':200,
    'c':300,
    'd':460
}

dict2= {
    'a':500,
    'b':100,
    'c':400
}

result = {}

## adding valus from dict1
for key in dict1:
    result[key] = dict1[key]

for key in dict2:
    if key in result:
        result[key]+=dict2[key]
    else:
        result[key] = dict2[key]

print(result)

