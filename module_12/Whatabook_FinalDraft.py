#Title: Whatabook.py
#Creator: Maddie Maxwell
#Date Created: Feburary 27, 2023
#Date updated: N/A
#Class: CYBER 410
#Assignment 12.3
#Description: This is my first attempted at the whatabook final 
#assignement for class 

#importing the connector to mySQL
import sys
import mysql.connector
from mysql.connector import errorcode

#config object database

config ={
    "user": "whatabook_user"
    "password": "MySQL8IsGreat!",
    "host": "192.168.56.1",
    "database": "whatabook"
    "raise_on_warning": True
}

def show_menu():
    print("\n -- Main Menu --")
    print(" 1. View Books\n     2. View Store locations\n   3. My Account\n 4. Exit")
    try:
        choice = int(input('Press 1 for book listings>: '))
        return choice
    except ValueError:
        print("\n   Invaild input, program will not terminat...\n")
        sys.exit(0)

def show_books(_cursor):
    #inner join
    _cursor.execute("SELECT the book_id, book_title, writer, and details from book")

    #cursor results
    books = _cursor.fetchall()
    print(" Displaying Book Listings")

    #display results
    for book in books:
        print(" Book Title: {}\n    Writer: {}\n    Details:{}\n".format(book[0], book[1], book[3]))
    
def show_store_locations(_cursor):
        _cursor.execute("SELECT store_id, locale from store")
        locations = _cursor.fetchall()
        print(" Displaying locations where selected book is available ")

def validate_user():
        #code to validate a user's id
        try:
            user_id = int(input('\n Please enter your user ID>: '))
            if user_id < 0 or user_id> 3:
                print(" Invaide user ID, program will now terminate....")
                sys.exit(0)
            return user_id
        except ValueError:
            print(" Invaild ID, program will now terminate")
            sys.exit(0)

def show_account_menu():
        #display the users account
        try:
            print(" User Menu ")
            print(" 1.Wishlist\n    2. Add Book\n   3. Main Menu")
            account_options = int(input('   Please enter the menu number you with to view>: '))
            return account_options
        except ValueError:
            print(" Invalid Input entered, progam will not terminate")
            sys.exit(0)

def show_wishlist(_cursor, _user_id):
        #getting the database for the list of books that were added to the wishlist
        _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_title, book.writer "+ 
                        "FROM wishlist " +
                        "INNER JOIN user ON wishlist.user id = user.user_id " +
                        "INNER JOIN book ON wishlist.book id = book.book_id " +
                        "WHERE user.user id = {}".format(_user_id))
        wishlist = _cursor.fetchall()
        print(" Displaying wishlist ")
        for book in wishlist:
            print(" Book Title: {}\n    Writer: {}\n".format(book[4],book[5]))

def show_books_need_added(_cursor, _user_id):
        #code to show books that need to be added to the wishlist
        query = ("SELECT book_id, book_title, writer, details" +
                 "FROM book " +
                 "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
        print(query)
        _cursor.execute(query)
        book_to_add = _cursor.fetchall()
        print(" Displaying books that can be added to the wishlist  ")
        for book in book_to_add:
            print(" Book ID: {}\n   Book Title: {}\n".format(_user_id, _book_id))
            try:
                #try/catch block that can be used to help handle MySQL errors
                db = db.cursor.connect (**config) #connecting to the whatabook database
                cursor = db.cursor() #cursor used for mysql 
                print("     Welcome to the Whatabook Program    ")
                user_selection = show_menu #this line will display the main menu

                #while the user selection is not 4
                while user_selection != 4:
                    #if user selects option 1, this code will fetch the books and display them
                    if user_selection == 1:
                        show_books(cursor)
                    #if user selects option 2, this code will fetch the store locations and display them
                    if user_selection ==2:
                        show_store_locations(cursor)
                    #if the user selects option 3, this code will validate the user using the validate user method
                    if user_selection == 3:
                        my_user_id = validate_user()
                        account_options = show_account_menu()
                        #while account option does not = 3
                        while account_options != 3:
                            # if statment that executes if user selected option 1,
                            if account_options == 1:
                                show_wishlist(cursor, my_user_id)
                            #if statement that executes if opton 2 is selected instead of opiton 3
                            if account_options == 2:
                                #show the books that are not currently on the user's wishlist
                                show_books_need_added(cursor, my_user_id)
                                #get entered book_id
                                book_id = int(input("   Enter the ID of the book you wish to add to you wishlist:   "))
                                #add the new book to the wishlist
                                book_to_add(cursor, my_user_id, book_id)

                                db.commit() #commit the changes to the database

                                #give a confimation to the user that the book was added
                                print(" Book ID: {} was successfully added to your wishlist!".format(book_id))
                            #if the input given is less than 0 or greater than 3, give a invalid input message
                            # and send user back to the account ment
                            if account_options < 0 or account_options > 3:
                                print("  Invaild option, pleare re-enter selection...")
                            #show account menu
                            account_options = show_account_menu()
                    
                    #if the input given is less than 0 or greater than 4, show a invalid user
                    #selection message, and send them back to the main menu
                    if user_selection < 0 or user_selection > 4:
                        print(" Invalid Input, please re-enter input")
                        #display main menu
                        user_selection = show_menu()
                        print(" Program ended")
except mysql.connector.Error as err:
    #handling errors
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
     print(" The usersname or password given is incorrect")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
     print(" The database you are looking for does not exist")
    else:
    print("err")
finally:
    #close the mysql connection
    db.close()
