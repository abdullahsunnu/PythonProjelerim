import matplotlib.pyplot as plt
import numpy as np

# ÖRNEK 1
"""
x = [1,2,3,4]
y = [1,4,9,16] # x  in karelerini aldık

plt.plot(x,y,"o--r") # o marker temzil eder,--kesik cizgi, r: red temsil eder
plt.axis([0,6,0,20]) # x sıfırdan altıya kadar git , y sıfırdan yirmiye kadar git

plt.title("Grafik Başlığı")
plt.xlabel("x label")
plt.ylabel("y label")
plt.show() # grafiği gormemizi sağlar
"""
"""
x = np.linspace(0,2,100) # 0 ile 2 arasında 100 eşit parcaya bol

plt.plot(x,x,label="linear",color="red") # düz cizgi
plt.plot(x,x**2 ,label="quadratic",color="yellow") # karesel cizgi
plt.plot(x,x**3,label="cubic",color="green") # küpsel cizgi

plt.xlabel("x label")
plt.ylabel("y label")

plt.title("simple plot")
plt.legend() # grafiğin haritasının labellardaki değeri otomatik olarak boş yere atar
plt.show()

"""
"""
x = np.linspace(0,2,100)
fig,axs = plt.subplots(2) # iki tane grafik oluşturur

axs[0].plot(x,x, color="red")
axs[0].set_title("Linear")# birinci grafiğin başlığı
axs[1].plot(x,x**2, color="yellow")
axs[1].set_title("quanratic") # ikinci grafiğin başlığı
plt.tight_layout()
plt.show()
"""
"""
 # Yan yana grafik
x = np.linspace(0,2,100)
fig,axs = plt.subplots(2,2) # yan yana oluşturur
fig.suptitle("Grafik başlığı") # hepsinin başlığı

axs[0,0].plot(x,x, color="red") # 4 de 1
axs[0,1].plot(x,x**2,color="yellow") # 4 de 2
axs[1,0].plot(x,x**3,color="green")# 4 de 3
axs[1,1].plot(x,x**4,color="black") # 4 de 4 , x 4 le carpar
plt.show()
"""

import pandas as pd

df = pd.read_csv("nba.csv")
df = df.drop(["Number"],axis = 1).groupby("Team").mean()

df.head(5).plot(subplots = True)
plt.legend()
plt.show()