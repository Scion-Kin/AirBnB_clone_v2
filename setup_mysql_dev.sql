-- create server for AirBnb project

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES on hbnb_dev_db.* to 'hbnb_dev'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
GRANT SELECT on performance_schema to 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

