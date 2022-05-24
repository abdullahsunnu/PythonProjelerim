import pandas as pd


# info dataframe hakkında bilgi verir
df = pd.read_csv("nba.csv")
#print(df.isnull().sum().sort_values(ascending=False)) # boş olan değerleri getirir toplar ve azalan şekilde sıralar
result = df["Salary"].mean() # ortalama maaş
result = df["Salary"].max() # en yüksek maaş
#result = df["Salary"].min() # en düşük maaş
result = df["Salary","Name"] == 25000000.0
print(result)
