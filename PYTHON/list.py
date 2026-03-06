list = [100, 120, 23, 12 , 35, 56,78,90,90]

print("The original list is: ", list)

list.append(500)
list.remove(78) #take the object
print(list)
list.pop() #take index  - pop() remove last element
list.sort(reverse= True)
print("Before pop() ",list)
list.pop(3)
print("printing list using for loop")
for item in list:
    print(item, end = ' ')


print(list.count(90))
print(len(list))
print(len("Amrit"))
print()
print("printing index and element using enumerate")
for index,item in enumerate(list, 4):
    print(index, item)

print("The original list: ", list)
print("Sublist or slicing the list")
print(list[2:5])  # 1: inclusive - 2: exclusive
print(list[2:])
print(list[:5])
print(list[-3:]) # from last index
print(list[::-1]) # reverse the list
list.reverse()

print(list)