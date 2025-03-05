-- Lists all genres from the database and displays the number of shows linked to each.
-- Only genres with at least one show linked are counted.
-- Results are ordered by descending number of shows to highlight popular genres.
-- Uses JOIN, GROUP BY and aggregate COUNT function to calculate these statistics.
SELECT tv_genres.name AS genre,
COUNT(*) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
