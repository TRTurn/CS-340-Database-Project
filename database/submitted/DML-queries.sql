--Display customers
SELECT customer_id, customer_first_name, customer_last_name, email, phone, premium, username FROM customers;

-- Add Customer
INSERT INTO customers(customer_first_name, customer_last_name, email, phone, premium, username, password) VALUES (:customer_first_name, :customer_last_name, :email, :phone, :premium, :username, :password);

-- Delete Customer
DELETE FROM customers where customer_id = :customer_id;

-- Update Customer
UPDATE customers SET customer_first_name = :customer_first_name, customer_last_name = :customer_last_name, email = :email, phone = :phone, premium = :premium, username = :username, password = :password WHERE customer_id = :customer_id);

-- Search Customers
SELECT customer_id, customer_first_name, customer_last_name, email, phone, premium, username, password FROM customers WHERE customer_first_name = :customer_first_name or customer_last_name = customer_last_name;

-- Display books
SELECT book_id, title, author, genre, page_count, description FROM books;

-- Insert Books
INSERT INTO books(title, author, genre, page_count, description) VALUES (title, author, genre, page_count, description);

-- Delete Books
DELETE FROM books WHERE book_id = :book_id;

-- Update Book
UPDATE books SET title = :title, author = :author, genre = :genre, page_count = :page_count, description = :description WHERE book_id = :book_id;

-- Search Books
SELECT book_id, title, author, genre, page_count, description FROM books WHERE title = :title;

--Display Movies
SELECT movie_id, movie_title, director, genre, run_time, year, description, rated, movie_id FROM movies;

-- Add Movie
INSERT INTO movies(movie_title, director, rated, actor, genre, run_time, year, country, description) VALUES (:title, :director, :rated, :actors, :genre, :runtime, :year, :country, :description);

-- Delete Movies
DELETE FROM movies where movie_id = :movie_id;

-- Search Movies
SELECT movie_id, movie_title, director, genre, run_time, year, description, rated FROM movies WHERE movie_title = :movie_title;

-- Update Movies
UPDATE movies SET movie_title = :movie_title, director = :director, rated = :rated, actor = :actor, genre = :genre, run_time = :run_time, year = :year, country = :country, description = :description WHERE movie_id = :movie_id;

-- Display Wishlists
SELECT wishlists.wishlist_id, wishlists.wishlist_name, customers.username FROM wishlists INNER JOIN customers on wishlists.customer_id = customers.customer_id;

-- Add Wishlist
INSERT INTO wishlists(customer_id, wishlist_name) VALUES ((SELECT customer_id FROM customers where username = :username), :wishlist_name);

-- Delete Wishlist
DELETE FROM wishlists WHERE wishlist_id = :wishlist_id;

-- Search Wishlists
SELECT wishlists.wishlist_id, wishlists.wishlist_name, customers.username FROM wishlists INNER JOIN customers on wishlists.customer_id = customers.customer_id WHERE customers.username = :username;

-- View Wishlist Contents
SELECT movies.movie_title, movies.director FROM movietrackers INNER JOIN movies on movietrackers.movie_id = movies.movie_id WHERE wishlist_id = wishlist_id;
SELECT books.title, books.author FROM booktrackers INNER JOIN books on booktrackers.book_id = books.book_id WHERE wishlist_id = :wishlist_id;
SELECT wishlist_name FROM wishlists WHERE wishlist_id = :wishlist_id;

-- Insert Book Tracker
INSERT INTO booktrackers(wishlist_id, book_id) VALUES ((SELECT wishlist_id FROM wishlists where wishlist_id = :wishlist_id), (SELECT book_id FROM books WHERE title = :title AND author = :author));

-- Insert Movie Tracker
INSERT INTO movietrackers(wishlist_id, movie_id) VALUES ((SELECT wishlist_id FROM wishlists where wishlist_id = :wishlist_id), (SELECT movie_id FROM movies WHERE movie_title = :movie_title AND director = :director));

-- Delete Movietracker
DELETE FROM movietrackers WHERE wishlist_id = :wishlist_id AND movie_id = :movie_id;

-- Delete booktracker
DELETE FROM booktrackers WHERE wishlist_id = :wishlist_id AND book_id = :movie_id;
