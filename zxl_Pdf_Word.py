# from pdf2docx import Converter
# pdf_file1=r"D:\2020_NeuropsychiatricDisorders\附件2_Annex II_20200917_Flyer_Tianmei Si.pdf"
# docx_file1=r"D:\2020_NeuropsychiatricDisorders\附件2_Annex II_20200917_Flyer_Tianmei Si.docx"
# cv=Converter(pdf_file1)
# cv.convert(docx_file1,start=0,end=None)
# cv.close()
print("/")


import os# terminal ：pip install pdf2docx
import shutil
from pdf2docx import Converter
def zxlpdf2docx(pdf_folder1):
# "This is an easy-go file wrote by BravoXL. You can convert pdf to docx freely ever after!"
    for l,m,n in os.walk(pdf_folder1):
        for i in os.scandir(l):
            cv = Converter(l+"/"+i.name)
            cv.convert(l+"/"+i.name.split(".")[0]+".docx", start=0, end=None)
            cv.close()
zxlpdf2docx(r"D:\zxl")

