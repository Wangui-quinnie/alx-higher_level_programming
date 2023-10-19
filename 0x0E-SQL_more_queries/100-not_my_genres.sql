-- script that uses the hbtn_0d_tvshows to list all genres not linked to the show Dexter
SELECT name FROM tv_genres
WHERE tv_genres.id NOT IN (
    SELECT tv_show_genres.genre_id
    FROM tv_show_genres
    INNER JOIN tv_shows ON tv_show_genres.show_id = id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name;
