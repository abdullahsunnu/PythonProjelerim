# class sınıf:
#     metin = "bu gun sınıf kavramını oğreniyorumm"
#

# class Topalama:
#     a = 15
#     b = 50
#     c = a + b


class Oyun:
    def __init__(self):
        self.enerji = 50
        self.para = 100
        self.fabrika = 4
        self.isci = 10
    def goster(self):
        print("enerji: ", self.enerji)
        print("para: ", self.para)
        print("fabrika: ", self.fabrika)
        print("işci: ", self.isci)


class Dusman(Oyun): # dusmandan sonra oyun sınıfını eklememizle oyun sınıfının ozellikleri dusman sınıfına gelmektedir.
    def __init__(self):
        Oyun.__init__(self)
        self.hak = 0
        print("hak: ", self.hak)


macera = Oyun()
print(macera.goster())
print("********************************")

dusman = Dusman()
print(dusman.goster())