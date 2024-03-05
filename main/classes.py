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


    def add_goods(self, good):
        ''' Метод добавления товаров в список'''
        self.__goods.append(good)

    @property
    def display(self):
        '''Данный метод позволяет принтом вывести список товаров'''
        return self.__goods

    @property
    def counting_goods(self):
        return len(self.__goods)


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
        '''Класс-метод по добавлению новых товаров'''
        return cls(**new_product)


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


def printing():
    '''Метод проверки корректности методов классов'''

    # Экземпляр класса Category
    ct1 = Category('Phones', 'mobile')

    # Экземпляр класса Product
    pr2 = Product('Samsung', 'smth', 90_000, 2)

    # Проверка по заданию 1. Добавление продекта в приватный список товаров
    ct1.add_goods(pr2)

    # Проверка по заданию 1. Отобращение приватного списка товаров
    print(ct1.display)

    # Проверка по заданию 1. Количество уникальных товаров в приватном списке
    print(ct1.counting_goods)

    # Проверка по заданию 2. Получение перечня товаров определнным форматом
    print(ct1.get_format)

    # Экземпляр класса Product
    pr1 = Product('iPhone', 'smth', 100_000, 3)

    #Создание словаря для дальнейшего добавления в экземпляры класса
    pr3 = {
        'name': 'Nokia',
        'description': 'smth',
        'price': 1000,
        'quantity': 10
    }

    new_pr3 = Product.launch_product(pr3) #Проверка по заданию 3

    # Проверка по заданию 3. Вывод добавленного словаря
    print(new_pr3)

    # Проверка на корректность ценыпо заданию 4. Переопределение цены первого экземпляра.
    pr1.price = 0

    # Проверка по заданию 4. Вывод первоначальной цены экземпляра
    print(pr1.price)

if __name__ == '__main__':
    printing()

