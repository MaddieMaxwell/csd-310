import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pysports"
)

SELECT player_id, first_name, Last_name, team_name
from player
INNER JOIN team
  on player.team_id = team.team_id
