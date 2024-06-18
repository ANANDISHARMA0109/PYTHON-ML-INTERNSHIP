# check prefix or suffix
str1=input("Enter the string: ")
pf=input("Enter the prefix: ")
sf=input("Enter the suffix: ")
l1=len(pf)
l2=len(sf)
if str1[:l1]==pf and str1[-l2:]==sf:
    print("The string contains the given prefix as well as the given suffix")
elif str1[:l1]==pf:
    print("The string contains the given prefix")
elif str1[-l2:]==sf:
    print("The string contains the given suffix")
else:
    print("The string does not contain the given prefix or suffix")
