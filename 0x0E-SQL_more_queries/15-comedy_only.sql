-- Lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_shows table contains only one record where name = Comedy.
-- Each record display: tv_shows.title
-- Results must be sorted in ascending order by the show title.
SELECT title FROM tv_shows
JOIN tv_show_genres ON id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;
