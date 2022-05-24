import pandas as pd
import pandas as ps
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index = ["A","B","C"], columns=["Column1","Column2","Column3"])

# KOLONA GÖRE SECME İŞLEMLERİ
result = df
result = df["Column1"] # column 1 i cagırır
result = type(df["Column1"]) # column un tipini veriri
result = df[["Column1","Column2"]] # cok kolonlu işlem yapmak istediğimizde bu şekilde cağırırız.

# SATIRA GÖRE SECME İŞLEMLERİ
# loc["row","column"] => kolon ve satır secmek için ilk başta loc daha sonra row ve column secmemiz gerekiyor
# loc["row"] => loc["column"] => sadece satır secmek istiyorsam loc row sadece colon secmek istiyorsam loc column secmemiz gerekiyor


result =df.loc["A"]
result =type(df.loc["A"])
result = df.loc[:,"Column1"] # colon 1 i verdi
result = df.loc[:,["Column1","Column2"]]  # 11. satırla bu satırdaki işlemler birbirinin aynısı
result = df.loc[:,"Column1":"Column3"] # araya verdiğimiz iki nokta ile başlangıc ve bitiş değerlerini çağırabiliriz.
result = df.loc[:,:"Column3"]  # üstteki örnekle aynı değerleri döndürüyor
result = df.loc["A":"B","Column1":"Column3"] # A ve B satırlarını cağırıyoruz
result = df.loc[:"B",:"Column2"]  # B satırını ve Column2 ye kadar colonları çağırıyoruz
result = df.loc["A","Column2"] # A indexteki satırın 2. column unu alabilirim
result = df.loc["C","Column1"] # C indexteki satırın 1. columunu alabilirim
result = df.loc[["A","B"],["Column1","Column2"]] # A ve B satırlarını sec bunlar arasından kolon 1 ve kolon 2 yi getir.


# Yeni kolon eklemek istersek
df["Column4"] = pd.Series(randn(3),["A","B","C"])
df["Column5"] = df["Column1"] + df["Column3"]


# Kolon silme işlemi

result = df.drop("Column5", axis=1, inplace=False)



print(result)
print(df)
