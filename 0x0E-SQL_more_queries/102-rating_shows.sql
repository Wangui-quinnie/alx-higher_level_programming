-- script that lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT title, SUM(tv_show_ratings.rate) AS rating FROM tv_shows
INNER JOIN tv_show_ratings ON id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
