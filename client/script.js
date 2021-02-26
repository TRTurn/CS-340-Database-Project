// URL OF server
let serverURL = "?";

let body = document.querySelector("body");

// dom elements for log in
let logOnButton = document.querySelector(".log-on-btn");
let userNameInput = document.querySelector(".user-name");
let userPassword = document.querySelector(".user-password");

// dom elements for registeration
let registerButton = document.querySelector(".register-btn");
let registerationFirstName = document.querySelector(".user-first-name");
let registerationLastName = document.querySelector(".user-last-name");
let email = document.querySelector(".email");
let phone = document.querySelector(".phone");
let regiserationUserName = document.querySelector(".user-name-registeration");
let regiserationPassword = document.querySelector(
  ".user-password-registeration"
);

// dom elements to add a book
let addBookButton = document.querySelector(".addBook-btn");
let bookTitle = document.querySelector(".book-title");
let bookAuthor = document.querySelector(".book-author");
let bookGenre = document.querySelector(".book-genre");
let bookPageCount = document.querySelector(".book-page-count");
let bookDescription = document.querySelector(".book-description");

// dom element to search for a book
let searchBookButton = document.querySelector(".search-btn-book");
let searchBookInput = document.querySelector(".book-search");

// dom elements to add a movie
let addMovieButton = document.querySelector(".addMovie-btn");
let movieTitle = document.querySelector(".movie-title");
let movieDirector = document.querySelector(".movie-director");
let movieRating = document.querySelector(".movie-rating");
let movieActors = document.querySelector(".movie-actors");
let movieGenre = document.querySelector(".movie-genre");
let movieRunTime = document.querySelector(".movie-runtime");
let movieYear = document.querySelector(".movie-year");
let movieCountry = document.querySelector(".movie-country");
let movieDescription = document.querySelector(".movie-description");

// dom element to search for a movie
let searchMovieButton = document.querySelector(".search-btn-movie");
let searchMovieInput = document.querySelector(".movie-search");

// dom element to create book wishlist
let createWishListButton = document.querySelector(
  ".create-book-wishlist-button"
);
let addToWishListButton = document.querySelector(".add-wishlist-book");
let wishListName = document.querySelector(".book-wishlist-name");

// dom element to create movie wishlist
let addToMovieWishListButton = document.querySelector(".add-wishlist-movie");
let movieWishListName = document.querySelector(".movie-wishlist-name");
let createMovieWishListButton = document.querySelector(
  ".create-movie-wishlist-button"
);

// dom element to create download

// for log in page, add click event for main page log in button
body.addEventListener("click", (event) => {
  if (event.target.className.includes("log-on-btn")) {
    event.preventDefault();
    // missing information for user log in, warn users.
    if (!validForm([userNameInput, userPassword])) {
      alert("Missing information. Pleae recheck the username and password!");
      return;
    }
    // create new ajax request
    let req = new XMLHttpRequest();

    // submit a get request to log in user (SELECT)
    let url = "?";

    req.open("GET", url, true);
    // set header for request
    req.setRequestHeader("Content-Type", "application/json");

    // set load event and store username in local storage for future wishlist creation
    req.addEventListener("load", function () {
      if (req.status >= 200 && req.status < 400) {
        // server sends back username, store this data into localStorage
        let data = JSON.parse(req.response);
        localStorage.removeItem("username");
        localStorage.setItem("username", data.username);
      } else {
        alert("Server side error, please try again.");
      }
    });

    // send data
    req.send(
      JSON.stringify({
        username: userNameInput.value,
        password: userPassword.value,
      })
    );
  }
});

// create a new user
body.addEventListener("click", (event) => {
  if (event.target.className.includes("register-btn")) {
    event.preventDefault();

    // missing information for registeration. Warn the user
    if (
      !validForm([
        registerationFirstName,
        registerationLastName,
        email,
        phone,
        regiserationUserName,
        regiserationPassword,
      ])
    ) {
      alert(
        "Missing an information for your registeration. Please recheck the form field!"
      );
      return;
    }

    // create new ajax request
    let req = new XMLHttpRequest();

    // submit a POST request to create user
    let url = "?";

    req.open("POST", url, true);

    // set header for request
    req.setRequestHeader("Content-Type", "application/json");

    // send data to server.
    // to create new customer: Need customer_first_name, customer_last_name, email, phone, premium, username, password
    req.send(
      JSON.stringify({
        customer_first_name: registerationFirstName.value,
        customer_last_name: registerationLastName.value,
        email: email.value,
        phone: phone.value,
        premium: true,
        username: regiserationUserName.value,
        password: regiserationPassword.value,
      })
    );
  }
});

// add a book
body.addEventListener("click", (event) => {
  if (event.target.className.includes("addBook-btn")) {
    event.preventDefault();

    // missing information for adding a book. Warn the user
    if (
      !validForm([
        bookTitle,
        bookAuthor,
        bookGenre,
        bookPageCount,
        bookDescription,
      ])
    ) {
      alert(
        "Missing an information for adding a book. Please fill in all the fields!"
      );
      return;
    }

    // create new ajax request
    let req = new XMLHttpRequest();

    // submit a POST request to add a book (CREATE)
    let url = "?";

    req.open("POST", url, true);

    // set header for request
    req.setRequestHeader("Content-Type", "application/json");

    // send data to server.
    // to create new book: Need title, author, genre, page_count, description
    req.send(
      JSON.stringify({
        title: bookTitle.value,
        author: bookAuthor.value,
        genre: bookGenre.value,
        page_count: bookPageCount.value,
        description: bookDescription.value,
      })
    );
  }
});

// search for a book by title
body.addEventListener("click", (event) => {
  if (event.target.className.includes("search-btn-book")) {
    event.preventDefault();

    // missing information for search query, warn users.
    if (!validForm([searchBookInput])) {
      alert("Search field is empty. Enter a book title please");
      return;
    }

    // create new ajax request
    let req = new XMLHttpRequest();

    // submit a GET request to search for books by title (SELECT)
    let url = "?";

    req.open("GET", url, true);

    // set header for request
    req.setRequestHeader("Content-Type", "application/json");

    // send data to server.
    req.send(
      JSON.stringify({
        book_title_input: searchBookInput.value,
      })
    );
  }
});

// add a movie
body.addEventListener("click", (event) => {
  if (event.target.className.includes("addMovie-btn")) {
    event.preventDefault();

    if (
      !validForm([
        movieTitle,
        movieDirector,
        movieRating,
        movieActors,
        movieGenre,
        movieRunTime,
        movieYear,
        movieCountry,
        movieDescription,
      ])
    ) {
      alert(
        "Missing an information for adding a Movie. Please fill in all the fields!"
      );
      return;
    }

    // create new ajax request
    let req = new XMLHttpRequest();

    // submit a POST request to add a book (CREATE)
    let url = "?";

    req.open("POST", url, true);

    // set header for request
    req.setRequestHeader("Content-Type", "application/json");

    // send data to server.
    // to create new movie: Need movie_title, director, rated, actor, genre, run_time, year, country, description
    req.send(
      JSON.stringify({
        movie_title: movieTitle.value,
        director: movieDirector.value,
        rated: movieRating.value,
        actor: movieActors.value,
        genre: movieGenre.value,
        run_time: parseInt(movieRunTime.value),
        year: parseInt(movieYear.value),
        country: movieCountry.value,
        description: movieDescription.value,
      })
    );
  }
});

// search for a movie by title
body.addEventListener("click", (event) => {
  if (event.target.className.includes("search-btn-movie")) {
    event.preventDefault();

    // missing information for search query, warn users.
    if (!validForm([searchMovieInput])) {
      alert("Search field is empty. Enter a movie title please");
      return;
    }

    // create new ajax request
    let req = new XMLHttpRequest();

    // submit a GET request to search for movies by title (SELECT)
    let url = "?";

    req.open("GET", url, true);

    // set header for request
    req.setRequestHeader("Content-Type", "application/json");

    // send data to server.
    req.send(
      JSON.stringify({
        movie_title_input: searchMovieInput.value,
      })
    );
  }
});

// add to wishlist for books
body.addEventListener("click", (event) => {
  if (event.target.className.includes("add-wishlist-book")) {
    // get id of book
    let bookId;
    for (let child of event.target.parentNode.children) {
      if (child.className.includes("book-id")) {
        bookId = child.firstElementChild.innerText;
      }
    }

    // nested call back
    body.addEventListener("click", (event) => {
      if (event.target.className.includes("create-book-wishlist-button")) {
        // missing information for wishlist creation, warn users.
        if (!validForm([wishListName])) {
          alert("Missing book Wishlist name!");
          return;
        }

        // create new ajax request
        let req = new XMLHttpRequest();

        // submit a POST request to create a wishlist (CREATE)
        let url = "?";

        req.open("POST", url, true);

        // set header for request
        req.setRequestHeader("Content-Type", "application/json");

        // set load event and warn user if wishlist already exists
        req.addEventListener("load", function () {
          if (req.status >= 200 && req.status < 400) {
            // server sends back error, wishlist name already exists
            let data = JSON.parse(req.response);
            if (data.error) {
              alert("This wishlist already exists!");
            }
          } else {
            alert("Server side error, please try again.");
          }
        });

        // send data to server. Send data to create wishlist and BookTracker (M:M)
        req.send(
          JSON.stringify({
            username_input: localStorage.getItem("username"),
            wishlist_name_input: wishListName.value,
            book: true,
            book_id_to_add: parseInt(bookId),
          })
        );
      }
    });
  }
});

// add to wishlist for movies
body.addEventListener("click", (event) => {
  if (event.target.className.includes("add-wishlist-movie")) {
    // get id of movie
    let movieId;
    for (let child of event.target.parentNode.children) {
      if (child.className.includes("movie-id")) {
        movieId = child.firstElementChild.innerText;
      }
    }

    // nested call back
    body.addEventListener("click", (event) => {
      if (event.target.className.includes("create-movie-wishlist-button")) {
        // missing information for wishlist creation, warn users.
        if (!validForm([movieWishListName])) {
          alert("Missing movie Wishlist name!");
          return;
        }

        // create new ajax request
        let req = new XMLHttpRequest();

        // submit a POST request to create a Movie wishlist (CREATE)
        let url = "?";

        req.open("POST", url, true);

        // set header for request
        req.setRequestHeader("Content-Type", "application/json");

        // set load event and warn user if wishlist already exists
        req.addEventListener("load", function () {
          if (req.status >= 200 && req.status < 400) {
            // server sends back error, wishlist name already exists
            let data = JSON.parse(req.response);
            if (data.error) {
              alert("This wishlist already exists!");
            }
          } else {
            alert("Server side error, please try again.");
          }
        });

        // send data to server. Send data to create wishlist and MovieTracker (M:M)
        req.send(
          JSON.stringify({
            username_input: localStorage.getItem("username"),
            wishlist_name_input: movieWishListName.value,
            movie: true,
            movie_id_to_add: parseInt(movieId),
          })
        );
      }
    });
  }
});

// add to downloads
body.addEventListener("click", (event) => {
  if (event.target.className.includes("download")) {
    let movieId;
    let bookId;

    // get movieId or bookId depending on url page.
    for (let child of event.target.parentNode.children) {
      if (
        child.className.includes("movie-id") &&
        window.location.href.includes("movies")
      ) {
        movieId = child.firstElementChild.innerText;
      } else if (
        child.className.includes("book-id") &&
        window.location.href.includes("books")
      ) {
        bookId = child.firstElementChild.innerText;
      }
    }

    // create new ajax request
    let req = new XMLHttpRequest();

    // submit a POST request to create a download wishlist (CREATE)
    let url = "?";

    req.open("POST", url, true);

    // set header for request
    req.setRequestHeader("Content-Type", "application/json");

    // send data to server. based on book or movie. This will go to the M:M tracker either MovieTracker or BookTracker
    if (movieId) {
      req.send(
        JSON.stringify({
          username_input: localStorage.getItem("username"),
          movie: true,
          movie_id_to_add: parseInt(movieId),
          wishlist_name: "Downloads",
        })
      );
    } else {
      req.send(
        JSON.stringify({
          username_input: localStorage.getItem("username"),
          book: true,
          book_id_to_add: parseInt(bookId),
          wishlist_name: "Downloads",
        })
      );
    }
  }
});

// form validation
function validForm(args) {
  // any field requirements in argument that is blank will be invalid
  for (const data of args) {
    if (data.value === "") {
      return false;
    }
  }
  return true;
}
