# \\\\\print(filename1.name)
import os
list1=[]
for path1,subfolderlist1,filelist1 in os.walk(r"D:\zxl_PreciousPythonFiles\abstract"):
    for filename1 in os.scandir(path1):
        print(filename1.name)
        if filename1.is_file():
            filecontent1=open(filename1,"rb").read()
            if hash(filecontent1) in list1:
                os.remove(filename1)
            else:
                list1.append(hash(filecontent1))


