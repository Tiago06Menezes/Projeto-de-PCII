


# Class Product
# Import the generic class
from classes.gclass import Gclass
from classes.category import Category
class Product(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_product_name','_price','_category_id']
    # Class header title
    header = 'Product'
    # field description for use in, for example, input form
    des = ['Id','Product_Name','Price','Category_id']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, product_name, price, category_id):
        super().__init__()
        # Object attributes
        id = Product.get_id(id)
        self._id = id
        self._product_name = product_name
        self._price = float(price)
        self._category_id = int(category_id)
        if not Category.obj:  # Se a lista de categorias estiver vazia
            Category.read('data/ecommerce.db')  # Carregar categorias do banco de dados
        if int(category_id) not in Category.lst:
            print(f'Category {category_id} not found')
            return
        # Add the new object to the Product list
        Product.obj[id] = self
        Product.lst.append(id)
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    # name property getter method
    @property
    def product_name(self):
        return self._product_name
    # price property getter method
    @property
    def price(self):
        return self._price
    # price property setter method
    @price.setter
    def price(self, price):
        self._price = price
    # Adicionar getter/ para category_id:
    @property
    def category_id(self):
        return self._category_id
    
    @category_id.setter
    def category_id(self, category_id):
        self._category_id = int(category_id)
    