-- Lists all shows in database and NUll the ones with no genre
SELECT
	tv_shows.title,
	tv_show_genres.genre_id
FROM
	tv_show
LEFT JOIN
	tv_show_genres
   ON
	tv_shows.id = tv_show_genres.show_id
ORDER BY
	tv_shows.title ASC,
	tv_show_genres.genre_id ASC;
