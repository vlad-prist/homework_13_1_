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
        self.goods = []

        Category.count_category += 1 #при создании экземлпяра, счетчик увеличивается на 1

    def list_goods(self, good):
        ''' Метод добавления товаров в список'''
        self.goods.append(good)

    def __repr__(self):
        return f'Наименование: {self.name}, Описание: {self.description}, Список позиций: {self.goods}'



class Product:
    name: str
    description: str
    price: float
    amount: int
    count_product = 0 #Счетчик количества продуктов (экземпляров, не остатка)

    def __init__(self, name, description, price, quantity):
        '''Инициализация по заданию. Атрибуты экземпляра: наименование, описание, цена, остаток'''
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product.count_product += 1 #при создании экземлпяра, счетчик увеличивается на 1

    def __repr__(self):
        return f'Наименование: {self.name}, Описание: {self.description}, Список позиций: {self.price}/ Остаток: {self.quantity}'



# ct1 = Category('Phones', 'mobile')
# ct1.list_goods('iPhone')
# ct1.list_goods('Samsung')
#
# ct2 = Category('Laptops', 'mini computers')
# ct2.list_goods('iPhone')
# ct2.list_goods('Samsung')
# print(ct1)
# print(ct2)
# print(Category.count_category)
#
# pr1 = Product('iPhone', 'smth', 100_000, 3)
# pr2 = Product('Samsung', 'smth', 90_000, 2)
# print(pr1)
# print(pr2)
# print(Product.count_product)