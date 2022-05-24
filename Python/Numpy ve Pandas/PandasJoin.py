import pandas as pd

# customers = {
#     "CustomerId" : [1,2,3,4],
#     "FirstName" : ["Ahmet","Mehmet","Hüseyin","Sıla"],
#     "LastName" : ["Yilmaz","Cakır","Ateş","Bulut"]
# }
#
# ordres = {
#     "OrderId" : [10,11,12,13],
#     "CustomerId" : [1,2,5,7],
#     "OrderDate": ["2010-07-04","2022-01-09","2011-09-14","2018-05-08"]
# }
#
# df_Customers = pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
# df_Orders = pd.DataFrame(ordres,columns=["OrderId","CustomerId","OrderDate"])
#
# print(df_Customers)
# print(df_Orders)
#
# result = pd.merge(df_Customers,df_Orders,how="inner") # siparişi olan tüm müşterileri getirir
# result = pd.merge(df_Customers,df_Orders,how="right") # sağdakileri getir sağdaki Orders soldakileri getirme deriz
# result = pd.merge(df_Customers,df_Orders,how="left") # soldakileri getir sağdakileri getirme
# result = pd.merge(df_Customers,df_Orders,how="outhor") # sağdaki ve soldaki bütün kayıtlar getirirlir
# print(result)

customersA = {
    "CustomerId" : [1,2,3,4],
    "FirstName" : ["Ahmet","Mehmet","Hüseyin","Sıla"],
    "LastName" : ["Yilmaz","Cakır","Ateş","Bulut"]
}

customersB = {
    "CustomerId" : [4,5,6,7],
    "FirstName" : ["Murat","Arda","Hasan","Sinem"],
    "LastName" : ["Yılar","Köpek","Köz","Ay"]
}

df_CustomersA = pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])
df_CustomersB = pd.DataFrame(customersB,columns=["OrderId","CustomerId","OrderDate"])

result = pd.concat([df_CustomersA,df_CustomersB],axis=0)
result = pd.concat([df_CustomersA,df_CustomersB],axis=1)
print(result)