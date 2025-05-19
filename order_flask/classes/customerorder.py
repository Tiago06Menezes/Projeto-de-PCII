
from classes.customer import Customer
from classes.gclass import Gclass
import datetime

class CustomerOrder(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    
    # Atributos da classe (o primeiro deve ser sempre o identificador '_id')
    att = ['_id', '_customer_id']
    
    # Cabeçalho para impressão
    header = 'CustomerOrder'
    
    # Descrição dos atributos para UI
    des = ['Id', 'Customer ID']
    
    def __init__(self,id,customer_id):
        super().__init__()
        # Object attributes
        id = CustomerOrder.get_id(id)
        self._id = id
        self._customer_id = customer_id
       
        
    
        CustomerOrder.obj[id] = self
        CustomerOrder.lst.append(id)

    # Property getters
    @property
    def id(self):
        return self._id

    @property
    def customer_id(self):
        return self._customer_id

    # Property setters
    @customer_id.setter
    def customer_id(self, customer_id):
        self._customer_id=customer_id
        