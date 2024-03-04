class Category:
    name: str
    description: str
    goods: list

    count_category = 0 #Счетчик количества категорий

    def __init__(self, name, description):
        '''Инициализация по заданию. Атрибуты экземпляра: название, описание.
        Товары передаются списком через метод добавления.'''
        self.name = name
        self.description = description
        self.__goods = [] #Список товаров сделали приватным

        Category.count_category += 1 #при создании экземлпяра, счетчик увеличивается на 1


    def list_goods(self, good):
        ''' Метод добавления товаров в список'''
        self.__goods.append(good)


    def __repr__(self):
        return f'{self.name}, {self.description}, {self.__goods}'


    @property
    def get_format(self):
        '''добавлен геттер для вывода необходимого формата'''
        result = ''
        for good in self.__goods:
            result += f'{good.name}, {good.price} руб. Остаток: {good.quantity} шт.\n'
        return result



class Product:
    name: str
    description: str
    price: float
    quantity: int
    count_product = 0 #Счетчик количества продуктов (экземпляров, не остатка)


    def __init__(self, name, description, price, quantity):
        '''Инициализация по заданию. Атрибуты экземпляра: наименование, описание, цена, остаток'''
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.count_product += 1 #при создании экземлпяра, счетчик увеличивается на 1


    def __repr__(self):
        return f'{self.name}, {self.description}, {self.__price}, {self.quantity}'


    @classmethod
    def launch_product(cls, new_product):
        '''Метод по добавлению новых товаров'''
        name, price, description, quantity = new_product.split(',')
        return cls(name, price, description, quantity)


    @property
    def price(self):
        '''геттер - установка цены'''
        return self.__price


    @price.setter
    def price(self, new_price):
        '''сеттер - условие, если цена <= 0, то вывод сообщения, иначе вывод заданной цены'''
        if new_price <= 0:
            print('Введена некорректная цена')
        else:
            self.__price = new_price



ct1 = Category('Phones', 'mobile')
pr2 = Product('Samsung', 'smth', 90_000, 2)
ct1.list_goods(pr2) #Проверка по заданию 2
print(ct1.get_format) #Проверка по заданию 2

pr1 = Product('iPhone', 'smth', 100_000, 3)
pr3 = 'Nokia, smth, 1000, 10' #Проверка по заданию 3
new_pr3 = Product.launch_product(pr3) #Проверка по заданию 3
print(new_pr3) #Проверка по заданию 3

pr1.price = 0 #Проверка по заданию 4
print(pr1.price) #Проверка по заданию 4



