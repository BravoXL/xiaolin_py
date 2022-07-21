# \\\\\\\\1
# import os
# import datetime
# import shutil
# for l,m,n in os.walk(r"D:\2020_001_张岱老师筹办的神经精神障碍系列讲座"):#path
#     for i in os.scandir(l):
#         if ("附件2" in i.name) and ("Annex" in i.name):
#             date1=datetime.datetime.fromtimestamp(i.stat().st_mtime)
#             newfilename1=str(date1.year)+"_"+str(date1.month)+"_"+str(date1.day)+"_"+i.name
#             newpath1= r"D:\2020_NeuropsychiatricDisorders"
#             shutil.copy(l+"/"+i.name,newpath1+"/"+i.name)
# \\\\\\\\\\\-----------------------

# \\\\\\\\\从2022seminar文件夹中抽出文件名含有Flyer的pdf文件
# import os
# import datetime
# import shutil
# for l,m,n in os.walk(r"C:\Users\86135\Desktop\2022_Seminar"):#path
#     for i in os.scandir(l):
#         if ("Flyer" in i.name) and ("pdf" in i.name):
#             # date1=datetime.datetime.fromtimestamp(i.stat().st_mtime)
#             # newfilename1=str(date1.year)+"_"+str(date1.month)+"_"+str(date1.day)+"_"+i.name
#             newpath1= r"C:\Users\86135\Desktop\20220617flyers"
#             shutil.copy(l+"/"+i.name,newpath1+"/"+i.name)

# \\\\\\\批量修改文件名，给文件名加上2022. ,输入和输出文件夹最好是两个分支，不要嵌套
# import os
# import datetime
# import shutil
# for l,m,n in os.walk(r"C:\Users\86135\Desktop\20220617flyers\新建文件夹"):#path
#     for i in os.scandir(l):
#         newpath1= r"C:\Users\86135\Desktop\out"
#         shutil.copy(l + "/" + i.name, newpath1 + "/" + "Flyer_2022"+i.name.split("r_")[1])
#

# \\\\\\\\\从文件夹中抽出文件名含有flyer和Flyer的pdf文件
# import os
# import datetime
# import shutil
# import re
# for l,m,n in os.walk(r"C:\Users\86135\Desktop\执行"):#path
#     for i in os.scandir(l):
#         # if ("Flyer" in i.name) and ("pdf" in i.name):
#         if re.search("flyer",i.name,re.IGNORECASE) and ("pdf" in i.name):
#             newpath1= r"C:\Users\86135\Desktop\OUT"
#             shutil.copy(l+"/"+i.name,newpath1+"/"+i.name)


# \\\\\\\\\\把20210714_flyer改成Flyer_20210714
# import os
# import datetime
# import shutil
# import re
# for l,m,n in os.walk(r"C:\Users\86135\Desktop\OUT\新建文件夹"):#path
#     for i in os.scandir(l):
#             newpath1= r"C:\Users\86135\Desktop\out1"
#             shutil.copy(l + "/" + i.name, newpath1 + "/" + "Flyer_" + i.name.split("_")[0]+".pdf")
#

# \\\\\\\\\把Flyer_20210630改成4_Flyer_20210630
# import os
# import datetime
# import shutil
# import re
# chosfoler1=r"C:\Users\86135\Desktop\OUT"
# outputfolder1=r"C:\Users\86135\Desktop\out1"
# for l,m,n in os.walk(chosfoler1):#path
#     for i in os.scandir(l):
#             shutil.copy(l + "/" + i.name, outputfolder1 + "/" + "4_" + i.name)


# \\\\\\\\\从2021_Seminar 提取所有含有flyer Flyer 的pdf
# import os
# import datetime
# import shutil
# import re
# chosfoler1=r"C:\Users\86135\Desktop\2021_Seminar"
# outputfolder1=r"C:\Users\86135\Desktop\out"
# for l,m,n in os.walk(chosfoler1):
#     for i in os.scandir(l):
#         if re.search("flyer", i.name, re.IGNORECASE) and ("pdf" in i.name):
#             shutil.copy(l + "/" + i.name, outputfolder1 + "/" + i.name)
#

# \\\\\\\\\加上2021，把1_Flyer_0105_Xiong Xiao改成1_Flyer_20210105_Xiong Xiao
# import os
# import datetime
# import shutil
# import re
# chosfoler1=r"C:\Users\86135\Desktop\out"
# outputfolder1=r"C:\Users\86135\Desktop\oout"
# for l,m,n in os.walk(chosfoler1):
#     for i in os.scandir(l):
#         if re.search("flyer", i.name, re.IGNORECASE) and ("pdf" in i.name):
#             shutil.copy(l + "/" + i.name, outputfolder1 + "/" + "1_Flyer_2021" + i.name.split("r_")[1])
#

# \\\\\\\\\从2019_Seminar 提取所有含有B-type 的word
# import os
# import datetime
# import shutil
# import re
# chosfoler1=r"D:\CIBR\T谭禄彬\+学术报告\2019_Seminar"
# outputfolder1=r"C:\Users\86135\Desktop\input"
# for l,m,n in os.walk(chosfoler1):
#     for i in os.scandir(l):
#         if re.search("Flyer", i.name, re.IGNORECASE) :
#             shutil.copy(l + "/" + i.name, outputfolder1 + "/" + i.name)



# \\\\\\\\\把1_20200403_Flyer_Qing Yu改成1_Flyer_20200403_Qing Yu
# # \\\\\\\\\把2_20200110_Flyer_Yang Du  改成 2_Flyer_20200110_Yang Du
#
# import os
# import datetime
# import shutil
# import re
# chosfoler1=r"D:\CIBR\M毛军文老师指导摘要整理\按类别5类\2_Invited\新建文件夹"
# outputfolder1=r"C:\Users\86135\Desktop\out"
# for l,m,n in os.walk(chosfoler1):
#     for i in os.scandir(l):
#         if re.search("flyer", i.name, re.IGNORECASE) and ("pdf" in i.name):
#             shutil.copy(l + "/" + i.name, outputfolder1 + "/" + "2_Flyer_" + i.name.split("_")[1]+"_"+i.name.split("r_")[1])




# \\\\\\\\\把3_附件2_Annex II_20200515_Flyer_Xiangdong Wang改成 3_Flyer_20200110_Yang Du

# import os
# import datetime
# import shutil
# import re
# chosfoler1=r"D:\CIBR\M毛军文老师指导摘要整理\按类别5类\3_Neuropsychiatric Disorders\新建文件夹"
# outputfolder1=r"C:\Users\86135\Desktop\out"
# for l,m,n in os.walk(chosfoler1):
#     for i in os.scandir(l):
#         if re.search("flyer", i.name, re.IGNORECASE) and ("pdf" in i.name):
#             shutil.copy(l + "/" + i.name, outputfolder1 + "/" + "3_Flyer_" + i.name.split("_")[2]+"_"+i.name.rsplit("_",1)[1])


# \\\\\\\\\执行文件夹 提取所有含有Record 的xlsx
import os
import datetime
import shutil
import re
choosefoler1=r"D:\CIBR\T谭禄彬\+学术报告\+2021启动内部学术交流会\执行"
outputfolder1=r"C:\Users\86135\Desktop\out"
for l,m,n in os.walk(choosefoler1):
    for i in os.scandir(l):
        if re.search("Record", i.name, re.IGNORECASE) and ("xlsx" in i.name) :
            shutil.copy(l + "/" + i.name, outputfolder1 + "/" + i.name)
