from flask import Flask, render_template, json
from flask import request, redirect
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
    query = "SELECT book_id, title, author, genre, page_count, description FROM Books;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("book-library.html", books=results)

@app.route('/add_book')
def render_books():
    return render_template('/add_book.html')

# Add book
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

# Delete Book Entry
@app.route('/delete-book/<id>')
def remove_book(id):
    query = "DELETE FROM Books WHERE book_id = %s" %(id)
    db.execute_query(db_connection, query)
    return redirect('/book-library')

# Update Book Entry
@app.route('/update-book/<id>', methods=['POST', 'GET'])
def update_book(id):
    db_connection = db.connect_to_database()
    if request.method == 'GET':
        book_query = 'SELECT * FROM Books WHERE book_id = %s' %(id)
        book_result = db.execute_query(db_connection, book_query).fetchone()
        return render_template('update-book.html', book=book_result)

        if book_result == None:
            return "No such movie found!"

    elif request.method == 'POST':
        print("Updated")
        book_id = request.form['book_id']
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        page_count = request.form['page_count']
        description = request.form['description']

        book_update_query = "UPDATE Books SET title = %s, author = %s, genre = %s, page_count = %s, description = %s WHERE book_id = %s"
        update_data = (title, author, genre, page_count, description, book_id)
        db.execute_query(db_connection, book_update_query, update_data)
        return redirect('/book-library')

@app.route('/search-books', methods = ['POST', 'GET'])
def search_books():
    title = request.form['book-search-query']
    query = "SELECT book_id, title, author, genre, page_count, description FROM Books WHERE title = %s" %("'" + title + "'")
    results = db.execute_query(db_connection, query).fetchall()
    return render_template("book-library.html", books=results)

###########################################
# MOVIES
###########################################
# Display Movie
@app.route('/movie-library')
def display_movies():
    query = "SELECT movie_id, movie_title, director, genre, run_time, year, description, rated, movie_id FROM Movies;"
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

# Delete Movie Entry
@app.route('/delete-movie/<id>')
def remove_movie(id):
    query = "DELETE FROM Movies where movie_id = %s" %(id)
    db.execute_query(db_connection, query)
    return redirect('/movie-library')

# Update Movie Entry
@app.route('/update-movie/<id>', methods=['POST', 'GET'])
def update_movie(id):
    db_connection = db.connect_to_database()
    if request.method == 'GET':
        movie_query = 'SELECT * FROM Movies WHERE movie_id = %s' %(id)
        movie_result = db.execute_query(db_connection, movie_query).fetchone()
        return render_template('update-movie.html', movie=movie_result)

        if movie_result == None:
            return "No such movie found!"

    elif request.method == 'POST':
        print("Updated")
        movie_id = request.form['movie_id']
        movie_title = request.form['movie_title']
        director = request.form['director']
        rated = request.form['rated']
        actor = request.form['actor']
        genre = request.form['genre']
        run_time = request.form['run_time']
        year = request.form['year']
        country = request.form['country']
        description = request.form['description']

        movie_update_query = "UPDATE movies SET movie_title = %s, director = %s, rated = %s, actor = %s, genre = %s, run_time = %s, year = %s, country = %s, description = %s WHERE movie_id = %s"
        update_data = (movie_title, director, rated, actor, genre, run_time, year, country, description, movie_id)
        db.execute_query(db_connection, movie_update_query, update_data)
        return redirect('/movie-library')

# Search Movie by title
@app.route('/search-movies', methods = ['POST', 'GET'])
def search_movies():
    title = request.form['movie_search_query']
    query = "SELECT movie_id, movie_title, director, genre, run_time, year, description, rated FROM Movies WHERE movie_title = %s" %("'" + title + "'")
    results = db.execute_query(db_connection, query).fetchall()
    print(results)
    return render_template("movie-library.html", movies=results)

#############################
# Customers
#############################
# Display Customer - library
@app.route('/customers-library')
def customers():
    query = "SELECT customer_id, customer_first_name, customer_last_name, email, phone, premium, username FROM customers;"
    cursor = db.execute_query(db_connection = db_connection, query=query)
    results = cursor.fetchall()
    return render_template("customers-library.html", customers=results)

# Add New Customers
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

# Delete Customer
@app.route('/delete-customer/<id>')
def remove_customer(id):
    query = "DELETE FROM Customers where customer_id = %s" %(id)
    db.execute_query(db_connection, query)
    return redirect('/customers-library')

# Update Customer Entry
@app.route('/update-customer/<id>', methods=['POST', 'GET'])
def update_customer(id):
    db_connection = db.connect_to_database()
    if request.method == 'GET':
        customer_query = 'SELECT * FROM Customers WHERE customer_id = %s' %(id)
        customer_result = db.execute_query(db_connection, customer_query).fetchone()
        return render_template('update-customer.html', customer=customer_result)

        if people_result == None:
            return "No such person found!"

    elif request.method == 'POST':
        print("Updated")
        customer_id = request.form['customer_id']
        customer_first_name = request.form['customer_first_name']
        customer_last_name = request.form['customer_last_name']
        email = request.form['email']
        phone = request.form['phone']
        premium = request.form['premium']
        username = request.form['username']
        password = request.form['password']

        customer_update_query = "UPDATE customers SET customer_first_name = %s, customer_last_name = %s, email = %s, phone = %s, premium = %s, username = %s, password = %s WHERE customer_id = %s"
        update_data = (customer_first_name, customer_last_name, email, phone, premium, username, password, customer_id)
        db.execute_query(db_connection, customer_update_query, update_data)
        return redirect('/customers-library')

# Search for Customers
@app.route('/search-customers', methods = ['POST', 'GET'])
def customer_search():
    customer_name = request.form['customer-search-query']
    query = "SELECT customer_id, customer_first_name, customer_last_name, email, phone, premium, username, password FROM Customers WHERE customer_first_name = %s or customer_last_name = %s " %("'" + customer_name + "'", "'" + customer_name + "'")
    results = db.execute_query(db_connection, query).fetchall()
    print(results)
    return render_template("customers-library.html", customers=results)

#############################
# Wishlists
#############################
@app.route('/wishlist-library')
def wishlists():
    query = "SELECT Wishlists.wishlist_id, Wishlists.wishlist_name, customers.username FROM Wishlists INNER JOIN Customers on Wishlists.customer_id = Customers.customer_id;"
    cursor = db.execute_query(db_connection = db_connection, query=query)
    results = cursor.fetchall()
    return render_template("wishlist-library.html", wishlists=results)

# Add New Wishlist
@app.route('/add-wishlist', methods=['POST', 'GET'])
def display_wishlist_creation():
    return render_template("/add-wishlist.html")

@app.route('/create-wishlist', methods=['POST', 'GET'])
def create_wishlist():
    wishlist_name = request.form['wishlist_name']
    username = request.form['username']
    query = "INSERT INTO Wishlists(customer_id, wishlist_name) VALUES ((SELECT customer_id FROM customers where username = %s), %s);"
    wishlist_data = (username, wishlist_name)
    db_connection = db.connect_to_database()
    db.execute_query(db_connection, query, wishlist_data)
    return render_template("add-wishlist.html")

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
@app.route('/index', methods = ["GET"])
def root():
    return render_template("index.html")

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
def display_books():
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
