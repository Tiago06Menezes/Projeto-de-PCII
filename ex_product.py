
from classes.product import Product
from classes.category import Category 
test_class = Product
ob = '135;official;462;2'
db = 'ecommerce.db'


import datetime

#Reads the test_class.csv file
Product.read('data/'+ db)
Category.read('data/'+ db)
op = ''
while op != 'q':
    print('')
    print('Choose one letter for select the option')
    print('---------------')
    print('l - list')
    print('b - beginning')
    print('n - next')
    print('p - previous')
    print('e - end')
    print('---------------')
    print('i - insert')
    print('m - modify')
    print('r - remove')
    print('---------------')
    print('s - sort by attribute')
    print('f - find by attribute')
    print('---------------')
    print('q - quit')
    print('---------------')
    p = test_class.current()
    print(f'\n{p}')
    op = input('?')
    if op == 'b':
        test_class.first()
    elif op == 'n':
        test_class.nextrec()
    elif op == 'p':
        test_class.previous()
    elif op == 'e':
        test_class.last()
    elif op == 'i':
        # Cria um objeto temporário para obter os atributos se a lista estiver vazia
        if len(test_class.lst) == 0:
            p_temp = test_class.from_string(ob)
            str_list = list(p_temp.__dict__.keys())
            test_class.lst = []  # Limpa a lista temporária
        else:
            p = test_class.current()
            str_list = list(p.__dict__.keys())
    
        # Coleta os dados do novo produto
        print('Deixe em branco para auto-incrementar')
        values = []
        for attrib in str_list:
            field_name = attrib[1:]  # Remove o underscore (ex: '_id' vira 'id')
            value = input(f"{field_name} = ")
            
            # Trata campos numéricos
            if field_name in ['id', 'price', 'category_id']:
                value = int(value) if value else 0
            values.append(str(value))

        # Cria a string no formato "id;product_name;price;category_id"
        new_product = ";".join(values)
        
        # Insere o produto
        product = test_class.from_string(new_product)
        test_class.insert(product.id)
        print("Produto inserido com sucesso!")

    elif op == 'm':
        str_list = list(p.__dict__.keys())
        attrib = str_list[0]
        id = input(f'Record {attrib[1:]} = ') 
        if id != "":
            id = int(id)
            obj=test_class.current(id)
            print('Leave blank or new value to modify')
            for attrib in str_list[1:]:
                # attrib = str_list[i]
                value = input(f'{attrib[1:]} = ') 
                if value != "":
                    atype = type(getattr(p, attrib))
                    if atype == datetime.date:
                        setattr(obj, attrib, datetime.date.fromisoformat(value))
                    else:
                        setattr(obj, attrib, atype(value))
        # id = getattr(obj, test_class.att[0][1:])
        test_class.update(id)
    elif op == 'r':
        str_list = list(p.__dict__.keys())
        attrib = str_list[0]
        atype = type(getattr(p, attrib))
        cod = atype(input(f'{attrib[1:]} = '))
        if cod in test_class.lst:
            print(test_class.obj[cod])
            print('Confirm that you want to delete the record (y/n)?', end='')
            if input().upper() == 'Y':
                test_class.remove(cod)
    elif op == 'l':
        for code in test_class.lst:
            print(test_class.obj[code])
    elif op == 's':
        # Sort products by attribute in ascending order
        attrib = input('sort by attribute name:')
        if '_' + attrib in list(p.__dict__.keys()):
            reverse = False
            if input('Reverse (False):'):
                reverse = True
            codep = p.id         # Keep the position
            test_class.sort(attrib, reverse)
            for code in test_class.lst:
                print(test_class.obj[code])
            test_class.current(codep)
    elif op == 'f':
        # Find objects with a given value in an attribute
        attrib = input('Attribute name:')
        if '_' + attrib in list(p.__dict__.keys()):
            atype = type(getattr(p, attrib))
            value = atype(input('Value:'))
            fobjs = test_class.find(value, attrib)
            if len(fobjs) > 0:
                test_class.current(fobjs[0].id)
                for obj in fobjs:
                    print(obj)

