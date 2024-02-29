
# 1 chi masala

# class Car:
#     def __init__(self, model, prise, year, color, engine):
#         self.model = model
#         self.price = prise
#         self.year = year
#         self.color = color
#         self.engine = engine
#
#
# class BMW(Car):
#
#     """
#          Bu class boshqa class dan meros oladi va avtomobil haqida ma'lumot olib va ma'lumotlarni qaytaradi
#     """
#     def __init__(self, model, prise, year, color, engine):
#         super().__init__(model, prise, year, color, engine)
#
#
#     def car_info(self):
#         return f"Avtomobil nomi {self.model}: yili {self.year}: va dvigatel dyumi {self.engine}"
#
#     def addition_info(self):
#         return f"Qushimcha ma'lumot: Avtomobilni narxi {self.price}$: va rangi {self.color}"
#
#
#
# class Malibu(Car):
#
#     """
#         Bu class boshqa class dan meros oladi va avtomobil haqida ma'lumot olib va ma'lumotlarni qaytaradi yana polimorfizam ilatilinadi
#     """
#     def __init__(self, model, prise, year, color, engine):
#         super().__init__(model, prise, year, color, engine)
#
#     def car_info(self):
#         return f"Avtomobilni narxi {self.price}$:  va rani {self.color}"
#
#     def addition_info(self):
#         return f"Qushimcha ma'lumot: Avtomobil modeli {self.model}: dvigatel dyumi {self.engine} va yili {self.year}:"
#
#
# class Lamborghini(Car):
#     """
#         Bu class boshqa class dan meros oladi va avtomobil haqida ma'lumot olib va ma'lumotlarni qaytaradi yana polimorfizam ilatilinadi
#     """
#
#     def __init__(self, model, prise, year, color, engine):
#         super().__init__(model, prise, year, color, engine)
#
#     def car_info(self):
#         return f"Avtomobil nomi {self.model}: yili {self.year}: dvigatel dyumi {self.engine} narxi {self.price}$: va rangi {self.color}"
#
#     def addition_info(self):
#         return "Qushimcha ma'lumot: Qushimcha ma'lumot topilmadi"
#
#
# user = BMW("M5", "50.000", 2018, "qora", 4.5)
# print(user.car_info())
# print(user.addition_info())
#
#
# user2 = Malibu("Malibu 1", "14.000", 2014, "qizil", 2.4)
# print(user2.car_info())
# print(user2.addition_info())
#
#
# user3 = Lamborghini("Urus", "99.000", 2023, "sariq", 4.0)
# print(user3.car_info())
# print(user3.addition_info())


#=======================================================================================================================

# 2 chi masala

class Figure:
    def __init__(self, name):
        self.name = name


class Triangle(Figure):
    def __init__(self, name, a, b, c, h):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c
        self.b = b
        self.h = h

    def perimetr(self):
        p = self.a + self.b + self.c
        return f"Uchburchakni perimetri: {p}"

    def uch_yuzasi(self, b, h):
        self.b = b
        self.h = h

        natija = 0.5 * self.b * self.h
        return f"Uchburchakni yuzasi {natija}"



class Square(Figure,Triangle):
    def __init__(self, name, a, b):
        super().__init__(name, a, b)


    def perimetr(self):
        p = 2 * (self.a * self.b)
        return f"Turtburchakni perimetri {p}"

    def turt_yuzasi(self):
        S = self.a * self.b
        return f"Turtburchakning yuzasi {S}"



class Circle(Figure):
    def __init__(self, name, r):
        super().__init__(name)
        self.r = r

    def doira_uzunligi(self):
        c = 2 * 3.14 * self.r
        return f"Doiraning uzunligi {c}"

    def doira_yuzasi(self):
        s = 3.14 * self.r * self.r
        return f"Doiraning yuzazi {s}"


user = int(input("Uchburchak uchun - 1 ni bosing:"
             "Turtburchak uchun - 2 ni bosing"
             "Doira uchun - 4 ni bosing: - "))

if user == 1:
    p_y = int(input("Perimetr uchun: 1 / Yuzani hisoblash uchun: 2 ni bosing: "))
    if p_y == 1:
        a = int(input("A sonni kriting: "))
        b = int(input("B sonni kriting: "))
        c = int(input("C sonni kriting: "))

        natija = Triangle("user", a=a, b=b, c=c)
        print(natija.perimetr())
    else:
        b = int(input("b ni  kriting: "))
        h = int(input("h ni kriting: "))

        natija = Triangle.uch_yuzasi(Triangle, b=b, h=h)
        print(natija)

elif user == 2:
    p_y = int(input("Perimetr uchun: 1 / Yuzani hisoblash uchun: 2 ni bosing: "))
    if p_y == 1:
        a = input("A sonni kriting: ")
        b = input("B sonni kriting: ")
        natija = Square("user", a=a, b=b)
        print(natija.perimetr("user", a=a, b=b))
    else:
        a, b = input("A sonni kriting: "), input("B sonni kriting: ")
        natija = Square("user", a=a, b=b)
        print(natija.turt_yuzasi())


elif user == 3:
    u_y = int(input("Doirani uzunligi uchun: 1 / Yuzasi uchun: 2 ni bosing: "))
    if u_y == 1:
        r = float(input("Radiusni kriting: "))
        natija = Circle("user", r=r)
        print(natija.doira_uzunligi())
    else:
        r = float(input("Radiusni kriting: "))
        natija = Circle("user", r=r)
        print(natija.doira_yuzasi())


elif user > 3:
    print("Siz mavjud bulmagan sonni krittingiz !!! ")


























































