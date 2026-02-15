## Count the number of occurance in the tupple

tupple = (1,3,4,5,4,1,3)
checked = []
for i in tupple:
    if i not in checked:
     counter= tupple.count(i)
     print(f"{i} occurs {counter} times")
     checked.append(i)