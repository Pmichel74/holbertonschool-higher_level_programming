-- Lists all shows contained in the database hbtn_0d_tvshows.
-- Uses LEFT JOIN to include all shows, even those without a genre.
-- NULL is displayed for shows without a linked genre.
-- Results are sorted by show title and genre ID for clear presentation.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;