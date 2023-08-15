-- Lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in my MySQL server.
-- Display in descending order: the score, the number of records for this score with the label number.
SELECT score, COUNT(1) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
