import turtle
kibritcopleri=[]

class geometrik_sekiller:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def tanı(self):
        self.a=input("Birinci Ölçüyü Giriniz:")
        self.b=input("ikinci Ölçüyü Giriniz:")
        self.c=input("Üçüncü Ölçüyü Giriniz:")

    def kare(self):
        if self.a == self.b== self.c:
            print("Girilen Ölçülerin tasvir ettiği Şekil=Karedir.")
        else:
            print("Uygun Bir Ölçü Giriniz!")

    def dikdörtgen(self):
        if self.a == self.b +self.c == self.d:
            print("Girilen Ölçülerin tasvir ettiği Şekil=Dikdörtgendir.")

        else:
            print("Uygun Bir Ölçü Giriniz:")


    def ucgen(self):
        if self.a == self.b == self.c:
            print("Girilen Ölçülerin tasvir ettiği Şekil=Dikdörtgendir.")

        else:
            print("Uygun Bir Ölçü Giriniz:")



for i in range(0,12):
    kibritcopleri.append(i)
    print(kibritcopleri)


def ucgen():
    ucgen().turtle.Turtle()
    ucgen().pencolor("red")
    ucgen().pensize(2)
    ucgen().speed(6)

def kare():
    kare().turtle.Turtle()
    kare().pencolor("red")
    kare().pensize(2)
    kare().speed(6)


def dikdörtgen():
    dikdörtgen().turtle.Turtle()
    dikdörtgen().pencolor("red")
    dikdörtgen().pensize(2)
    dikdörtgen().speed(6)

