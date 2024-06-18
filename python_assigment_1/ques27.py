# convert string to list of characters
str1=input("Enter the string: ")
lst1=[]
for i in range(len(str1)):
    lst1.append(str1[i])
print("List of characters:",lst1)