import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0.0,2,0.01)
y1=np.sin(2*np.pi*x)
y2=1.2*np.sin(4*np.pi*x)
fig1,plot1=plt.subplots()
plot1.plot(x,y1,x,y2,color="black")
plot1.fill_between(x,y1,y2,where=y2>y1,facecolor="y")
plot1.fill_between(x,y1,y2,where=y2<=y1,facecolor="v")
plt.show()