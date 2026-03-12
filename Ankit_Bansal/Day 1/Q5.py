#write a program which takes the name of the user as input and print the index of character 'a' in the string. if 'a' is not there then return -1.


# Taking input from the user
name = input("Enter your name: ")

# Finding the index of 'a'
index = name.find('a')

# Printing the result
print("Index of 'a':", index)
