create database pysports
create user 'pysports_user'@'localhost' IDENTIFIED WITH Mysql_native_password BY 'MySQLIsGreat!';
GRANT ALL PRIVILEGES ON pysports.* TO 'pysports_user'@'localhost';
DROP USER IF EXISTS 'pysports_user'@'localhost';
CREATE TABLE team (
    team_id     INT           NOT NULL    AUTO_INCREMENT,
    team_name   VARCHAR(75)   NOT NULL,
    mascot      VARCHAR(75)   NOT NULL,
    PRIMARY KEY(team_id)
);
CREATE TABLE player(
    player_id   INT           NOT NULL     AUTO_INCREMENT,
    first_name  VARCHAR(75)   NOT NULL,
    last_name   VARCHAR(75)   NOT NULL,
    team_id     INT           NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);
INSERT team (team_name, mascot)
    VALUES ('Team Ravenclaw', 'Black Ravens');
DROP TABLE IF EXISTS player;
SELECT team_id FROM team WHERE team_name = 'Team Slytherin';
pip install mysql-connector-python
import mysql.connector
from mysql.connector import errorcode
config = {
    "user": "pysports_user",
    "password": "MySQLIsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": TRUE
}
db = mysql.connector.connect(**config)
print("\n Database user {} connected to MySQL on host {} with database {}*.format["user"], config["host"], config["database"]")
input("\n\n Press any key to continue")
except mysql.connector.Error as err:
  if err.errno ==errorcode.ER_ACCESS_DENIED_ERROR:
    print(" The specified database does not exist")
 else:
  print(err)
  
finally:
  db.close()
