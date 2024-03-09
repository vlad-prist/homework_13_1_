from classes import Category, Product


class CategoryIter:
    def __init__(self, category: Category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.category.display):
            raise StopIteration
        else:
            product = self.category.display[self.index]
            self.index += 1
            return product


category = Category('Fruits', 'seasonal fruits')
product1 = Product('Apple', 'sour', 100, 10)
product2 = Product('Pear', 'sweet', 200, 2)
product3 = Product('Plum', 'sweet', 300, 1)

category.append_goods(product1)
category.append_goods(product2)
category.append_goods(product3)

category_iter = CategoryIter(category)

for fruit in category_iter:
    print(fruit)
