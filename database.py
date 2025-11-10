import psycopg2

# connect to postgress database
connect=psycopg2.connect(
    host='localhost',
    user='postgres',
    port=5433,
    dbname='myduka_db',
    password='12345'
)

# declare cursor to connect to database
curr=connect.cursor()

# # fetch products
# curr.execute('select * from products;')
# prods=curr.fetchall()
# print(prods)
# prods

# # fetch sales
# curr.execute('select * from sales;')
# my_sales=curr.fetchall()
# print(my_sales)

# # fetch stock
# curr.execute('select * from stock;')
# my_stock=curr.fetchall()
# print(my_stock)




# task
# store in a function
def fetch_products():
    curr.execute('select * from products;')
    prods=curr.fetchall()
    return prods

# prods=fetch_products()
# print(prods)


def fetch_sales():
    curr.execute('select * from sales;')
    my_sales=curr.fetchall()
    return my_sales

# my_sales=fetch_sales()
# print(my_sales)


def fetch_stock():
    curr.execute('select * from stock;')
    my_stock=curr.fetchall()
    return my_stock

# my_stock=fetch_stock()
# print(my_stock)

# fetch data
# have one function the have parameters

def fetch_data(table_name):
    curr.execute(f'select * from {table_name}')
    data=curr.fetchall()
    return data

# call the speficic table
# products=fetch_data('products')
# print(products)

# sales=fetch_data('sales')
# print(sales)

# stock=fetch_data('stock')
# print(stock)



# insert products
# curr.execute("insert into products(name,buying_price,selling_price)values('Avocado',30.00,50.00);")
# connect.commit()

# products=fetch_data('products')
# print(products)

# insert products using a function
# def insert_products():
#     # curr.execute("insert into products(name,buying_price,selling_price)values('Delamere yoghurt',130.00,250.00);")
#     connect.commit()

# # call the functio then fetch data from  the products
# insert_products()
# products=fetch_data('products')
# print(products)

# insert products using place values remember to use a parameter
def insert_products(values):
    querry="insert into products(name,buying_price,selling_price)values(%s,%s,%s)"
    curr.execute(querry,values)
    connect.commit()

# new_product=('Baking powder',50.00,80.00)
# insert_products(new_product)
# products=fetch_data('products')
# print(products)


# # insert sales
def insert_sales(values):
    querry="insert into sales(pid,quantity,created_at)values(%s,%s,now())"
    curr.execute(querry,values)
    connect.commit()

# new_sale=(3,10)
# insert_sales(new_sale)
# products=fetch_data('sales')
# print(products)

# insert stock
def insert_stock(values):
    querry="insert into stock(pid,stock_quantity)values(%s,%s)"
    curr.execute(querry,values)
    connect.commit()

# new_stock=(2,15)
# insert_stock(new_stock)
# products=fetch_data('stock')
# print(stock)

# write a function to get:
# querry to get profit per product
def product_profit():
    querry=' select p.name,p.id,sum((p.selling_price-p.buying_price)*s.quantity) as ' \
    'total_profit from products as p join sales as s on p.id=s.pid group by p.name,p.id;'
    curr.execute(querry)
    profit=curr.fetchall()
    return profit

# my_profit=product_profit()
# print('these are my profit')
# print(my_profit)


# querry to get sales per product
def sales_product():
    querry= 'select p.name,p.id,sum(p.selling_price*s.quantity) as total_sales from products' \
    ' as p join sales as s on p.id=s.pid group by p.name,p.id;'
    curr.execute(querry)
    sales=curr.fetchall()
    return sales

# querry to get sales per day
def sales_per_day():
    querry=' select date(s.created_at)as day, sum(p.selling_price * s.quantity)as total_sales from sales as s ' \
    'join products as p on s.pid=p.id group by date(s.created_at) order by date(s.created_at);'
    curr.execute(querry)
    total_sales=curr.fetchall()
    return total_sales

# my_sales=sales_product()
# print('these are my sales')
# print(my_sales)

# query to get profit per day
def profit_per_day():
    querry='select date(s.created_at)as day, sum(p.selling_price - p.buying_price)as total_sales from products as p ' \
    'join sales as s on p.id=s.pid group by date(s.created_at) order by date(s.created_at);'
    curr.execute(querry)
    total_profit=curr.fetchall()
    return total_profit
# new_profit=profit_per_day()
# print(new_profit)



# function to get total sales
def total_sales():
    querry='select sum(selling_price*quantity) from products join sales on sales.pid=products.id;'
    curr.execute(querry)
    data=curr.fetchone()
    return data
print(total_sales())
