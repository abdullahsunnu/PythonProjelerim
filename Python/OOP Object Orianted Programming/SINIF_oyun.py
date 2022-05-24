import random as rnd
import time


print("         ******* HOŞGELDİNİZ***********")
time.sleep(2)

print("Savaş Başlıyor")


time.sleep(2)

kahramanAd = input("Kahraman Adının Giriniz: ")
dusmanAd = input("Düşman Adını Giriniz: ")

class Kahraman():
    def __init__(self):
        self.kahramanAd = kahramanAd
        self.kahramanPara = 10
        self.kahramanEnerji  = 100

    def saldır(self,kahramanHasar):
        self.kahramanHasar = kahramanHasar
kahraman1 = Kahraman()

class Dusman():
    def __init__(self):
        self.dusmanAd = dusmanAd
        self.dusmanPara = 10
        self.dusmanEnerji = 100

    def saldır(self,dusmanHasar):
        self.dusmanHasar = dusmanHasar

dusman1 = Dusman()

kahramanSayac = 0
dusmanSayac = 0

while True:
    if kahraman1.kahramanEnerji ==0:
        kahraman1.kahramanPara -=1
        kahraman1.kahramanEnerji = 100

    elif dusman1.dusmanEnerji == 0:
        dusman1.dusmanPara -=1
        dusman1.dusmanEnerji = 100

    if kahraman1.kahramanPara ==0:
        print("Düşman,",kahramanSayac,"kez hasar verdi,kahraman ise ",dusmanSayac, "kez hasar verdi ",dusmanAd, "kazandı")
        break

    if dusman1.dusmanPara == 0:
        print("Düşman,", dusmanSayac, "kez hasar verdi,kahraman ise ", kahramanSayac, "kez hasar verdi ", kahramanAd, "kazandı")
        break

    kahraman1.saldır(rnd.randint(1,100))
    dusman1.saldır(rnd.randint(1,100))
    if kahraman1.kahramanHasar>dusman1.dusmanHasar:
        print("Kahraman :",kahraman1.kahramanHasar,"düşman : ",dusman1.dusmanHasar,"---> Düşman",dusman1.dusmanHasar ," hasar aldı")
        time.sleep(0.1)
        dusman1.dusmanEnerji -= 10
        dusmanSayac +=1

    elif dusman1.dusmanHasar> kahraman1.kahramanHasar:
        print("Düşman :", dusman1.dusmanHasar, "kahraman : ", kahraman1.kahramanHasar, "---> Kahraman ",kahraman1.kahramanHasar ,"hasar aldı")
        time.sleep(0.1)
        kahraman1.kahramanEnerji -=10
        kahramanSayac+=1
