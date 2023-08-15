-- Import in hbtn_0c_0 database this table dump Temperatures
-- Displays the top 3 of cities temperature during July and August ordered by temperature (descending).
SELECT city, AVG(value) AS avg_temp From temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
