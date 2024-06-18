# check if 2 strings are anangrams
str1=input("Enter first string: ")
str2=input("Enter second string: ")
dict1={}
dict2={}
if len(str1)==len(str2):
    for i in range(len(str1)):
        dict1[str1[i]]=str1.count(str1[i])
        dict2[str2[i]]=str2.count(str2[i])
    if dict1==dict2:
        print("The given strings are anagrams of each other")
    else:
        print("The given strings are not anagrams")
else:
    print("The given strings are not anagrams")