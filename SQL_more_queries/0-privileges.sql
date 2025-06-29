-- Lists privileges of the MySQL users
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

GRANT USAGE ON *.* TO 'user_0d_1'@'localhost';
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
