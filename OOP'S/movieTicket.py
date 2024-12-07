#Create a MovieTicket class with attributes like movie_name, 
# available_tickets, and price_per_ticket. Add methods 
# book_ticket(quantity) and cancel_ticket(quantity). 
# Ensure that tickets can only be booked if the requested 
# quantity is available, and update the available tickets 
# accordingly.

class MovieTicket:
    def __init__(self, movie):
        self.movie_name = movie
        self.available_tickets = 10
        self.services()

    def services(self):
        print(f"Currently available tickets for {self.movie_name} is: {self.available_tickets}")
        while(1):
            print("1.Book Ticket \n2.Cancel Ticket \n3.Exit")
            ch = int(input("Enter your choice: \n"))
            if ch == 1:
                quantity = int(input("Enter the quantatity: \n"))
                self.book_ticket(quantity)
            elif ch == 2:
                quantity = int(input("Enter the quantatity to cancel: \n"))
                self.cancel_ticket(quantity)
            elif ch == 3:
                exit()


    def book_ticket(self, quantity):
        if quantity > self.available_tickets:
            print("Quantity is too large..")
            return -1
        self.available_tickets = self.available_tickets - quantity
        print(f"Your ticket is booked, currently available tickets are {self.available_tickets}")

    def cancel_ticket(self, quantity):
        if (self.available_tickets + quantity) < 10:
            self.available_tickets = self.available_tickets + quantity
            print(f"Available tickets now are: {self.available_tickets}")
            return 1
        print("You are cancelling more then the ticketes you booked")

movie = input("Enter the movie name: \n")
obj = MovieTicket(movie)

