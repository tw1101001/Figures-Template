import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

x = pd.read_excel(".xlsx",sheet_name = "",usecols = [0],skiprows = [0],skipfooter = 0)
y = pd.read_excel(".xlsx",sheet_name = "",usecols = [0],skiprows = [0],skipfooter = 0)

# mx = x.as_matrix()
# my = y.as_matrix()
# nx = mx.flatten()
# ny = my.flatten()

fig = plt.figure(figsize = (5, 5))
ax = fig.add_subplot(111)

ax.scatter(x,y,marker = "o",s = 20)
ax.scatter(x1,y1,marker = "o",s = 20)

# ax.set_xscale("log") #ログスケールで描く．
ax.set_xlim(0,5)
ax.set_xticks([0,1,2,3,4,5])
# ax.set_yscale("log") #ログスケールで描く．
ax.set_ylim(0,20)
ax.set_yticks([0,5,10,15,20])

plt.grid(linestyle = "-",which = "both") #グリッドwhichはxy軸両方にグリッドを描く．
ax.xaxis.label.set_color("black")
ax.yaxis.label.set_color("black")

ax.set_xlabel("$$〔$\mathrm{}$〕",fontname = "Hiragino sans",fontweight = "black")
ax.set_ylabel("$$〔$\mathrm{}$〕",fontname = "Hiragino sans",fontweight = "black")

ax.set_axisbelow(True) #グリッドより点が前に来るように．

# a = np.polyfit(x,y,1) #1次近似の係数を生成．
# yy = np.poly1d(np.polyfit(x, y, 1))(x) #関数を生成．(引数)をつければ引数による係数を計算．この場合，引数はx．
def log(x,a,b):
    return a * x ** b
popt, pcov = curve_fit(log,z2,w2) # poptは最適推定値、pcovは共分散
print(popt)
# print(pcov)
range = [0.00001,1]
log(z2,popt[0],popt[1])
ax.plot(range,log(range,popt[0],popt[1]),c = "black",label = "")
ax.legend() #枠内ラベルの表示

plt.show()
# fig.savefig("sample.png",dpi = 300)

# print(x)
# print(y)
