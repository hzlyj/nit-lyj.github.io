import numpy as np
import matplotlib.pyplot as plt

ω=np.pi
a=2
φ=np.pi/3
t=np.linspace(-np.pi, np.pi, 1000)
x1 =a*np.cos(ω*t+φ)
plt.figure()
plt.xlabel(' ')
plt.ylabel(' ')                                #设置坐标轴的文字标签

ax = plt.gca()                                            # get current axis 获得坐标轴对象

ax.spines['right'].set_color('none') 
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边

ax.xaxis.set_ticks_position('bottom')   
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴

ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
ax.set_title("X=Acos(ωt+φ)")
plt.plot(t,x1)


ω=np.pi
a=2
n=3
φ=np.pi/3
t=np.linspace(-np.pi, np.pi, 1000)
x2 =np.e**t*a*np.cos(ω*t+φ)
plt.figure()
plt.xlabel(' ')
plt.ylabel(' ')                                #设置坐标轴的文字标签

ax = plt.gca()                                            # get current axis 获得坐标轴对象

ax.spines['right'].set_color('none') 
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边

ax.xaxis.set_ticks_position('bottom')   
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴

ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
ax.set_title("X=Ce**αtcos(ωt+φ)   α>0")
plt.plot(t,x2)



ω=np.pi
a=2
n=3
φ=np.pi/3
t=np.linspace(-np.pi, np.pi, 1000)
x2 =np.e**-t*a*np.cos(ω*t+φ)
plt.figure()
plt.xlabel(' ')
plt.ylabel(' ')                                #设置坐标轴的文字标签

ax = plt.gca()                                            # get current axis 获得坐标轴对象

ax.spines['right'].set_color('none') 
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边

ax.xaxis.set_ticks_position('bottom')   
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴

ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
ax.set_title("X=Ce**αtcos(ωt+φ)   α<0")
plt.plot(t,x2)

plt.show()


