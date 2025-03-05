-- Lists all shows in the database hbtn_0d_tvshows that don't have a genre linked.
-- Uses LEFT JOIN to include all shows and filters with WHERE to keep only those without genres.
-- Results are sorted by show title for clear organization.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id is NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;