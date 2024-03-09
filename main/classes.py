class Category:
    name: str
    description: str
    goods: list
    count_category = 0 #Счетчик общего количества категорий
    unique_product = 0 #Общее количество уникальных продуктов

    def __init__(self, name, description):
        '''Инициализация по заданию. Атрибуты экземпляра: название, описание.
        Товары передаются списком через метод добавления.'''
        self.name = name
        self.description = description
        self.__goods = [] #Список товаров сделали приватным
        Category.count_category += 1 #при создании экземлпяра, счетчик увеличивается на 1

    def append_goods(self, good):
        '''
         Метод добавления товаров в список
        также данный метод считает итоговое количество всех продуктов в сумме
        '''
        self.__goods.append(good)
        Category.unique_product += good.quantity

    @property
    def display(self):
        '''Данный метод позволяет принтом вывести приватный список товаров'''
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

    def __len__(self):
        '''Вывод количества продуктов на складе'''
        return len(self.__goods)

    def __str__(self):
        '''Добавлено строковое отображение'''
        return f'Название категории: {self.name}, количество продуктов: {Category.unique_product} шт.'


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        '''Инициализация по заданию. Атрибуты экземпляра: наименование, описание, цена, остаток'''
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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

    def __repr__(self):
        return f'{self.name}, {self.description}, {self.__price}, {self.quantity}'

    def __str__(self):
        '''Добавлено строковое отображение'''
        return f'Название продукта: {self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        ''' Метод сложения объектов (сложением сумм, умноженных на количество на складе).'''
        # return Product(name='',
        #                description='',
        #                price=self.price+other.price,
        #                quantity=self.quantity+other.quantity)
        return (self.price * self.quantity) + (other.price * other.quantity)


def printing():
    '''Метод проверки корректности методов классов'''

    category_1 = Category('Телефоны', 'мобильные телефоны') #Экземпляр класса Category
    product_1 = Product('Samsung', 'smth', 90_000, 2)
    product_2 = Product('iPhone', 'smth', 100_000, 3) #Экземпляр класса Product
    category_1.append_goods(product_1) #Добавление продукта в приватный список товаров
    category_1.append_goods(product_2)
    #print(ct1.display) #Отображение приватного списка товаров
    print(f'Уникальных продуктов: {category_1.unique_product}') #Количество уникальных товаров в приватном списке
    print(f'Вывод длины: {len(category_1)}')
    print(category_1.get_format) #Получение перечня товаров определнным форматом
    print(str(category_1)) #Отображение строкового представления

   #Создание словаря для дальнейшего добавления в экземпляры класса
    new_product_3 = {
        'name': 'Nokia',
        'description': 'smth',
        'price': 1000,
        'quantity': 10
    }

    product_3 = Product.launch_product(new_product_3) #Добавление нового продукта
    print(product_3) #Вывод добавленного словаря
    #pr1.price = 0 #Переопределение цены первого экземпляра.
    #print(pr1.price) #Вывод первоначальной цены экземпляра
    print(product_1)
    print(product_2)
    print(f'Метод add для 2х экземпляров класса Product: {product_1 + product_2}')



if __name__ == '__main__':
    printing()


