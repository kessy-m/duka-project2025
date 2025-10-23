from flask import Flask

app=Flask(__name__)



@app.route('/')
def home():
    return 'my home page'


# products route
@app.route('/products')
def products():
    return 'My products page'


# sales route
@app.route('/sales')
def sales():
    return 'My sales page'


# stock route
@app.route('/stock')
def stock():
    return 'My stock page'


app.run()

