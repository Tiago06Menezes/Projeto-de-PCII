from flask import render_template, session
from classes.product import Product 
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

def apps_plotly():
    engine = create_engine('sqlite:///' + filename + 'trabalho.db')
    df_orderproduct = pd.read_sql('OrderProduct', con=engine)
    result = df_orderproduct.groupby('products_id')['quantity'].sum().reset_index()
    result = pd.DataFrame(result)
    fig = px.bar(result, x='quantity',y='products_id',title="Quantidade por Produto", color_discrete_sequence=['purple'])

    fig.update_layout(xaxis_title="quantidade",yaxis_title="id",title_text=" Total de unidades vendidas")
    barras = fig.to_html(full_html=False, div_id='my-plot1')
    
    engine = create_engine('sqlite:///' + filename + 'trabalho.db')
    df_product = pd.read_sql('Product', con=engine)
    r = df_product.groupby('category_id')['price'].sum().reset_index()
    circulo = px.pie(r,values='price', names='category_id',title='Preço total por Categoria')

    circulo = circulo.to_html(full_html=False, div_id='my-plot2')
    return render_template("plotly.html", plot1=barras, plot2=circulo, ulogin=session.get("user"))
