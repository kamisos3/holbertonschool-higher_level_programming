-- Creating table that handles unique id with default value 1
CREATE TABLE IF NOT EXISTS unique_id (
	id INT NOT NULL DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
