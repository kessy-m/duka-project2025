from flask import Flask,render_template
from database import fetch_data

app=Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')


# products route
@app.route('/products')
def products():
    prods=fetch_data('products')
    # print(prods)
    return render_template('products.html',my_prods=prods)


# sales route
@app.route('/sales')
def sales():
    my_sales=fetch_data('sales')
    # print(my_sales)
    return render_template('sales.html',sales_1=my_sales)


# stock route
@app.route('/stock')
def stock():
    my_stock=fetch_data('stock')
    # print(my_stock)
    return render_template('stock.html',stock_1=my_stock)


app.run()

