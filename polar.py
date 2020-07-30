import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

theta = pd.read_excel(".xlsx",usecols = [6],skiprows = [1,2],skipfooter = 0)
theta_30 = theta - 30
r = pd.read_excel(".xlsx",usecols = [7],skiprows = [1,2],skipfooter = 0)

theta_rad = np.deg2rad(theta_30)

fig = plt.figure(figsize = (6, 6))
ax = fig.add_subplot(111, projection = "polar")

ax.scatter(theta_rad,r,marker = "o",c = "black",s = 20)

ax.set_thetagrids(np.arange(36)*10.)
ax.set_theta_direction(-1)

ax.set_theta_zero_location("N")

ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])

ax.set_axisbelow(True)

fig.savefig("φ=45°(-45°).pdf")
# print(theta_30)
# plt.show()
