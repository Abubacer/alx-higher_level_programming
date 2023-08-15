-- Import in hbtn_0c_0 database this table dump Temperatures
-- Displays the max temperature of each state (ordered by State name)..
SELECT state, MAX(value) AS max_temp From temperatures
GROUP BY state
ORDER BY state ASC;
