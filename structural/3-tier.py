#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*TL;DR80
Separates presentation, application processing, and data management functions.

* 一句话总结
分离表现层，应用逻辑，数据管理功能。
"""


class Data(object):
    """ 数据存储类 """

    products = {
        'milk': {'price': 1.50, 'quantity': 10},
        'eggs': {'price': 0.20, 'quantity': 100},
        'cheese': {'price': 2.00, 'quantity': 10}
    }

    def __get__(self, obj, klas):
        print("(Fetching from Data Store)")
        return {'products': self.products}


class BusinessLogic(object):
    """ 业务逻辑包含了数据存储实例 """

    data = Data()

    def product_list(self):
        return self.data['products'].keys()

    def product_information(self, product):
        return self.data['products'].get(product, None)


class Ui(object):
    """ UI 交互类 """

    def __init__(self):
        self.business_logic = BusinessLogic()

    def get_product_list(self):
        print('PRODUCT LIST:')
        for product in self.business_logic.product_list():
            print(product)
        print('')

    def get_product_information(self, product):
        product_info = self.business_logic.product_information(product)
        if product_info:
            print('PRODUCT INFORMATION:')
            print('Name: {0}, Price: {1:.2f}, Quantity: {2:}'.format(
                product.title(), product_info.get('price', 0),
                product_info.get('quantity', 0)))
        else:
            print('That product "{0}" does not exist in the records'.format(
                product))


def main():
    ui = Ui()
    ui.get_product_list()
    ui.get_product_information('cheese')
    ui.get_product_information('eggs')
    ui.get_product_information('milk')
    ui.get_product_information('arepas')

if __name__ == '__main__':
    main()

### OUTPUT ###
# PRODUCT LIST:
# (Fetching from Data Store)
# cheese
# eggs
# milk
#
# (Fetching from Data Store)
# PRODUCT INFORMATION:
# Name: Cheese, Price: 2.00, Quantity: 10
# (Fetching from Data Store)
# PRODUCT INFORMATION:
# Name: Eggs, Price: 0.20, Quantity: 100
# (Fetching from Data Store)
# PRODUCT INFORMATION:
# Name: Milk, Price: 1.50, Quantity: 10
# (Fetching from Data Store)
# That product "arepas" does not exist in the records
