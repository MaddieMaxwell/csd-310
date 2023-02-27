## Assigment: 11.2: Whatabook Development
# Creator: Maddie Maxwell
# Date Created: February 2, 2023
# Date updated: N/A
# Description: Developing queries for whatabook assignment. 



#creating queries using selects to view user wishlists

SELECT user._id, user.first_name, user.last_name, book.book_id, book.book_title, book.writer
FROM wishlist
    INNER JOIN user ON wishlist.user_id, = user.user_id
    INNER JOIN user ON wishlist.book_id = book.book_id
WHERE user.user_id = 1;

#queries that are used to view a stores location

SELECT store_id, locale FROM store;

#queries that use SELECT to view a full listing of the books the Whatabook offers

SELECT book_id, book_title, book_writer, details FROM book;

# Using select queries to view a listing of books that are not already
# in a users wishlist. User ids will be replaced with the acutal values 
# that are selected by the user.

SELECT book_id, book_title, book_writer, details
FROM book
WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = 1);

# create statements to add a new book to a users wishlist.
# Values will need to be replaced with the acutal values that the 
# users select from the program.

INSERT INTO wishlist(user_id, book_id)
    VALUES (1,9)

# Create code to remove a book from a user's wishlist. The user id and book id values
# will be replaced with actual values the user selects.

DELETE FROM wishlist WHERE user_id = 1 AND book_id = 9;
