# Create two sets of integers and perform:

# Union

# Intersection

# Difference

# Symmetric Difference

set1 = {1,2,4,5,6}
set2 = {3,4,5,7,9}
set1_union =set1.union(set2)
set1_intersection=set1.intersection(set2)
set1_difference=set1.difference(set2)
set2_symmetric=set2.symmetric_difference(set1)

print(set1_union)
print(set1_intersection)
print(set1_difference)
print(set2_symmetric)