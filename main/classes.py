from abc import ABC, abstractmethod

class BaseProduct(ABC):
    ''' Абстрактный базовый класс, для выделения общего функционала  между классами '''

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


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
        self.__goods = []
        Category.count_category += 1 #при создании экземлпяра, счетчик увеличивается на 1

    def append_goods(self, good):
        '''
        Метод добавления товаров в список с условиями:
        1. Также данный метод считает итоговое количество всех продуктов.
        2. Если товар не относится к наследникам, то выводится ошибка.
        3. Если количество товара равно нулю, то выводится ошибка.
        '''
        Category.unique_product += good.quantity

        if not issubclass(good.__class__, (SmartPhones, LawnGrass)):
            raise TypeError('Продукт не соответсвует классу')
        elif good.quantity == 0:
            raise ZeroQuantity('Товар с нулевым количеством не может быть добавлен')
        self.__goods.append(good)

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

    def average_sum(self):
        ''' Метод, который подсчитывает средний ценник всех товаров.
        Если в Категории не передан ни один товар, возвращает 0 '''
        try:
            total_sum = 0
            for good in self.__goods:
                total_sum += good.price
            average_sum = total_sum / len(self.__goods)
            return average_sum
        except ZeroDivisionError:
            return 0


class ZeroQuantity(Exception):
    ''' класс исключения, который отвечает за обработку событий,
    когда в «Категорию» добавляется товар с нулевым количеством '''
    def __init__(self, message="Ошибка количества"):
        self.message = message
        super().__init__(message)


class MixinRepr:
    ''' Миксин, который можно добавить к каждому классу для вывода информации в консоль о том, что был создан объект.'''

    def __init__(self, *args, **kwargs):
        # print(repr(self))
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} {self.__dict__.items()}"


class Product(MixinRepr, BaseProduct):

    def __init__(self, name: str, description: str, price: float, quantity: int):
        '''Инициализация по заданию. Атрибуты экземпляра: наименование, описание, цена, остаток'''
        super().__init__()
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
        super().__repr__()

    def __str__(self):
        '''Строковое отображение'''
        return f'Название продукта: {self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        ''' Метод сложения объектов (сложением сумм, умноженных на количество на складе).'''
        return (self.price * self.quantity) + (other.price * other.quantity)


class SmartPhones(Product, MixinRepr):
    capacity: float #производтельность (измеряется в герцах)
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, capacity, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.capacity = capacity
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        ''' Суммирование объектов только одного класса, в случае, если объект иного класса - вывод ошибки '''
        if isinstance(other, SmartPhones): #(other, type(self)) можно еще так записать
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise ValueError("Товары из разных классов продуктов")
    
    def __repr__(self):
        super().__repr__()


class LawnGrass(Product, MixinRepr):
    country: str #страна-производитель
    period: int #срок прорастания
    color: str

    def __init__(self, name, description, price, quantity, country, period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.period = period
        self.color = color

    def __add__(self, other):
        ''' Суммирование объектов только одного класса, в случае, если объект иного класса - вывод ошибки '''
        if not isinstance(other, LawnGrass):
            raise ValueError("Товары из разных классов продуктов")
        return (self.price * self.quantity) + (other.price * other.quantity)

    def __repr__(self):
        super().__repr__()


def printing():
    '''Метод проверки корректности методов классов'''

    category_1 = Category('Телефоны', 'мобильные телефоны')

    phone_1 = SmartPhones('LG', 'smartphone', 20732, 1, 1120.00, 'V50',
                       512,'Black')
    phone_2 = SmartPhones('Motorola', 'Раскладушка', 2823.50, 1, 516, 'V3',
                       8, 'Black')

    category_1.append_goods(phone_1)
    category_1.append_goods(phone_2)
    # print(category_1.average_sum())
    # print(category_1.__len__())

    try:
        category_2 = Category('Газонная трава', 'трава для сада')
        grass_1 = LawnGrass('Премиум-газон', 'Премиум', 1000, 0, 'Россия',
                     13, 'green')
        category_2.append_goods(grass_1)
    except ZeroQuantity:
        print("Добавляется товар с нулевым количеством")
    else:
        print("Товар добавлен")
    finally:
        print("Обработка добавления товара завершена")


if __name__ == '__main__':
    printing()


