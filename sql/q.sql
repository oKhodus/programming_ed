SELECT city, COUNT(*) AS user_count
FROM users
GROUP BY city;

SELECT * FROM users
LIMIT 3; 


SELECT name, age from users as youngest_person
ORDER by age asc limit 1;

SELECT DISTINCT city from users;

SELECT avg(age) from users;