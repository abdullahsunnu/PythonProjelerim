import pandas as pd
import numpy as np

df = pd.read_csv("nba.csv")



result = df.head(10) # ilk 10 kaydı getirir
result = len(df.index) # toplam kayıtları getirir
result = df["Salary"].mean() # tüm oyuncuları toplam maaş bilgisini verir
result = df["Salary"].max() # en yüksek maaş bilgisi
result = df[df["Salary"]==df["Salary"].max()]["Salary"].iloc[0] # en yüksek maaşı alan oyuncu ismini verir
result = df[(df["Age"] >=20) & (df["Age"]<=25)][["Name","Team","Age"]].sort_values("Age",ascending=False) # yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
result = df[df["Name"] == "John Holland"]["Team"].iloc[0] # john holland isimli oyuncunun oynadığı takım hangisidir
result = df.groupby("Team").mean()["Salary"] # takımlara gore oyuncuların maaş bilgileri
result = len(df.groupby("Team")) # kac farklı takım mevcuttur
result = df["Team"].nunique()  # kac farklı takım mevcuttur
result = df["Team"].value_counts() # her takımda kac oyuncu oynamaktadır


df = df.dropna() # bos kayıtları sildik
result = df[df["Name"].str.contains("and")]  # isim içerisinde and gecen kayıtları bulur


# ikinci yöntem
def str_find(name):  # isim içerisinde and gecen kayıtları bulur
    if "and" in name.lower():
        return True
    return False

result = df[df["Name"].apply(str_find)]

print(result)