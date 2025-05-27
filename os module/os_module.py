import os



# for i in range(0,7):
#     os.rename(f"Folder {i}",f"Folder-{i+1}")

os.chdir("os module")

print(os.getcwd())

for i in range(0,7):
    os.chdir(f"Folder-{i+1}")
    with open(f"INFO_WRITE.md {i+1}","w") as fp:
        fp.write(f"Hello, you are inside Folder-{i+1}, and this is an automated content")
    os.chdir("..")
    



