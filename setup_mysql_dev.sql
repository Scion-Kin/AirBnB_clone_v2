-- create server for AirBnb project


-- create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create user
CREATE USER 'hbnb_dev'@'localhost' IF NOT EXISTS IDENTIFIED BY 'hbnb_dev_pwd';
-- grant privileges
GRANT ALL PRIVILEGES on hbnb_dev_db to 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
GRANT SELECT on performance_schema to 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

