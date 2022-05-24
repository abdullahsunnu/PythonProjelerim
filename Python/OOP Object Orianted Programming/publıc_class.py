class Calisanlar():
    def __init__(self, isim, soyisim, tckn, departman):
        self.__isim     = isim
        self.soyisim    = soyisim
        self.__tckn     = tckn
        self.departman  = departman

calisan_1 = Calisanlar("Hacı Abdullah", "SÜNNÜ","01234567891", "Yazılım")

print(calisan_1.departman)

print(calisan_1.isim)



