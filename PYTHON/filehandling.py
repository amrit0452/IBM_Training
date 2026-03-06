with open('data.txt', 'r') as file:
    content = file.read()
    print(content)


# writing
with open('output.txt', 'w') as file:
    file.write("Hellow, file!")

#with will automatically close the open resources/file