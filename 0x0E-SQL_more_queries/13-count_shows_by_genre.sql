-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record display: <TV Show genre> - <Number of shows linked to this genre>.
-- First column must be called genre and Second column must be called number_of_shows.
-- Results are sorted in descending order by the number of shows linked.
SELECT name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
