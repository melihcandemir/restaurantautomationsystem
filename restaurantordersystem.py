# Restaurant Order and Payment Automation
# Importing Library
from pyfiglet import figlet_format as figlet
from colorama import Fore as color
from os import system as command
import sqlite3 as sql
# Here is the Class name RestaurantMenu
class RestaurantOrderSystem():
    # Instance Constructor
    def __init__(self, name):
        self.name = name
        self.menu = {}

        try:
            connection = sql.connect("restaurant.db")
            c = connection.cursor()
            c.execute("SELECT name, price FROM menu")
            menu_data = c.fetchall()

            for name, price in menu_data:
                self.menu[name] = price
        except sql.Error as e:
            print("An error occurred while fetching the menu:", e)
        
        finally:
            connection.close()
 
    # Specifies customer order
    def customer(self, order):
        price = self.menu.get(order)
        if price is not None:
            self.order = order
            print("=" * 50)
            print("The Menu: {} - ${}".format(order, price))
            print("=" * 50)
            print("Thanks for your order, {}!".format(self.name))
            print("Your order will be ready in ~10 minutes.")
            print("=" * 50)
            
        else:
            print("Please choose another item from the menu.")

    # Displays the menu on the screen
    def display_menu(self):
        try:
            connection = sql.connect("restaurant.db")
            c = connection.cursor()

            c.execute("SELECT name, price FROM menu")
            menu_data = c.fetchall()

            print("=" * 30)
            for index, (name, price) in enumerate(menu_data, start=1):
                print("{:<0}. {:<20} {:<5}$".format(index, name, price))
            print("=" * 30)
        
        except sql.Error as e:
            print("An error occurred:", e)
        
        finally:
            connection.close()

    # Welcome Message to Customer
    def greeting(self):
        print("Welcome Restaurant!\n")
        print("What are you eating or drinking today ?\n")

    # An empty payment function but this will be completed in the future
    def payment(self, payment_method, balance):
        prices = float(self.menu[self.order])
        if payment_method == "Creditcard":
            if balance >= prices:
                balance -= prices
                print("Payment Confirmed.")
                print("Thank you for choosing us.")
                print("Have a nice day!")
            else:
                print("Insufficient Balance!")
                print("Please Try Again or Change Payment Method!")
        elif payment_method == "Cash":
            if balance >= prices:
                balance -= prices
                print("Thanks for your payment!")
                print("Thank you for choosing us.")
                print("Have a nice day!")
            else:
                print("Insufficient Balance!")
                print("Please Try Again or Change Payment Method!")
    
    # Will be arranged soon for refund system
    def refund():
        pass    
    
    # Will be arranged soon for the waiter tip system
    def waitress_tips():
        pass
    
    # Will be arranged soon for the invoice system
    def invoice():
        pass


    def login_interface(self, username, password):
        try:
            connection = sql.connect("restaurant.db")
            c = connection.cursor()

            c.execute("SELECT username, password FROM login WHERE username = ?", (username,))
            row = c.fetchone()

            if row:
                db_username, db_password = row
                if (username == db_username and password == db_password):
                    print("Welcome {}".format(self.name))
                    print("You have successfully logged in!")
                else:
                    print("Incorrect password.")
                    print("Continuing with Guest account!")
            else:
                print("User not found.")
                print("Continuing with Guest account.")
        
        except sql.Error as e:
            print("An error occurred:", e)
        
        finally:
            connection.close()

# Here is the Main Function
def main():
    try:
        while True:
            print(color.LIGHTGREEN_EX)
            print(figlet("Welcome Restaurant"))
            greeting = RestaurantOrderSystem("")
            print(color.YELLOW)
            greeting.greeting()
            customer_name = input("Hello there! What's your name ? \n\n")
            print(color.LIGHTBLUE_EX)
            order = RestaurantOrderSystem(customer_name)   
            username = input("Username: ")
            password = input("Password: ")
            order.login_interface(username, password)
            order.display_menu()
            print(color.LIGHTGREEN_EX)
            customers_order = input("Please enter order menu: ").capitalize()
            order.customer(customers_order)
            customer_payment = input("How would you like to make your payment ? ").capitalize()
            customer_balance = float(input("Enter the amount to pay: "))
            order.payment(customer_payment,customer_balance)
            exit_question = input("Exit (Q): ").upper()
            if exit_question == "Q":
                break
            command("cls")

    except Exception as e:
        print(e)

# If the function name is main, it executes the code inside the main function.
if __name__ == "__main__":
    main()
