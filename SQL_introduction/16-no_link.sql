-- Lists all records of the table second_table having a score greater than 10 and a non-empty name.
-- Records are ordered by descending score.
SELECT score, name 
FROM second_table
WHERE score > 10 AND name IS NOT NULL AND name != ''
ORDER BY score DESC;
