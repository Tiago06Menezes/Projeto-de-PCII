
# Class OrderProduct
from classes.customerorder import CustomerOrder
from classes.product import Product
# Import the generic class
from classes.gclass import Gclass

class OrderProduct(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier id, attribute must be the first on the list
    att = ['_id', '_order_id','_product_id','_quantity','_price_line']
    # Class header title
    header = 'OrderProduct'
    # field description for use in, for example, input form
    des = ['Id','Order_id','Product_id','Quantity','Price_line']
    # Constructor: Called when an object is instantiated
    def __init__(self,id,order_id, product_id, quantity, price_line ):
        super().__init__()
        # Object attributes
        id = CustomerOrder.get_id(id)
        self._id = id
        self._order_id=order_id
        self._product_id=product_id
        self._quantity=quantity
        self._price_line = price_line


        # Add the new object to the Customer's list
        OrderProduct.obj[id] = self
        OrderProduct.lst.append(id)


    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    # order property getter method
    @property
    def order_id(self):
        return self._order_id
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
    # price property getter method
    @property
    def price_line(self):
        return self._price_line
    # price property setter method
    @price_line.setter
    def price_line(self, price):
        self._price_line = float(price)


#print(OrderProduct.lst)  # Deve retornar IDs de orders existentes
#print(Product.lst)  # Deve retornar IDs de produtos existentes
