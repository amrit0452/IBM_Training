# Tuple

t = (12,34,45,89,56,67,33)
print(t)

print(t[2:5])
print(t[2:])
print(t[:5])
print(t[-3:])
print(t[:-3])


# Dictionary

d = {"name": "Amrit", "age": 25, "city":  "New York"}
print(d["age"])
print(d.get("name"))
d["age"] = 23
print(d)

d["country"] = "INDIA"
print(d)

for key in d: 
    print(key, d[key])

for key, value in d.items():
    print(key, value)

print(list(d.keys()))
print(list(d.values()))

print()
print("enumerate")
for index, key in enumerate(d):
    print(index, key, d[key])

print()
print("zip")
for i in list(zip(d.keys(), d.values())):
    print(i)