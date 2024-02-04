-- Update the year published of a book
UPDATE books
SET year_published = '1865'
WHERE title = "Alice's Adventures in Wonderland";

-- Correct the last name of an author
UPDATE authors
SET last = 'Carroll'
WHERE first = 'Lewis';