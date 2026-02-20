# Create a set and check whether it is a subset of another set.
set1 = {2,3,4,5,6,7,8}
set2 = {2,3,4}

if set2.issubset(set1): ## it checks wheather set 2 is subset of set1 or not
    print("set2 is subset of set1")
else:
    print("set 2 is not subset of set1")