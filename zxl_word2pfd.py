#\\\\\\\\\用docx2pdf把docx转为pdf
# print("start")
# from docx2pdf import convert
# import os
# def zxldocx2pdf(docx_folder1):
# # "This is an easy-go file wrote by Xiaolin Zhang from CIBR. You can convert docx to pdf freely ever after!"
#     for l,m,n in os.walk(docx_folder1):
#         for i in os.scandir(l):
#             print(f"turn to {i}")
#             convert(l + "/" + i.name.split(".")[0] + ".docx",l + "/" + i.name.split(".")[0] + ".pdf" )
#             print(f"finish {i}")
# zxldocx2pdf(r"D:\word2pdf")





# \\\\\\\\\**Best*用pywin32把docx转为pdf，文件夹里的文件都转完会报错。这个报错是第一个文件，故可以忽略这个错误。但是要在ctrl+alt+del，中关上word
print("start")
import win32com.client
import os# terminal ：pip install pdf2docx
import shutil
import time
wdFormatPDF = 17
def zxldocx2pdf(docx_folder1):
# "This is an easy-go file wrote by Xiaolin Zhang from CIBR. You can convert pdf to docx freely ever after!"
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = False
    for l,m,n in os.walk(docx_folder1):
        for i in os.scandir(l):
            time.sleep(3)
            print(f"turn to {i}")
            doc = word.Documents.Open(l+"/"+i.name)
            doc.SaveAs(l+"/"+i.name.split(".")[0]+".pdf", FileFormat=wdFormatPDF)
            doc.Close()
            print(f"finish {i}")
    word.Quit()
zxldocx2pdf(r"D:\word2pdf")





