#
#
# import os
# import datetime
# import shutil
# def findFlyer1(folder1,folder2):
#     for l,m,n in os.walk(folder1):#path
#         for i in os.scandir(l):
#             if ("附件2" in i.name) and ("Annex" in i.name)and i.name.endswith("pdf"):
#                 date1=datetime.datetime.fromtimestamp(i.stat().st_mtime)
#                 newfilename1=str(date1.year)+"_"+str(date1.month)+"_"+str(date1.day)+"_"+i.name
#                 shutil.copy(l+"/"+i.name,folder2+"/"+i.name)
# # \\\【【【step1】】】find out all the flyer (附件2， Annex， pdf)，input the folder path and the final folder path:
# # \\\findFlyer1(r"D:\2020_001_张岱老师筹办的神经精神障碍系列讲座",r"D:\用代码汇总psy\2020psy_pdf2docx")
# findFlyer1(r"D:\2021_+_张岱老师筹办的神经精神障碍系列讲座",r"D:\用代码汇总psy\2021_flyer")


#\\\【step2】：input one folder
import os
import shutil
from pdf2docx import Converter
def zxlpdf2docx(pdf_folder1):
# "This is an easy-go file wrote by Xiaolin Zhang from CIBR. You can convert pdf to docx freely ever after!"
    j = 0
    for l,m,n in os.walk(pdf_folder1):
        for i in os.scandir(l):
            cv = Converter(l+"/"+i.name)
            cv.convert(l+"/"+i.name.split(".")[0]+".docx", start=0, end=None)
            cv.close()
            j=j+1

    print(f'we have converted {j} files!')
# \\\【step2】：input one folder
zxlpdf2docx(r"D:\zzz用代码汇总psy\2020_2021_pdf2docx")