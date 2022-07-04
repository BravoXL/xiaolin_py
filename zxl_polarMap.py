# >>>>>>>>>>>>>>>>polar demo
# import numpy as np
# import matplotlib.pyplot as plt
# plt.style.use("ggplot")
# angle1=np.array([0.25,0.75,1,1.5,1.75,0.25])#copy the first dot, we can make a close region
# radius1=[20,60,40,80,90,20]
# plt.polar(angle1*np.pi,radius1,"ro-",alpha=0.75)# "0"visible."r"dot color
# plt.fill(angle1*np.pi,radius1,"g",alpha=0.25)#alpha means transparent
# plt.ylim(0,100)#in polarplot，this code must be place at the end.
# plt.show()

#>>>>>>>>>>>>>>> data analysis
#????????????thetagrids_location
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")
# plt.rcParams["font.sans-serif"]=["SimHei"]#"用黑体显示中文"
data0=pd.read_excel(r"D:\张晓琳！！！\xiaolin_py\polar.xlsx",index_col="Name")
Anna0=data0.query("Name=='Anna'")['Score']
Jim0=data0.query("Name=='Jim'")['Score']
Discipline0=data0.query("Name=='Anna'")["Discipline"]
angle0=np.linspace(0,2*np.pi,len(Anna0),endpoint=False)
Anna_p=np.concatenate((Anna0,[Anna0[0]]))
Jim_p=np.concatenate((Jim0,[Jim0[0]]))
Discipline_p=np.concatenate((Discipline0,[Discipline0[0]]))
angle0_p=np.concatenate((angle0,[angle0[0]]))
#plot
figure0=plt.figure()
plt.suptitle("DIFF",fontsize=20,fontweight="bold",color="black")
plot1=figure0.add_subplot(111,polar=True)
plot1.plot(angle0_p,Anna_p,"ro-",linewidth=2,alpha=1,label="Anna")
plot1.fill(angle0_p,Anna_p,"r",alpha=0.25)
plot1.plot(angle0_p,Jim_p,"bo-",linewidth=2,alpha=1,label="Jim")
plot1.fill(angle0_p,Jim_p,"b",alpha=0.25)
plot1.set_ylim(0,100)
plot1.set_thetagrids(angle0_p*180/np.pi,Discipline_p)
plt.legend(loc="best")
plt.show()

