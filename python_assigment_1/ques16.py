# counts frequency of each char in string
dict1={}
str1=input("Enter the string: ")
for i in range(len(str1)):
    dict1[str1[i]]=str1.count(str1[i])
print("Frequency of each char in string: ",dict1)