# Title: whatabook.init.sql
# Creator: Maddie Maxwell
# Date Created: 02/27/2023
# Date Updated: N/A
# Description: whatabook database creation

CREATE DATABASE whatabook_user;
use whatabook_user;
CREATE TABLE whatabook(store varchar(100), books varchar(100), user varchar(100));
desc whatabook;
#insert data
INSERT INTO whatabook (store,books,user) VALUES ('Store1', 'The Tears', 'William Hopkins');
INSERT INTO whatabook (store,books,user) VALUES ('Store1', 'Thunderbolts', 'Anna Roberts');
INSERT INTO whatabook (store,books,user) VALUES ('Store1', 'The Adventures of Tom Sawyer', 'Mark Twain');
INSERT INTO whatabook (store,books,user) VALUES ('Store1', 'The Sandman - His Stories', 'William Hopkins');
INSERT INTO whatabook (store,books,user) VALUES ('Store1', 'The Ups and Downs in Life', 'Anna Roberts');
INSERT INTO whatabook (store,books,user) VALUES ('Store1', 'The Adventures of Huckleberry Finn', 'Mark Twain');
INSERT INTO whatabook (store,books,user) VALUES ('Store1', 'The Doers', 'William Hopkins');
INSERT INTO whatabook (store,books,user) VALUES ('Store1', 'Return to Phoenix', 'Anna Roberts');
INSERT INTO whatabook (store,books,user) VALUES ('Store1', 'Following the Equator', 'Mark Twain');
select * from whatabook;
