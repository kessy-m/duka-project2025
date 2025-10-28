from flask import Flask,render_template,request,redirect,url_for
from database import fetch_data,insert_products

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

# add products route
@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method=='POST':
        pname=request.form['product_name']
        bp=request.form['buying_price']
        sp=request.form['selling_price']
        new_product=(pname,bp,sp)
        insert_products(new_product)
        return redirect(url_for('products'))
    return redirect(url_for('products'))

    



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


app.run(debug=True)

