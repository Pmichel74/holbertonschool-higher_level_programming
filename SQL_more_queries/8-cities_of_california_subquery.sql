-- Lists all cities of California from the database hbtn_0d_usa.
-- Uses a subquery to find California's ID and then matches cities.
-- Results are sorted by cities.id in ascending order.
SELECT id, name
    FROM cities
WHERE state_id IN 
    (SELECT id FROM states WHERE name = 'California')
ORDER BY id;