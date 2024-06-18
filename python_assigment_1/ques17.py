# convert string to title
str1=input("Enter the string: ")
str2=''
str2+=str1[0].upper()
i=1
while i<len(str1):
    if str1[i]==' ' and i+1<len(str1):
        str2+=' '+str1[i+1].upper()
        i+=1
    else:
        str2+=str1[i]
    i+=1
print("Title:",str2)