import os
import glob2
import datetime

print(os.listdir())
print(glob2.glob("fi*.txt"))
file_list=glob2.glob("fi*.txt")

for i in file_list:
    with open(i,"r") as file:
        list2=file.read()
        with open("fle_mg.txt","a+") as file:
            file.write(list2+ "\n")
