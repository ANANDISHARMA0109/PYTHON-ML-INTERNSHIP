# removes all punctutations
str1=input("Enter the string: ")
str2=''
for i in range(len(str1)):
    if str1[i].isalnum()==True or str1[i]==' ':
        str2+=str1[i]
print("String without punctuations: ",str2)