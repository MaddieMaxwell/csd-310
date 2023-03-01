# Titel: whatabook.init.sql
# Creator: Maddie Maxwell
# Date Created: 02/15/2023
# Date Updated: N/A
# Description: whatabook database creation

#drop test user
DROP USER IF EXISTS 'whatabook_user'@'localhost';

#create whatabook_user then grant all priviledges to them 
GRANT ALL PRIVILEGES ON whatabook.*TO'whatabook_user'@'localhost';

#drop constraints
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlilt DROP FOREIGN KEY fk_user;

#drop table 
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

#create the tables

#store table
CREATE TABLE store (
  store_id  INT         NOT NULL    AUTO_INCREMENT,
  locale  varchar(100)  NOT NULL,
  PRIMARY KEY(store_id)
);

#book table
CREATE TABLE book(
  book_id     INT           NOT NULL  AUTO_INCREMENT,
  book_title  VARCHAR(100)  NOT NULL,
  book_writer VARCHAR(100)  NOT NULL,
  details     VARCHAR(600),
);
#user table
CREATE TABLE user(
  user_id     INT           NOT NULL  AUTO_INCREMENT,
  first_name  VARCHAR(90)   NOT NULL,
  last_name   VARCHAR(90)   NOT NULL,
  PRIMARY KEY(user_id)
);
#wishlist table
CREATE TABLE wishlist(
  wishlist_id   INT   NOT NULL  AUTO_INCREMENT,
  user_id       INT   NOT NULL,
  book_id       INT   NOT NULL,
  PRIMARY KEY (wishlist_id),
  CONSTRAINT fk_book
  FOREIGN KEY (book_id)
      REFERENCES book(book_id),
);

#insert store record 

INSERT INTO store(locale)
    VALUES('1000 Galvin Rd S, Bellevue, NE 68005');


#insert book records 
INSERT INTO book (book_title, author,)
    VALUES ('The Tears', 'William Hopkins');
INSERT INTO book (book_title, author,) 
    VALUES ('Thunderbolts', 'Anna Roberts');
INSERT INTO book (book_title, author,)
    VALUES ('The Adventures of Tom Sawyer', 'Mark Twain');
INSERT INTO book (book_title, author,)
    VALUES ('The Sandman - His Stories', 'William Hopkins');
INSERT INTO book (book_title, author,) 
    VALUES ('The Ups and Downs in Life', 'Anna Roberts');
INSERT INTO book (book_title, author,) 
    VALUES ('The Adventures of Huckleberry Finn', 'Mark Twain');
INSERT INTO book (book_title, author,)
    VALUES ('The Doers', 'William Hopkins');
INSERT INTO book (book_title, author,) 
    VALUES ('Return to Phoenix', 'Anna Roberts');
INSERT INTO book (book_title, author,) 
    VALUES ('Following the Equator', 'Mark Twain');

#insert user info
INSERT INTO user (first_name, last_name)
    VALUES ('Betty', 'White'):
INSERT INTO user (first_name, last_name)
    WALUES ('Tom', 'Hanks');
INSERT INTO user (first_name, last_name)
    VALUES ('Debbie', 'Gallagher');

#create wishlist records
INSERT INTO wishlist(user_id, bood_id)
   VALUES (
    (SELECT user_id, FROM user WHERE first_name = 'Betty'),
    (SELECT book_id FROM user WHERE book_title = 'Following the Equator')
    );
INSERT INTO wishlist(user_id, bood_id)
   VALUES (
    (SELECT user_id, FROM user WHERE first_name = 'Tom'),
    (SELECT book_id FROM user WHERE book_title = 'Return to Phoenix')
    );
INSERT INTO wishlist(user_id, bood_id)
   VALUES (
    (SELECT user_id, FROM user WHERE first_name = 'Debbie'),
    (SELECT book_id FROM user WHERE book_title = 'The Doers')
    );
