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
         Метод добавления товаров в список. Если товар не относится к наследникам, то выводится ошибка
        также данный метод считает итоговое количество всех продуктов в сумме
        '''
        Category.unique_product += good.quantity

        if not issubclass(good.__class__, (SmartPhones, LawnGrass)):
            raise TypeError('Продукт не соответсвует классу')
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


class SmartPhones(Product):
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

    def __str__(self):
        ''' Строковое представление экз.класса SmartPhones'''
        return f'Бренд: {self.name}, модель: {self.model}.\nОбъем памяти: {self.memory} ГБ. Цвет: {self.color}'

    def __add__(self, other):
        ''' Суммирование объектов только одного класса, в случае, если объект иного класса - вывод ошибки '''
        if isinstance(other, SmartPhones): #(other, type(self)) можно еще так записать
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise ValueError("Товары из разных классов продуктов")

class LawnGrass(Product):
    country: str #страна-производитель
    period: int #срок прорастания
    color: str

    def __init__(self, name, description, price, quantity, country, period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.period = period
        self.color = color

    def __str__(self):
        ''' Строковое представление экз.класса LawnGrass'''
        return (f'{self.name},'
                f' страна-производитель: {self.country}.\nCрок прорастания: {self.period} дней. Цвет: {self.color}')

    def __add__(self, other):
        ''' Суммирование объектов только одного класса, в случае, если объект иного класса - вывод ошибки '''
        if not isinstance(other, LawnGrass):
            raise ValueError("Товары из разных классов продуктов")
        return (self.price * self.quantity) + (other.price * other.quantity)



def printing():
    '''Метод проверки корректности методов классов'''

    category_1 = Category('Телефоны', 'мобильные телефоны') #Экземпляр класса Category

   #Создание словаря для дальнейшего добавления в экземпляры класса
    new_product_3 = {
        'name': 'Nokia',
        'description': 'smth',
        'price': 1000,
        'quantity': 10
    }
    product_3 = Product.launch_product(new_product_3) #Добавление нового продукта

    phone_1 = SmartPhones('LG', 'smartphone', 20732, 3, 1120.00, 'V50',
                       512,'Black')
    phone_2 = SmartPhones('Motorola', 'Раскладушка', 2823.50, 3, 516, 'V3',
                       8, 'Black')
    print(phone_1) #строковое отображение экз.класса SmartPhone
    print(f'Общая сумма категории "Смартфон": {phone_1+phone_2}')

    grass_1 = LawnGrass('Премиум-газон', 'Премиум', 1000, 3, 'Россия',
                     13, 'green')

    grass_2 = LawnGrass('Газон дачный', 'Эконом', 200, 10, 'Россия',
                     10, 'light-green')

    print(grass_1) #строковое отображение экз.класса LawnGrass
    print(f'Общая сумма категории "Трава газонна": {grass_1 + grass_2}')
    category_1.append_goods(phone_2) #Проверка, что обновленный метод append_goods работает корректно
    print(category_1.get_format) #Вывод на печать категории, с добавленным новым продуктом

if __name__ == '__main__':
    printing()


