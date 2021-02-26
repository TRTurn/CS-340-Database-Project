from flask import Flask, render_template, json
from flask import request
import os
import database.db_connector as db


app = Flask(__name__)


# Routes (Maybe dictate which page? Think handlebars?)
@app.route('/', methods = ["GET"])
def root():
    data = request.get_json()
    print(data)
    return render_template("main.j2")

@app.route('/customers')
def customers():
    # Write a query and save it as a variable
    query = "SELECT * FROM customers;"

    cursor = db.execute_query(db_connection = db_connection, query=query)

    results = json.dumps(cursor.fetchall())
    return results

@app.route('/register', methods = ['POST', 'GET'])
def add_new_customer():
    print("Adding new customer")
    customer_first_name = request.form['customer_first_name']
    customer_last_name = request.form['customer_last_name']
    email = request.form['email']
    phone = request.form['phone']
    premium = request.form['premium']
    username = request.form['username']
    password = request.form['password']

    query = 'INSERT INTO Customers(customer_first_name, customer_last_name, email, phone, premium, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    customer_data = (customer_first_name, customer_last_name, email, phone, premium, username, password)
    db_connection = connect_to_database()
    execute_query(db_connection, query, customer_data)

    return render_template('customers.j2')

@app.route('/add_book', methods = ['POST', 'GET'])
def add_new_book():
    print("Adding new book")
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    pages = request.form['pages']
    description = request.form['description']

    query = 'INSERT INTO Books(title, author, genre, page_count, description) VALUES (%s, %s, %s, %s, %s)'
    book_data = (title, author, genre, pages, description)
    db_connection = connect_to_database()
    execute_query = (db_connection, query, book_data)
    return render_template('add_book.j2')

@app.route('/add_movie', methods = ['POST', 'GET'])
def add_new_movie():
    print("Adding new movie")
    title = request.form['title']
    director = request.form['director']
    rated = request.form['rated']
    actors = request.form['actors']
    genre = request.form['genre']
    runtime = request.form['runtime']
    year = request.form['year']
    country = request.form['country']
    description = request.form['description']

    query = 'INSERT INTO Movies(movie_title, director, rated, actor, genre, run_time, year, country, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    movie_data = (title, director, rated, actors, genre, runtime, year, country, description)
    db_connection = connect_to_database()
    execute_query = (db_connection, query, book_data)
    return render_template('add_movie.j2')

@app.route('/wishlist', methods = ['POST', 'GET'])
def add_wishlist():
    print('Adding wishlist')
    username = request.form['username']
    wishlist_name = request.form['wishlist_name']
    # Username -> customer_id + wishlist name
    username_query = 'SELECT customer_id FROM customers WHERE username = %s'
    db_connection = connect_to_database()
    execute_query = (db_connection, username_query, username)

@app.route('/fill', methods = ['POST', 'GET'])
def add_book_tracker():
    pass

@app.route('/fill')
def add_movie_tracker():
    pass



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112)) # 9112 can be any port
    db_connection = db.connect_to_database()
    app.run(port=port, debug=True)
