from flask import Flask, render_template, url_for, request
import sqlite3


 
app = Flask(__name__)

def create_table():
    con = sqlite3.connect('products.db')
    cursor = con.cursor()
    # cursor.execute('''DROP TABLE news;''')
    cursor.execute('''
CREATE TABLE IF NOT EXISTS news(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    watch_brands VARCHAR,
    price INTEGER,
    water_resistance VARCHAR,
    quality VARCHAR
) ''')
    con.commit()
    cursor.close()
    con.close()




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    if request.method == 'GET':
        return render_template('products.html')
    else:
        con = sqlite3.connect('products.db')
        cursor = con.cursor()
        query = cursor.execute('''INSERT INTO news(watch_brands,price,water_resistance,quality) VALUES(?,?,?,?)''')
        query_data = (request.form.get('brand'), request.form.get('price'), request.form.get('water_resistance'), request.form.get('quality'))
        cursor.execute(query,query_data)
        con.commit()
        cursor.close()
        con.close() 
        return 'Форма заполнена успешно.'
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
    create_table()
    app.run(debug=True, port=8000)





