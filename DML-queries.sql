--Insert New Customer
INSERT INTO Customers (customer_first_name, customer_last_name, email, phone, premium, username, password) VALUES(:customer_first_name_input, :customer_last_name_input, :email_input, :phone_input, :amount_owed_input, :premium_input, :username_input, :password_input)

--Insert New Movies
INSERT INTO Movies(movie_title, director, genre, run_time, year, country, description) VALUES (:movie_title_input, :director_input, :genre_input, :run_time_input, :year_input, :country_input, :description_input)

--Insert New Book
INSERT INTO Books(title, author, genre, page_count, description, isbn) VALUES (:title_input, :author_input, :genre_input, :page_count_input, :description_input, :isbn_input)

--Insert New MovieTrackers
INSERT INTO MovieTrackers(wishlist_id, movie_id) VALUES ((SELECT wishilst_id FROM Wishlists WHERE wishlist_name = :wishlist_name_input AND customer_id = (SELECT customer_id FROM Customers where username = :username_input)), :movie_id_to_add)

--Insert New BookTrackers
INSERT INTO BookTrackers(wishlist_id, book_id) VALUES ((SELECT wishilst_id FROM Wishlists WHERE wishlist_name = :wishlist_name_input AND customer_id = (SELECT customer_id FROM Customers where username = :username_input)), :movie_id_to_add)

--Insert New Wishlists
INSERT INTO Wishlists (customer_id, wishlist_name) VALUES ((SELECT customer_id FROM Customers where username = :username_input), :wishlist_name_input)

--Delete Customers
DELETE FROM Customers WHERE customer_id= SELECT customer_id FROM Customers WHERE username = :username_input)

-- DELETE Movies
DELETE FROM Movies WHERE movie_id = :movie_id_selected

-- DELETE BookTrackers
DELETE FROM Books WHERE book_id = :book_id_selected

-- DELETE MovieTrackers
DELETE FROM MovieTrackers WHERE wishlist_id = :wishlist_id_selected_from_wishlist AND movie_id = :movie_id_selected_from_wishlist

-- DELETE BookTrackers
DELETE FROM BookTrackers WHERE wishlist_id = :wishlist_id_selected_from_wishlist AND book_id = :book_id_selected_from_wishlist

-- DELETE BookTrackers
DELETE FROM Wishlists WHERE wishlist_id = :wishlist_id_selected_by_user

-- Update Wishlist Name
UPDATE Wishlist SET wishlist_name = :new_wishlist_name WHERE wishlist_name = :wishlist_name_input AND customer_id = (SELECT customer_id FROM Customers where username = :username_input))

-- Search Books
SELECT title, author, genre, page_count FROM Books WHERE title = :book_title_input

-- Search Movies
SELECT title, author, genre, year, runtime FROM movies WHERE title = :movie_title_input

-- Search Username
SELECT customer_first_name, customer_last_name, email, phone FROM Customers WHERE username = :username_input

-- Wishlist display
SELECT title FROM Books INNER JOIN  ON WHERE book_id = (SELECT book_id FROM BookTrackers where wishlist_id = (SELECT wishlist_id FROM Wishlists WHERE (SELECT wishlist_id FROM Wishlists WHERE wishlist_name = :wishlist_selected AND customer_id = SELECT customer_id FROM Customers where username = :username_selected))
UNION
SELECT title FROM Movies INNER JOIN  ON WHERE movie_id = (SELECT movie_id FROM MovieTrackers where wishlist_id = (SELECT wishlist_id FROM Wishlists WHERE (SELECT wishlist_id FROM Wishlists WHERE wishlist_name = :wishlist_selected AND customer_id = SELECT customer_id FROM Customers where username = :username_selected))
