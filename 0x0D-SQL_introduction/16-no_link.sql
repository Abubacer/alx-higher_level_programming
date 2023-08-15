-- Lists all records of the table second_table of the database hbtn_0c_0 in my MySQL server.
-- Don’t list rows without a name value.
--  Displays the score and the name and records should be listed by descending score.
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
