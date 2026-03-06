s = {23,4,23,45,78,89,56,100}
s1 = {100, 200, 300,1}

print(s)
s.add(100)
print(s)
s.remove(4)
print(s)

s.update({200, 300,988})
print(s)

print("Union of s and s1: ", s.union(s1))
print("Intersection of s and s1: ", s.intersection(s1))

for item in s: 
    print(item, end = ' ')