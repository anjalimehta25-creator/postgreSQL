CREATE DATABASE library_db;

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100)
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE loans (
    member_id INT REFERENCES members(id),
    book_id INT REFERENCES books(id)
);

INSERT INTO books (title, author)
VALUES
('Harry Potter', 'J.K. Rowling'),
('The Alchemist', 'Paulo Coelho'),
('Wings of Fire', 'A.P.J. Abdul Kalam'),
('Atomic Habits', 'James Clear');

INSERT INTO members (name)
VALUES
('Anjali'),
('Priya'),
('Rahul');

INSERT INTO loans (member_id, book_id)
VALUES
(1, 2),
(2, 1),
(1, 3);

SELECT * FROM books;

SELECT * FROM members;

SELECT * FROM loans;
