-- List all records of table that have value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
	AND name <> ''
ORDER BY score DESC;
