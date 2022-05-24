import pandas as pd
import numpy as np


# Data

numbers = [20,30,40,50]
latter = ["a","bdullah","c","d"]
scalar = 5
dict = {"a":10,"b":20,"c":30,"d":40}

random_numbers = np.random.randint(0,100,6)

# pandas_series = pd.Series() # float ve boş bir sri gelir
# pandas_series = pd.Series(numbers) # bilgileri belli bir sirada verir numaralandırarak
# pandas_series = pd.Series(latter) # bilgileri belli bir sirada verir numaralandırarak
# pandas_series = pd.Series(scalar ,[1,2,3,])  # scaler bilgi verdiğimiz index numarası kadar artırılır.
# pandas_series = pd.Series(numbers ,["a","b","c","d"]) # numara yerine kendi belirlediğin bilgileri de verebiliyoruz
# pandas_series = pd.Series(dict) # istediğin sayıya istediğin ddeğeri verebilirim
pandas_series = pd.Series(random_numbers) # numpy kutuphanesiyle 0 dan 100 e kadar alti tane sayı oluşturup indexleyebiliriz

print(pandas_series)
