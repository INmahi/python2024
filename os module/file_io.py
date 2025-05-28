import os

os.chdir("os module/Folder-1")
print(os.getcwd())

# f = open("Student_Data.txt","w")
# f.write("test")

# f = open("Student_Data.txt","r")
# print(f.read())
i = 0
with open("Student_Data.txt","r") as sheet:

    while True:
        i = i+1
        line  = sheet.readline()
        mark = line.split(",")
        if not line:
            break
        print(line.strip())
        print(f"Student {i} -> | Bangla = {mark[0]} | English = {mark[1]} | Math = {mark[2]}")    
        
