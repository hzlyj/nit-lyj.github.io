# 课本图1-12 1-14

* 关于在表格中使用颜色的说明Python代码

```
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
fig = plt.figure(figsize=(8, 8))
ax = axisartist.Subplot(fig, 111)  
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ω=np.pi
a=2
φ=np.pi/3
t=np.linspace(-np.pi, np.pi, 1000)
x1=a*np.cos(ω*t+φ)
ax.set_title("X=Acos(ωt+φ)")
plt.xticks([])
plt.yticks([])
plt.plot(t,x1)
fig = plt.figure(figsize=(8, 8))
ax = axisartist.Subplot(fig, 111)  
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ω=np.pi
a=2
n=3
φ=np.pi/3
t=np.linspace(-np.pi, np.pi, 1000)
x2 =np.e**t*a*np.cos(ω*t+φ)
ax.set_title("X=Ce**αtcos(ωt+φ)   α>0")
plt.xticks([])
plt.yticks([])
plt.plot(t,x2)
fig = plt.figure(figsize=(8, 8))
ax = axisartist.Subplot(fig, 111)  
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ω=np.pi
a=2
n=3
φ=np.pi/3
t=np.linspace(-np.pi, np.pi, 1000)
x2 =np.e**-t*a*np.cos(ω*t+φ)
plt.xticks([])
plt.yticks([])
ax.set_title("X=Ce**αtcos(ωt+φ)   α<0")
plt.plot(t,x2)
plt.show()
```

* 效果图
![Image text](https://github.com/nit-lyj/nit-lyj.github.io/blob/master/1.png)
![Image text](https://github.com/nit-lyj/nit-lyj.github.io/blob/master/2.png)
![Image text](https://github.com/nit-lyj/nit-lyj.github.io/blob/master/3.png)




