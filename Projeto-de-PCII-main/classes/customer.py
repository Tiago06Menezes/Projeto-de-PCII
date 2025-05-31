
# Class Customer_login
# Import the generic class
from classes.gclass import Gclass

class Customer(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_name','_email','_address']
    # Class header title
    header = 'Customers'
    # field description for use in, for example, input form
    des = ['Id','Name','Email','Address']
    # Constructor: Called when an object is instantiated
    def __init__(self,id,name,email,address):
        super().__init__()
        # Object attributes
        id = Customer.get_id(id)
        self._id = id
        self._name = name
        self._email = email
        self._address = address
        
        # Add the new object to the Customer's list
        Customer.obj[id] = self
        Customer.lst.append(id)
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    # name property getter method
    @property
    def name(self):
        return self._name
    # name property setter method
    @name.setter
    def name(self, name):
        self._name = name
    # address property getter method
    @property
    def address(self):
        return self._address
    # address property setter method
    @address.setter
    def address(self, address):
        self._address = address
    # email property getter method
    @property
    def email(self):
        return self._email
    # email property setter method
    @email.setter
    def email(self, email):
        self._email = email
