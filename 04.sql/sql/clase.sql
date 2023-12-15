SELECT * FROM actor;
SELECT * FROM actor WHERE actor_id <5;
-- payment amount menores que 5 euros:
-- payment amount mayores que 10 euros:

SELECT * FROM payment WHERE amount < 10.99;
SELECT * FROM payment WHERE amount > 10;
SELECT * FROM payment WHERE amount >= 5 AND amount <= 10;
SELECT * FROM payment WHERE amount BETWEEN 5 AND 10; -- incluye 5 y 10
SELECT * FROM payment WHERE payment_date BETWEEN '2005-07-01' AND '2005-07-15';
SELECT * FROM address WHERE district = 'california';
SELECT * FROM address WHERE district = 'california' OR district = 'nagasaki';
SELECT * FROM address WHERE address LIKE '%Aurora' ; -- 0
SELECT * FROM address WHERE address LIKE '%Aurora%' ; -- 1
SELECT * FROM customer WHERE first_name LIKE 'A%' ; -- 44
SELECT * FROM customer WHERE email LIKE '%@gmail.com' ; 
SELECT * FROM customer WHERE email NOT LIKE '%@gmail.com' ;
SELECT * FROM customer WHERE email LIKE '%@sakilacustomer.org' ;

INSERT INTO customer (`store_id`, `first_name`, `last_name`, `email`, `address_id`) VALUES ('2', 'silvia', 'sanchez', 'silviasanchez@gmail.com', '605');


SELECT * FROM city;
SELECT * FROM country WHERE country = 'spain';
INSERT INTO city (city, country_id) VALUES('leon', 87 );
INSERT INTO city  VALUES (602,'madrid',87, '2023-01-01');

SELECT * FROM film;


SHOW COLUMNS FROM film;
Insert into film (title, languaje_id, rental_duration, rental_rate, replacement_cost) VALUES ('ejemplo title', 1, 5,2.99,18.99); 
-- INSERT manual de filas nuevas en la tabla staff
-- BLOB binary large Object se usa normalmente para guardar imagen, pdf, archivos
use Sakila;

SELECT * FROM staff;

SHOW COLUMNS FROM staff;
-- NULLABLE YES significa opcional, NULLABLE NO significa obligatorio
-- staff empleado
SELECT * FROM address;
SELECT * FROM store;


