'''from dataclasses import dataclass
@dataclass
class Book:
    item_id: str
    name: str
    category: str
    year: int
    author: str
    pages: int

    def __post_init__(self):
        if not isinstance(self.item_id, str):
            raise TypeError("ID должен быть строкой")
        if not self.item_id.strip():
            raise ValueError("ID не может быть пустым")

        if not isinstance(self.name, str):
            raise TypeError("should be str")
        if not self.name.strip():
            raise ValueError("should be text in it")

        if type(self.year) is not int:
            raise ValueError("should be int")
        if not (self.year<=2026 and self.year>=1450):
            raise ValueError("time")

        if type(self.pages) is not int:
            raise ValueError("should be int")
        if not (self.pages>0):
            raise ValueError('should be >0')'''


'''class Car:

    def __init__(self, make, model, year): #технический метод инит. селф говорит что мы работаем именно с обьектом а не с классом
        self.make = make
        self.model = model
        self.year = year
        self.speed = None #ноне это заглушка, обязвательно сделать

        def __str__(self):
            return f"{self.year}, {self.model}, {self.year}"

class FastCar(Car):
    def __init__(self, make, model, year, speed):
        super().__init__(make, model,year) #круглые скобки всегда пустые
        self.speed = speed

        



my_car = Car('toyota', 'camry', 1990)#создание обьекта

print(my_car)
my_car.model= 'corolla' #ищменение обьекта
print(my_car.__str__)

'''

class A:
    def __init__(self):
        print("im class a")


class B:
    def __init__(self):
        print("im class b")


class C(A,B):
    def __init__(self):
        super().__init__()
        print("im class c")

c = C()
print(C.__mro__)



#можно сделать обертку в виде словаря с переданноым функции значением в виде ключс и результатом по этому ключи. типа чтобы удобно проверять повторные выполениния функции