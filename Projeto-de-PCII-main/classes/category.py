
# Import the generic class
from classes.gclass import Gclass

class Category(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id', '_category_name']
    # Class header title
    header = 'Category'
    # field description for use in, for example, input form
    des = ['Id', 'Category Name']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, category_name):
        super().__init__()
        # Object attributes
        id = Category.get_id(id)
        self._id = id
        self._category_name = category_name
        
        # Add the new object to the Category list
        Category.obj[id] = self
        Category.lst.append(id)
    
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    
    # category_name property getter method
    @property
    def category_name(self):
        return self._category_name
    
    # category_name property setter method
    @category_name.setter
    def category_name(self, category_name):
        self._category_name = category_name