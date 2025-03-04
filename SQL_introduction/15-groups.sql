-- Lists the number of records with the same score in the table second_table.
-- Records are grouped by score with label number.
-- Records are ordered by descending score.
SELECT score, COUNT(*)
FROM second_table
GROUP BY score
ORDER BY score DESC;
