#reads data from 
import csv
file1=open("file.csv","r")
r_obj=csv.reader(file1)
for i in r_obj:
    print(i)