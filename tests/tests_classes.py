import pytest
from main.classes import Category, Product

@pytest.fixture()
def category_phones():
    '''тестируем класс Category'''
    ct1 = Category('Phones', 'mobile phones')
    return ct1

def test_init(category_phones):
    '''Тестируем метод init'''
    assert category_phones.name == 'Phones'
    assert category_phones.description == 'mobile phones'
    assert category_phones.goods == []

def test_list_goods(category_phones):
    '''тестируем добавление товаров в список, проверяем данные товар в списке'''
    good = 'iphone'
    category_phones.list_goods(good)
    assert good in category_phones.goods

def test_count_cat(category_phones):
    '''тест кол-ва категорий'''
    category_phones.count_category = 2
    assert category_phones.count_category == 2

@pytest.fixture()
def product_iphone():
    '''тест класса Product'''
    pr1 = Product('iPhone', 'the most expensive phone', 110_000, 3)
    return pr1

def test_init_pr(product_iphone):
    '''инициализируем обект класса через тест'''
    assert product_iphone.name == 'iPhone'
    assert product_iphone.description == 'the most expensive phone'
    assert product_iphone.price == 110_000
    assert product_iphone.quantity == 3

def test_count_prod(product_iphone):
    '''считаем кол-во объектов эксземплярор класса'''
    product_iphone.count_product = 2
    assert product_iphone.count_product == 2






