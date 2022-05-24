import pandas as pd
df = pd.read_csv("imdb.csv")


result = df
result = df.columns
result = df.info

result = df.loc[4] # ilk 5 kaydı verir
result = df.head(5)  # ilk 5 kaydı verir
result = df.loc[10]  # ilk 10 kaydı verir
result = df.head(10)  # ilk 10 kaydı verir
result = df.tail(5)  # son 5 kaydı getirir
result = df.tail(10) # son 10 kaydı getirir
result = df["Movie_Title"]  # sadece movie title kolonunu getirir
result = df["Movie_Title"].head(5) # movie title ait 5 kaydı getirir
result = df[["Movie_Title","Rating"]].head(5) # Movie title ve rating kolonunu içeren ilk 5 kayıtı getirir
result = df[["Movie_Title","Rating"]].tail(7)  # Movie title ve rating kolonlarını içeren son 7 kaydı getirir.
result = df[5:][["Movie_Title","Rating"]].head() # sadece Movie title ve rating kolonlarını içeren ikinçi 5 kaydı alır
result = df[5:20][["Movie_Title","Rating"]].head(10) # sadece Movie title ve rating kolonlarını içeren 5 ike 20 arasında 10 kaydı alır
result = df[df["Rating"] >= 8.0][["Movie_Title","Rating"]].head(50) # sadece Movie Title ve rating kolonlarını içeren ve imdb puanı 8.0 ve üstünde olan kayıtlardan ilk 50 tanesini getir.
result = df[(df["YR_Released"] >= 2014) & (df["YR_Released"] <= 2015)][["Movie_Title","YR_Released"]] # yayın tarihi 2014 ve 2015 arasında olan filmlerin isimlerini getir
result = df[(df["Num_Reviews"] >= 100000) | ((df["Rating"] >= 8) & (df["Rating"] <= 9))][["Movie_Title","Rating","Num_Reviews"]]





print(result)
print(df.columns)