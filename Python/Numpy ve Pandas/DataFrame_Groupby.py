import pandas as pd

personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)
result = df

result = df["Maaş"].sum() # Maaş satırını toplar
result = df.groupby("Departman").groups # departman satırını gruplar
result = df.groupby(["Departman","Semt"]).groups # departman ve semt satırını gruplar




# for name, group in df.groupby("Semt"): # hangi semtte oturduklarıyla gruplar
#     print(name)
#     print(group)


for name, group in df.groupby("Departman"): # hangi departmanda olduklarını gruplar
    print(name)
    print(group)








print(result)