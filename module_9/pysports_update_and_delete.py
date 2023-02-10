import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pysports"
)

UPDATE player
SET team_id - 2,
  first_name = 'Betty'
  last_name = 'White'
WHERE first_name = 'Smeagol'

DELETE FROM player
WHERE  first_name = 'Smeagol'

INSERT INTO player ('Betty', 'White', 2)
  VALUES('Smeagol', 'Shire Folk' 1);
