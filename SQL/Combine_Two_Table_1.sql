CREATE DATABASE mydatabase;
USE mydatabase;

CREATE TABLE threat_types (
id INT PRIMARY KEY,
threat_types VARCHAR(255)
);

INSERT INTO  threat_types VALUES(1,"Phishing");
INSERT INTO threat_types VALUES(2,"Rootkit");

SELECT * FROM threat_types;

CREATE TABLE qurantine_urls_1(
id INT PRIMARY KEY ,
threat_id INT ,
domain_name VARCHAR(255),
status ENUM("Qurantined","Safe","Deleted"),
total_occurrances INT ,
total_user_affected INT,
FOREIGN KEY (threat_id) REFERENCES threat_types(id)
);

SELECT * FROM qurantine_urls_1;

INSERT INTO qurantine_urls_1 VALUES (1,1,"amzon.com",null,2,903);
INSERT INTO qurantine_urls_1 VALUES (2,2,"yahoo.com",null,1,967);

SELECT * FROM qurantine_urls_1;

CREATE TABLE df AS
SELECT
    threat_types.id,
    threat_types.threat_types,
    qurantine_urls_1.threat_id,
    qurantine_urls_1.total_occurrances,
    qurantine_urls_1.domain_name,
    qurantine_urls_1.total_user_affected
    
FROM
    threat_types
INNER JOIN
    qurantine_urls_1
ON
    threat_types.id = qurantine_urls_1.threat_id;
    


SELECT 
    domain_name, 
    threat_types, 
    total_occurrances, 
    total_user_affected
    
FROM 
    df
ORDER BY 
    total_user_affected DESC, 
    domain_name ASC;







