-- Import in hbtn_0c_0 database this table dump Temperatures.
-- Displays the average temperature (F) by city ordered by temperature (descending).
SELECT city, AVG(value) AS avg_temp From temperatures
GROUP BY city
ORDER BY avg_temp DESC;
