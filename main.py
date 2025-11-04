from flask import Flask,render_template,request,redirect,url_for
from database import fetch_data,insert_products,insert_sales,insert_stock,product_profit,sales_product,sales_per_day

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
    prods=fetch_data('products')
    # print(my_sales)
    return render_template('sales.html',sales_1=my_sales,prods_1=prods)


# add sales route
@app.route('/add_sales',methods=['GET','POST'])
def add_sales():
    if request.method=='POST':
        pid=request.form['product_id']
        quantity=request.form['quantity']
        new_sale=(pid,quantity)
        insert_sales(new_sale)
        return redirect(url_for('sales'))
    return redirect(url_for('sales'))



# stock route
@app.route('/stock')
def stock():
    my_stock=fetch_data('stock')
    my_products=fetch_data('products')
    # print(my_stock)
    return render_template('stock.html',stock_1=my_stock,prods_2=my_products)


# add stock route
@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method=='POST':
        prod_id=request.form['product_id']
        stock_quantity=request.form['s_quantity']
        new_stock=(prod_id,stock_quantity)
        insert_stock(new_stock)
        return redirect(url_for('stock'))
    return redirect(url_for('stock'))


#dashboard route
@app.route('/dashboard')
def dashboard():
    profits=product_profit()
    product_names=[]
    prod_profit=[]
    for i in profits:
        product_names.append(i[0])
        prod_profit.append(float(i[2]))

# sales per product
    all_sales=sales_product()
    sale_name=[]
    sale_product=[]
    for i in all_sales:
        sale_name.append(i[0])
        sale_product.append(float(i[2]))
        
# sales per day
    my_sales=sales_per_day() 
    # print(my_sales)
    dates=[]
    day_sales=[]
    for i in my_sales:
        dates.append(str(i[0]))
        day_sales.append(float(i[1]))

    return render_template('dashboard.html',p_name=product_names,p_profit=prod_profit,s_name=sale_name,
    s_product=sale_product,dates=dates,d_sales=day_sales)

   



app.run(debug=True)

