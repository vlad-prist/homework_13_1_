import json
from classes import Category, Product


def main():
    # распаковываем файл json
    with open('products.json', encoding='utf-8') as file:
        datas = json.load(file)

    # создаем экземпляры класса Category
    for category in datas:
        categories = Category(category['name'], category['description'])
        category_goods = []

        # выводим на печать информацию об экземпляре класса Category
        print(f'Наименование: {categories.name}.\nОписание: {categories.description}.')

        # Создаем экземпляры класса Product
        for product in category["products"]:
            products = Product(product['name'], product['description'], product['price'], product['quantity'])
            category_goods.append(products)

            # выводим на печать информацию об экземпляре класса Product
            print(f'''Модель: {products.name}, Характеристики: {products.description}, 
Цена: {products.price}, Остаток: {products.quantity}''')

        print(f'Всего позиций в категории: {len(category_goods)}')

    print(f'Всего категорий: {Category.count_category}')
    print(f'Всего товаров: {Product.count_product}')

if __name__ == "__main__":
    main()
