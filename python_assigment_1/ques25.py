# copies content of another text file
file1=open("C:/Users/Dell/Desktop/PYTHON ML INTERNSHIP/demo.txt","r")
file2=open("C:/Users/Dell/Desktop/PYTHON ML INTERNSHIP/demo2.txt","w")
lst=file1.readlines()
file2.writelines(lst)
file1.close()
file2.close()