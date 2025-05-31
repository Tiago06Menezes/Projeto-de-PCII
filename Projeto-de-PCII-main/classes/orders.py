# -*- coding: utf-8 -*-
"""
Created on Mon May 12 14:39:51 2025

@author: ACER
"""

# Class OrderProduct
from classes.customer import Customer
from classes.product import Product
# Import the generic class
from classes.gclass import Gclass

class Orders(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier id, attribute must be the first on the list
    att = ['_id', '_customer_id','_product_id','_quantity']
    # Class header title
    header = 'OrderProduct'
    # field description for use in, for example, input form
    des = ['Id','Customer_id','Product_id','Quantity']
    # Constructor: Called when an object is instantiated
    def __init__(self,id,customer_id, product_id, quantity):
        super().__init__()
        # Object attributes
        customer_id=int(customer_id)
        product_id=int(product_id)
        if customer_id in Customer.lst:
            if product_id in Product.lst:
                id = Customer.get_id(id)
                self._id = id
                self._customer_id=customer_id
                self._product_id=product_id
                self._quantity=quantity 
                Orders.obj[id] = self
                Orders.lst.append(id)
            else:
                print('Product ', product_id, ' not found')
        else:
            print('Customer ', customer_id, ' not found')

         
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    # order property getter method
    @property
    def order_id(self):
        return self._order_id
    @property
    def customer_id(self):
        return self._customer_id
    # product property getter method
    @property
    def product_id(self):
        return self._product_id
    # quantity property getter method
    @property
    def quantity(self):
        return self._quantity
    # quantity property setter method
    @quantity.setter
    def quantity(self, quantity):
        self._quantity = float(quantity)
    


# # print(Order.lst)  # Deve retornar IDs de orders existentes
# print(Product.lst)  # Deve retornar IDs de produtos existentes