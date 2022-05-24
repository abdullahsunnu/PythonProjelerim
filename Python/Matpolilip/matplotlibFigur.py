import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x**3
z = x**2

"""
figure = plt.figure()
axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])
axes_cube.plot(x,y,"b")

axes_cube.set_xlabel("X Axis")
axes_cube.set_ylabel("Y Axis")
axes_cube.set_title("Cube")

axes_suquare = figure.add_axes([0.15,0.6,0.25,0.25]) # ikinci figurun konumunu belirledik sağdan ustten ve toplam alanından
axes_suquare.plot(x,y,"r")

axes_suquare.set_xlabel("X Axis")
axes_suquare.set_ylabel("Y Axis")
axes_suquare.set_title("suquare")
plt.legend()

"""
"""
# Çizgi içerisinde çizgi
figure = plt.figure()
axes = figure.add_axes([0,0,1,1])
axes.plot(x,z,label="Square")
axes.plot(x,y, label="Cube")
axes.legend()
"""

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(4,4)) # nrows sattır, ncols sutun, figisze grfaik alan temsil eder
axes[0].plot(x,y) # satırın ve sütunun değerleri
axes[0].set_title("Cube")
axes[1].plot(x,z)
axes[1].set_title("Square")
plt.tight_layout()
fig.savefig("figure2.pdf")
plt.show()


