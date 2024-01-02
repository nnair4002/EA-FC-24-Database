#All male French players who play for PSG
SELECT *
FROM players.male_players
WHERE Club = 'Paris SG'
AND  Nation = 'France';

#Averge age of each position
SELECT Position, AVG(Overall)
FROM players.male_players
GROUP BY Position;

#Maximum overall rating for each position
SELECT Position, MAX(Overall)
FROM players.male_players
GROUP BY Position;

#All male English players with an overall of at least 84, sorted alphabetically
SELECT *
FROM players.male_players
WHERE Nation = 'England' AND Overall >= 84
ORDER BY Name;

#All male Bayern Munchen players, with an overall of at least 84, sorted by greatest shooting stat to lowest shooting stat
SELECT *
FROM players.male_players
WHERE Club LIKE '%Bayern%' AND Overall >= 84
ORDER BY Shooting DESC;

#All clubs which have an averge overall stat of greater than 75
SELECT Club, AVG(Overall)
FROM players.male_players
GROUP BY Club
HAVING AVG(Overall) > 75;

#Top 5 players in the curve stat category with a curve stat greater than 75
SELECT Name, AVG(Curve)
FROM players.male_players
GROUP BY Name
HAVING AVG(Curve) > 75
ORDER BY AVG(Curve) DESC
LIMIT 5;

#Third best position with of the positions with the highest average acceleration stat
SELECT Position, AVG(Acceleration) AS Average_Acceleration
FROM players.male_players
GROUP BY Position
ORDER BY Average_Acceleration DESC
LIMIT 2, 1;