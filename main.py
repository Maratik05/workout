from flask import Flask, render_template, url_for

 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)





