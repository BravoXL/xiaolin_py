import PySimpleGUI as sg
import os.path
from pdf2docx import Converter


def zxlpdf2docx(pdf_folder1):
    # "This is an easy-go file wrote by BravoXL. You can convert pdf to docx freely ever after!"
    for l, m, n in os.walk(pdf_folder1):
        for i in os.scandir(l):
            cv = Converter(l + "/" + i.name)
            cv.convert(l + "/" + i.name.split(".")[0] + ".docx", start=0, end=None)
            cv.close()


#input folder

file_input_list_column = [
    [
        sg.Text("Select Pdf folder！选中文件夹！不是单个文件！"),
        sg.In(size=(25,1),enable_events=True,key="-FOLDER-"),
        sg.FolderBrowse("1.选中Pdf文件夹"),
    ],
    [
        sg.Listbox(
            values=[],enable_events=True,size=(80,20),
            key="-FILE LIST-"
        )
    ]
]
#output word

file_output_list_column=[
       [sg.Text("Get Word，转出的Word在原Pdf文件夹里。")],
       [sg.Button("2.Pdf 转 Word 按钮，2分钟后出结果",size=(30,20),key="-OUTPUT-")],
]

#layout
layout=[
    [
        sg.Column(file_input_list_column),
        sg.VSeparator(),
        sg.Column(file_output_list_column)
    ]
]
window=sg.Window("zxl_Pdf2Word 就两步：1.选中pdf文件夹；2.转喽",layout)

# PySimpleGUI.Window(title="zxl_Pdf2Word",layout=[[]],margins=(300,300)).read()

#event loop
print("zxl")
while True:
    event,values=window.read()
    if event =="Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-FOLDER-":
        folder=values["-FOLDER-"]
        print(folder)

        try:
            #get list of files in folder
            file_list=os.listdir(folder)
        except:
            file_list=[]
        fnames=[
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder,f))
            and f.lower().endswith(".pdf")
        ]
        window["-FILE LIST-"].update(fnames)
    #单击输出按钮
    elif event == "-OUTPUT-":
         zxlpdf2docx(folder)
window.close()
