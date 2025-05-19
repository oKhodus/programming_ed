SELECT city, COUNT(*) AS user_count
FROM users
GROUP BY city;

SELECT * FROM users
LIMIT 3; 

SELECT name, age from users as youngest_person
ORDER by age asc limit 1;

SELECT DISTINCT city from users;

SELECT avg(age) from users;

SELECT name from users
WHERE age = 22 OR age = 28;

SELECT name FROM users
WHERE name LIKE "A%";

SELECT name FROM users
WHERE (city = "Tallinn" or city = "Tartu") and age < 30;

SELECT name, city from users
ORDER by age desc;

SELECT name from users
WHERE name like "%i%";

SELECT name FROM users
WHERE not city like "Narva";

SELECT name, age FROM users
WHERE age BETWEEN 20 and 30;

SELECT name, city from users
WHERE name like "%e";

SELECT count(name) as users_number from users;

SELECT name from users
WHERE name like "_____";