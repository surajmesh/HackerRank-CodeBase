CREATE DATABASE mydatabase_1 ;
USE mydatabase_1;
CREATE TABLE accounts(
id INT PRIMARY KEY,
mac VARCHAR(255)
);
INSERT INTO accounts VALUES(1,"A7-8A-8E-91-A6-01");
INSERT INTO accounts VALUES(2,"11-9C-11-26-19-15");
SELECT * FROM accounts;

CREATE TABLE encryptions (
accounts_id INT ,
dt VARCHAR(255),
phrase VARCHAR(255),
password VARCHAR(255),
FOREIGN KEY (accounts_id) REFERENCES accounts(id)
);
SELECT * FROM encryptions;

INSERT INTO encryptions VALUES(1,"2023-02-09 09:08:03","dapibus-augue-vel-accumsan-",null);
INSERT INTO encryptions VALUES(2,"2023-03-25 06:37:22","ipsum-primis-in-faucibus-orici",null);

SELECT * FROM encryptions;
CREATE TABLE df AS
SELECT
    accounts.id,
    accounts.mac,
    encryptions.accounts_id,
    encryptions.dt,
    encryptions.phrase,
    encryptions.password
FROM
    accounts
INNER JOIN
    encryptions
ON
    accounts.id = encryptions.accounts_id;
SELECT 
    mac, 
    dt, 
    phrase
FROM 
    df
ORDER BY 
    mac ASC;



