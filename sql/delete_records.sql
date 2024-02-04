-- Delete books by title
DELETE FROM books WHERE title IN ('The Outsiders', 'The Hobbit', 'Among the Hidden');

-- Delete discontinued movies
DELETE FROM books WHERE discontinued = 1;

-- Delete books with a rating below 5.0
DELETE FROM books WHERE rating < 5.0;