import pandas as pd

# df = pd.DataFrame() # boş bir data frame listesi
# df = pd.DataFrame()  # sayılardan oluşan bir liste tanımladık
list = [["Ahmet",50],["Ali",60],["Apo",100],["Sıla",40]] # data ya notları girdik ve onun uzerinden index numarasını ve başlıkları değiştirdik
dict = {"Name": ["Ahmet","Ali","Apo","Sıla"], "Greade": [50,60,100,40]} # listede oluşturduğumuz gibi işlemler yaptık ama tek satırda
dict_list = [
                {"Name":"Ahmet","Grade":50},
                {"Name":"Ali","Grade":60},
                {"Name":"Apo","Grade":100},
                {"Name":"Sıla","Grade":40}
            ]

# df = pd.DataFrame(data, columns = ["Name","Grade"], dtype= float, index = [1,2,3,4]) # column ve index numarasını belirtmezsen index columndan once olmazsa hata veriri ve dtype ine float dersem sayıları ondalık olarak gosterir.
# df = pd.DataFrame(dict, index=["254","265","321","254"]) # index numaralarını değiştirdik
df = pd.DataFrame(dict_list , index=["254","265","321","254"]) # dict_list de aynı list ve dict nin yaptığı görevi görür farklı yollarına vurgu yaptık

print(df)

# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,4,7])
#
# data = dict(apples = s1 , oranges = s2)
#
# df = pd.DataFrame(data) # verdiğimiz datalara yani apples ve oranges belli baaşlıklar oluyor ve seriler de karşısına geçiyor.
#
#
#
# print(df)
