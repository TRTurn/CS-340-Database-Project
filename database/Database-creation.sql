DROP TABLE IF EXISTS `Books`;
CREATE TABLE Books(
    book_id INT AUTO_INCREMENT,
    isbn varchar(13) NOT NULL,
    author varchar(128) NOT NULL,
    title varchar(255) NOT NULL,
    genre varchar(13),
    page_count INT NOT NULL,

    UNIQUE(title, author),
    PRIMARY KEY (book_id)
   );

DROP TABLE IF EXISTS `Movies`;
CREATE TABLE Movies(
    movie_id INT AUTO_INCREMENT,
    movie_title varchar(255) NOT NULL,
    director varchar(128) NOT NULL,
    genre varchar(13) NOT NULL,
    run_time int NOT NULL,
    year INT NOT NULL,
    country varchar(3) NOT NULL,
    description text,
    UNIQUE (movie_title, director),
    PRIMARY KEY (movie_id)
    );

DROP TABLE IF EXISTS `Wishlists`;
CREATE TABLE Wishlists(
  wishlist_id int AUTO_INCREMENT,
  customer_id int,
  wishlist_name VARCHAR(36) NOT NULL,
  UNIQUE (customer_id, wishlist_name),
  PRIMARY KEY (wishlist_id)
);

DROP TABLE IF EXISTS `Customers`;
CREATE TABLE Customers(
    customer_id int AUTO_INCREMENT,
    customer_first_name varchar(64) NOT NULL,
    customer_last_name varchar(64),
    email varchar(128) NOT NULL,
    phone varchar(10) NOT NULL,
    amount_owed decimal,
    premium boolean NOT NULL,
    username varchar(32) NOT NULL,
    password varchar(32) NOT NULL,
    download_id INT,
    UNIQUE (username),
    PRIMARY KEY (customer_id),
    FOREIGN KEY (download_id) REFERENCES Wishlists(wishlist_id)
    );

ALTER TABLE Wishlists
ADD FOREIGN KEY (customer_id) REFERENCES Customers(customer_id);

DROP TABLE IF EXISTS `BookTrackers`;
CREATE TABLE BookTrackers(
  wishlist_id INT NOT NULL,
  book_id INT NOT NULL,
  PRIMARY KEY (wishlist_id, book_id),
  FOREIGN KEY (wishlist_id) REFERENCES Wishlists(wishlist_id),
  FOREIGN KEY (book_id) REFERENCES Books(book_id)
  );

DROP TABLE IF EXISTS `MovieTrackers`;
CREATE TABLE MovieTrackers(
  wishlist_id INT,
  movie_id INT,
  PRIMARY KEY (wishlist_id, movie_id),
  FOREIGN KEY (wishlist_id) REFERENCES Wishlists(wishlist_id),
  FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
);
