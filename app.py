from flask import Flask, render_template, json
from flask import request
import os
import database.db_connector as db


app = Flask(__name__)

#######################################
# Working
#######################################

#######################################
# BOOKS
#######################################

# Display Books
@app.route('/book-library')
def book():
    query = "SELECT title, author, genre, page_count, description FROM Books;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("book-library.html", books=results)

# Render page
@app.route('/add_book')
def render_books():
    return render_template('/add_book.html')

# Adds book to database
@app.route('/add_a_book', methods=['POST', 'GET'])
def add_books():
    print("Adding new book")
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    page_count = request.form['page_count']
    description = request.form['description']
    query = 'INSERT INTO Books(title, author, genre, page_count, description) VALUES (%s, %s, %s, %s, %s)'
    book_data = (title, author, genre, page_count, description)
    db_connection = db.connect_to_database()
    db.execute_query(db_connection, query, book_data)
    return render_template('/add_book.html')

###########################################
# MOVIES
###########################################

# Display Movie

@app.route('/movie-library')
def display_movies():
    query = "SELECT movie_title, director, genre, run_time, year, description, rated, movie_id FROM Movies;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("movie-library.html", movies=results)

# Render page
@app.route('/add_movie', methods = ['POST', 'GET'])
def add_new_movie():
    return render_template('add_movie.html')

# Add movie
@app.route('/add_a_movie', methods=['POST', 'GET'])
def add_new_movies():
    print("Adding new movie")
    title = request.form['movie_title']
    director = request.form['director']
    rated = request.form['rated']
    actors = request.form['actor']
    genre = request.form['genre']
    runtime = request.form['run_time']
    year = request.form['year']
    country = request.form['country']
    description = request.form['description']
    query = 'INSERT INTO Movies(movie_title, director, rated, actor, genre, run_time, year, country, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    movie_data = (title, director, rated, actors, genre, runtime, year, country, description)
    db_connection = db.connect_to_database()
    db.execute_query(db_connection, query, movie_data)
    return render_template('add_movie.html')

# Delete Movie
@app.route('/delete_movie', methods = ['POST', 'GET'])
def delete_move():
    query = 'DELETE FROM Movies WHERE movie_id = %s'
#############################
# Customers
#############################

# Display Customer
@app.route('/customers-library')
def customers():
    # Write a query and save it as a variable
    query = "SELECT customer_first_name, customer_last_name, email, phone, premium, username FROM customers;"
    cursor = db.execute_query(db_connection = db_connection, query=query)
    results = cursor.fetchall()
    return render_template("customers-library.html", customers=results)

@app.route('/register-customer', methods=['POST', 'GET'])
def display_registration():
    return render_template("/register-customer.html")

@app.route('/add-customer', methods=['POST', 'GET'])
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
    db_connection = db.connect_to_database()
    db.execute_query(db_connection, query, customer_data)
    return render_template('register-customer.html')

#############
# End Working
#############

#########
# Testing
#########



###### END TESTING #####


###############
# Old defaults
###############
# Routes (Maybe dictate which page? Think handlebars?)
@app.route('/', methods = ["GET"])
def root():
    data = request.get_json()
    print(data)
    return render_template("index.html")


@app.route('/search-movies', methods = ['POST', 'GET'])
def search_movies():
    title = request.form['movie_title']
    query = f"SELECT movie_title, director, genre, run_time, year, description, rated FROM Movies WHERE movie_title like % {title} %;"
    cursor = db.execute_query(title, db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("movie-library.html", movies=results)





# Books
@app.route('/add_book', methods = ['POST', 'GET'])
def add_new_books():
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
    return render_template('add_book.html')

@app.route('/display_book', methods = ['POST', 'GET'])
def search_books():
    query = "SELECT title, author, description FROM Books WHERE title = %s"
    title = request.form['title']
    result = execute_query(db_connection, query).fetchall()
    return render_template('books.html')




# Wishlists
@app.route('/wishlist', methods = ['POST', 'GET'])
def add_wishlist():
    print('Adding wishlist')
    username = request.form['username']
    wishlist_name = request.form['wishlist_name']
    # Username -> customer_id + wishlist name
    username_query = 'SELECT customer_id FROM customers WHERE username = %s'
    db_connection = connect_to_database()
    execute_query = (db_connection, username_query, username)
    return render_template('wishlist.html')

@app.route('/fill', methods = ['POST', 'GET'])
def add_book_tracker():
    wishlist_name = request.form['wishlist_name']
    query = 'INSERT INTO BookTrackers(wishlist_id, book_id) VALUES ((SELECT wishlist_id FROM Wishlists WHERE wishlist_name = :wishlist_name_input AND customer_id = (SELECT customer_id FROM Customers where username = :username_input)), :movie_id_to_add)'

if __name__ == "__main__":
    @app.route('/wishlist')
    def add_movie_tracker():
        username = request.form['username']
        wishlist_name = request.form['wishlist_name']
        query = 'INSERT INTO MovieTrackers(wishlist_id, movie_id) VALUES (%s AND customer_id = %s), :movie_id_to_add)'
        wishlist_id = 'SELECT wishlist_id FROM WishLists WHERE wishlist name=%s and customer_id = %s'
        customer_id_query = 'SELECT customer_id FROM Customers where username = %s'

    if __name__ == "__main__":
        port = int(os.environ.get('PORT', 2000)) # 9112 can be any port
        db_connection = db.connect_to_database()
        app.run(port=port, debug=True)
