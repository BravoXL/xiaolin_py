#function: <<<count the times of each elements in the excel matrix,which contain None cells in the ends of the rows>>>.

# >>>>>>>>>>>>Step1:Before running：we should put the names in matrix(which can contain None cells,with one speaker's reviewers as a row.)
import openpyxl as zxl
import pandas as pd

# >>>>>>>>>>>>Step2:Change the file path.
path1=r"D:\zxl_PreciousPythonFiles_\zxlExcel\20220705.xlsx"
excel1=zxl.load_workbook(path1)

# >>>>>>>>>>>>Step3:Change the selected sheet.
sheet1=excel1["raw_20220706 (2)"]

# >>>>>>>>>>>>Step4:Change the selection matrix area
area1=sheet1["B1:M17"]

Names0 = []
for i in area1:
    for c in i:
        Names0.append(c.value)

Names0_dNone=list(filter(None,Names0))#Names0_dNone,area1 delete the Name item.

pNames=list(set(Names0_dNone))# set, delete the duplicates,

pNames.sort()

# >>>>>>>>>>>>Step5:Print the PI names in a-z order,then check the upper and lower letters of the same person. And replace the duplicated names by ctrl+F in the excel file.
list(map(print,pNames))# print the list elements vertically,you can aslo try # print(*pNames)
print("BravoZxl_"*10)

# >>>>>>>>>>>>Step6:print out the counted results
result_Index_a_z=pd.value_counts(Names0_dNone).sort_index(ascending=True)#Best
result_Num_z_a=pd.value_counts(Names0_dNone)
result_Num_a_z=pd.value_counts(Names0_dNone,ascending=True)

# >>>>>>>>>>>>Step7:paste to the excel
print(result_Index_a_z)#paste,文本导入导向，固定宽度
