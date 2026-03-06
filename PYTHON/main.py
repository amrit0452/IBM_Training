print("Hello, World!")
name = input("What is your name? ")
print("My name is", name)


# input("Enter number") -> this will take string input
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print("The sum of a and b is: " + str(a+b))

if a > b: 
    print("a is greater than b ")
elif a< b: 
    print("a c less than b")
else:
    print("a is equal to b")


for i in range(5):
    print(i, end = ' ')

print()
print("while loop")
count = 0 
while count < 10 : 
    print(count, end = ' ')
    count += 1