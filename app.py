from flask import Flask, render_template, json
from flask import request, redirect
import os
import database.db_connector as db


app = Flask(__name__)

#######################################
# Homepage
#######################################
@app.route('/index', methods = ["GET"])
def root():
    return render_template("index.html")

#######################################
# books
#######################################
# Display books
@app.route('/book-library')
def book():
    query = "SELECT book_id, title, author, genre, page_count, description FROM books;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("book-library.html", books=results)

@app.route('/add_book')
def render_books():
    return render_template('/add_book.html')

# Add book
@app.route('/add_a_book', methods=['POST', 'GET'])
def add_books():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    page_count = request.form['page_count']
    description = request.form['description']
    query = 'INSERT INTO books(title, author, genre, page_count, description) VALUES (%s, %s, %s, %s, %s)'
    book_data = (title, author, genre, page_count, description)
    db_connection = db.connect_to_database()
    db.execute_query(db_connection, query, book_data)
    return render_template('/add_book.html')

# Delete Book Entry
@app.route('/delete-book/<id>')
def remove_book(id):
    query = "DELETE FROM books WHERE book_id = %s" %(id)
    db.execute_query(db_connection, query)
    return redirect('/book-library')

# Update Book Entry
@app.route('/update-book/<id>', methods=['POST', 'GET'])
def update_book(id):
    db_connection = db.connect_to_database()
    if request.method == 'GET':
        book_query = 'SELECT * FROM books WHERE book_id = %s' %(id)
        book_result = db.execute_query(db_connection, book_query).fetchone()
        return render_template('update-book.html', book=book_result)

        if book_result == None:
            return "No such movie found!"

    elif request.method == 'POST':
        book_id = request.form['book_id']
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        page_count = request.form['page_count']
        description = request.form['description']

        book_update_query = "UPDATE books SET title = %s, author = %s, genre = %s, page_count = %s, description = %s WHERE book_id = %s"
        update_data = (title, author, genre, page_count, description, book_id)
        db.execute_query(db_connection, book_update_query, update_data)
        return redirect('/book-library')

@app.route('/search-books', methods = ['POST', 'GET'])
def search_books():
    title = request.form['book-search-query']
    query = "SELECT book_id, title, author, genre, page_count, description FROM books WHERE title = %s" %("'" + title + "'")
    results = db.execute_query(db_connection, query).fetchall()
    return render_template("book-library.html", books=results)

###########################################
# Movies
###########################################
# Display Movie
@app.route('/movie-library')
def display_movies():
    query = "SELECT movie_id, movie_title, director, genre, run_time, year, description, rated, movie_id FROM movies;"
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
    title = request.form['movie_title']
    director = request.form['director']
    rated = request.form['rated']
    actors = request.form['actor']
    genre = request.form['genre']
    runtime = request.form['run_time']
    year = request.form['year']
    country = request.form['country']
    description = request.form['description']
    query = 'INSERT INTO movies(movie_title, director, rated, actor, genre, run_time, year, country, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    movie_data = (title, director, rated, actors, genre, runtime, year, country, description)
    db_connection = db.connect_to_database()
    db.execute_query(db_connection, query, movie_data)
    return render_template('add_movie.html')

# Delete Movie Entry
@app.route('/delete-movie/<id>')
def remove_movie(id):
    query = "DELETE FROM movies where movie_id = %s" %(id)
    db.execute_query(db_connection, query)
    return redirect('/movie-library')

# Update Movie Entry
@app.route('/update-movie/<id>', methods=['POST', 'GET'])
def update_movie(id):
    db_connection = db.connect_to_database()
    if request.method == 'GET':
        movie_query = 'SELECT * FROM movies WHERE movie_id = %s' %(id)
        movie_result = db.execute_query(db_connection, movie_query).fetchone()
        return render_template('update-movie.html', movie=movie_result)

        if movie_result == None:
            return "No such movie found!"

    elif request.method == 'POST':
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
    query = "SELECT movie_id, movie_title, director, genre, run_time, year, description, rated FROM movies WHERE movie_title = %s" %("'" + title + "'")
    results = db.execute_query(db_connection, query).fetchall()
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

# Add New customers
@app.route('/register-customer', methods=['POST', 'GET'])
def display_registration():
    return render_template("/register-customer.html")

@app.route('/add-customer', methods=['POST', 'GET'])
def add_new_customer():
    customer_first_name = request.form['customer_first_name']
    customer_last_name = request.form['customer_last_name']
    email = request.form['email']
    phone = request.form['phone']
    premium = request.form['premium']
    username = request.form['username']
    password = request.form['password']

    query = 'INSERT INTO customers(customer_first_name, customer_last_name, email, phone, premium, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s);'
    customer_data = (customer_first_name, customer_last_name, email, phone, premium, username, password)
    db_connection = db.connect_to_database()
    db.execute_query(db_connection, query, customer_data)
    return render_template('register-customer.html')

# Delete Customer
@app.route('/delete-customer/<id>')
def remove_customer(id):
    query = "DELETE FROM customers where customer_id = %s;" %(id)
    db.execute_query(db_connection, query)
    return redirect('/customers-library')

# Update Customer Entry
@app.route('/update-customer/<id>', methods=['POST', 'GET'])
def update_customer(id):
    db_connection = db.connect_to_database()
    if request.method == 'GET':
        customer_query = 'SELECT * FROM customers WHERE customer_id = %s' %(id)
        customer_result = db.execute_query(db_connection, customer_query).fetchone()
        return render_template('update-customer.html', customer=customer_result)

        if people_result == None:
            return "No such person found!"

    elif request.method == 'POST':
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

# Search for customers
@app.route('/search-customers', methods = ['POST', 'GET'])
def customer_search():
    customer_name = request.form['customer-search-query']
    query = "SELECT customer_id, customer_first_name, customer_last_name, email, phone, premium, username, password FROM customers WHERE customer_first_name = %s or customer_last_name = %s " %("'" + customer_name + "'", "'" + customer_name + "'")
    results = db.execute_query(db_connection, query).fetchall()
    return render_template("customers-library.html", customers=results)

#############################
# Wishlists
#############################
@app.route('/wishlist-library')
def wishlists():
    query = "SELECT wishlists.wishlist_id, wishlists.wishlist_name, customers.username FROM wishlists INNER JOIN customers on wishlists.customer_id = customers.customer_id;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
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
    query = "INSERT INTO wishlists(customer_id, wishlist_name) VALUES ((SELECT customer_id FROM customers where username = %s), %s);"
    wishlist_data = (username, wishlist_name)
    db_connection = db.connect_to_database()
    db.execute_query(db_connection, query, wishlist_data)
    return render_template("add-wishlist.html")

# Delete Wishlist
@app.route('/delete-wishlist/<id>')
def delete_wishlist(id):
    query = "DELETE FROM wishlists WHERE wishlist_id = %s" %(id)
    db.execute_query(db_connection, query)
    return redirect('/wishlist-library')

# Search Wishlist
@app.route('/search-wishlist', methods=['POST','GET'])
def search_wishlist():
    username = request.form['wishlist-search-query']
    query = "SELECT wishlists.wishlist_id, wishlists.wishlist_name, customers.username FROM wishlists INNER JOIN customers on wishlists.customer_id = customers.customer_id WHERE customers.username = %s" %("'" + username + "'")
    wishlist_data = (username)
    results = db.execute_query(db_connection, query).fetchall()
    return render_template("wishlist-library.html", wishlists=results)

@app.route('/view-wishlist/<id>', methods = ['POST', 'GET'])
def view_wishlist(id):
    movie_query = "SELECT movies.movie_title, movies.director FROM movietrackers INNER JOIN movies on movietrackers.movie_id = movies.movie_id WHERE wishlist_id = %s;" %(id)
    book_query = "SELECT books.title, books.author FROM booktrackers INNER JOIN books on booktrackers.book_id = books.book_id WHERE wishlist_id = %s;" %(id)
    wishlist_name_query = "SELECT wishlist_name FROM wishlists WHERE wishlist_id = %s" %(id)
    books = db.execute_query(db_connection, book_query).fetchall()
    movies = db.execute_query(db_connection, movie_query).fetchall()
    wishlist_name = db.execute_query(db_connection, wishlist_name_query).fetchall()
    return render_template("view-wishlist.html", wishlist=wishlist_name, books=books, movies=movies, wishlist_id=id)

@app.route('/add-booktracker', methods=['POST', 'GET'])
def add_booktracker():
    wishlist_id = request.form['wishlist_id']
    title = request.form['book-title']
    author = request.form['author']
    book_query = "INSERT INTO booktrackers(wishlist_id, book_id) VALUES ((SELECT wishlist_id FROM wishlists where wishlist_id = %s), (SELECT book_id FROM books WHERE title = %s AND author = %s));"
    query_data = (wishlist_id, title, author)
    db_connection = db.connect_to_database()
    db.execute_query(db_connection, book_query, query_data)
    return redirect("/wishlist-library")

@app.route('/add-movietracker', methods=['POST', 'GET'])
def add_movietracker():
    wishlist_id = request.form['wishlist_id']
    title = request.form['movie_title']
    director = request.form['director']
    movie_query = "INSERT INTO movietrackers(wishlist_id, movie_id) VALUES ((SELECT wishlist_id FROM wishlists where wishlist_id = %s), (SELECT movie_id FROM movies WHERE movie_title = %s AND director = %s));"
    query_data = (wishlist_id, title, director)
    db_connection = db.connect_to_database()
    db.execute_query(db_connection, movie_query, query_data)
    return redirect("/wishlist-library")

@app.route('/remove-movietracker/<id>')
def remove_movietracker(id, movie_id):
    query = "DELETE FROM movietrackers WHERE wishlist_id = %s AND movie_id = %s" %(id, movie_id)
    db.execute_query(db_connection, query)
    return redirect('/wishlist-library')

@app.route('/remove-booktracker/<id>')
def remove_booktracker(id, book_id):
    query = "DELETE FROM booktrackers WHERE wishlist_id = %s AND book_id = %s" %(id, book_id)
    db.execute_query(db_connection, query)
    return redirect('/wishlist-library')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 2000)) # 9112 can be any port
    db_connection = db.connect_to_database()
    app.run(port=port, debug=True)
