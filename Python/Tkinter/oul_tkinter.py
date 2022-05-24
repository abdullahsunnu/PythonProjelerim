from tkinter import *

class Uygulama(object):
    def __init__(self):
        self.etiket = Label(text="Dosyayı silmek \n istediğinize emin misiniz?")
        self.etiket.pack()


pencere = Tk()
uyg = Uygulama()
mainloop()