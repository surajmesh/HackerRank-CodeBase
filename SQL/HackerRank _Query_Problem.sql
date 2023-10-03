-- create database :

CREATE DATABASE practise_db;   
USE practise_db;

-- crate table :
CREATE TABLE city (
id int PRIMARY KEY,
name VARCHAR(17),
countrycode VARCHAR(3),
district VARCHAR(20),
population INT
);

-- add values in columns :
INSERT INTO city (id,name,countrycode,district,population)
VALUES 
	(6, 'Rotterdam', 'NLD', 'Zuid-Holland', 593321),
    (3878, 'Scottsdale', 'USA', 'Arizona', 202705),
    (3965, 'Corona', 'USA', 'California', 124966),
    (3973, 'Concord', 'USA', 'California', 121780),
    (3977, 'Cedar Rapids', 'USA', 'Iowa', 120758),
    (3982, 'Coral Springs', 'USA', 'Florida', 117549),
    (4054, 'Fairfield', 'USA', 'California', 92256),
    (4058, 'Boulder', 'USA', 'Colorado', 91238),
    (4061, 'Fall River', 'USA', 'Massachusetts', 90555);
    
SELECT * FROM CITY;

-- Query all columns for a city in CITY with the ID 4061.:

SELECT * FROM city 
WHERE id = 4061;

-- query all columns and get even ID from table :
SELECT * FROM city 
WHERE id % 2 =0 ;

-- query all columns and get odd ID from table :
SELECT * FROM city 
WHERE ID % 2 <> 0;

-- Query a list of district names from city for distric that have an even ID number. Print the results in any order, but exclude duplicates from the answer.:

-- drop uplicate and print distinct country code name
SELECT DISTINCT countrycode FROM city
WHERE id % 2 = 0 ;

-- to get difference between total record of id and number of distinct of name :
SELECT count(id) - COUNT(DISTINCT NAME) FROM city ;

-- Query the list of NAME names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates. :

SELECT DISTINCT district FROM city 
WHERE district REGEXP('a','e','i','o','u') ;



