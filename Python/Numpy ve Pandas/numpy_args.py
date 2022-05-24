import numpy as np # DAHA ÇOK MATEMATİKSEL HESAPLAMALAR YAPMAK İÇİN KULLANILIR DAHA AZ YER KAPLAR

# result = np.array([1,2,3,4,6,8])
# result = np.arange(1,10) # 1 den başlayıp 9 a kadar sayı dondürür
# result = np.arange(10,100,3) # 10 dan başlar 100 e kadar 3 er sayar
# result = np.zeros(10) # 10 tane sıfırlardan oluşan liste çağırır
# result = np.ones(10)   # 10 tane birlerden oluşan liste çağırır
# result = np.linspace(0,100,5) # 0 ile 100 arasında sayı veriri 5 eşit parcaya böler
# result = np.linspace(0,5,5) # 0 dan 5 e kadar git 5 eşit parcaya böl
# result = np.random.randint(0,10)  # 0 ile 9 arasında biirbirinden farklı sayılar verir
# result = np.random.randint(20) # 0 ile 19 arsında sayı oluşturur
# result = np.random.randint(0,50,3) # 0 ile 50 arasında 3 tane sayı oluşturur
# result = np.random.rand(1,9)  # 1 den başlar 9 tene sayı oluşturur
# result = np.random.randn(5) # 5 tane tüm sayılardan (artılı veya eksili) sayı veriri

"""
np_array = np.arange(50)
np_multi = np_array.reshape(5,10)  # 0 dan 50 e kadar 5 e 10 luk bir matris oluşturur.
print(np_multi.sum(axis=1)) # matrisin satırların toplamını veriri.
print(np_multi.sum(axis=0))  # matrisin sütunların toplamını veriri.
"""

rnd_numbers = np.random.randint(1,100,10) # 1 ile 100 arasında 10 tane sayı veriri
print(rnd_numbers)
en_buyuk = rnd_numbers.max() # sayılardan en büyüğünü verir.
en_kücük = rnd_numbers.min() # sayılardan en küçüğünü verir.
ortalama = rnd_numbers.mean() # sayıların ortalamasını verir
en_büyük_sayı_indexi = rnd_numbers.argmax() # sayıların en küçüğğünün index numarasını verir
en_küçük_sayı_indexi = rnd_numbers.argmin() # sayıalrın en küçüğünün index numarasını verir

print(f"En büyük sayı {en_buyuk} dır ve en küçük sayı {en_kücük} dir ortalaması {ortalama} dir en büyük sayının indexi {en_büyük_sayı_indexi} dir ve en küçük sayının indexi {en_küçük_sayı_indexi} dir.")


# print(result)