# Railway Ticket Booking System
import random
import pandas as pd  

# Train data
trains = [
    {"train_no": 101, "train_name": "Shatabdi Express", "sleeper_seats": 50, "ac_seats": 20, "base_price_sleeper": 150, "base_price_ac": 500},
    {"train_no": 102, "train_name": "Rajdhani Express", "sleeper_seats": 60, "ac_seats": 15, "base_price_sleeper": 200, "base_price_ac": 600},
    {"train_no": 103, "train_name": "Duronto Express", "sleeper_seats": 70, "ac_seats": 25, "base_price_sleeper": 180, "base_price_ac": 550},
]

# Function to display available trains
def display_trains():
    print("\nAvailable Trains:")
    print("Train No\tTrain Name\t\tSleeper Seats\tAC Seats\tSleeper Price\tAC Price")
    for train in trains:
        print(f"{train['train_no']}\t\t{train['train_name']:<20}\t{train['sleeper_seats']}\t\t{train['ac_seats']}\t\t{train['base_price_sleeper']}\t\t{train['base_price_ac']}")

# Function to check seat availability
def check_availability(train_no, seat_type):
    for train in trains:
        if train['train_no'] == train_no:
            if seat_type == "sleeper":
                return train['sleeper_seats']
            elif seat_type == "ac":
                return train['ac_seats']
    return 0

# Function to calculate fare 
def calculate_fare(train_no, seat_type):
    for train in trains:
        if train['train_no'] == train_no:
            if seat_type == "sleeper":
                demand_factor = 1.2 if train['sleeper_seats'] < 20 else 1.0  
                return int(train['base_price_sleeper'] * demand_factor)
            elif seat_type == "ac":
                demand_factor = 1.5 if train['ac_seats'] < 5 else 1.0  
                return int(train['base_price_ac'] * demand_factor)
    return 0

# Function to book tickets (single or multiple)
def book_tickets(train_no, seat_type, passenger_names):
    for train in trains:
        if train['train_no'] == train_no:
            available_seats = train['sleeper_seats'] if seat_type == "sleeper" else train['ac_seats']
            if available_seats >= len(passenger_names):
                fare = calculate_fare(train_no, seat_type) * len(passenger_names)
                pnr_list = []
                for passenger_name in passenger_names:
                    if seat_type == "sleeper":
                        train['sleeper_seats'] -= 1
                    elif seat_type == "ac":
                        train['ac_seats'] -= 1
                    pnr = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=10))  # Generate alphanumeric PNR
                    pnr_list.append(pnr)
                    print(f"\nTicket booked successfully!\nPassenger Name: {passenger_name}\nTrain: {train['train_name']}\nClass: {seat_type.capitalize()}\nFare: Rs. {calculate_fare(train_no, seat_type)}\nPNR: {pnr}")
                print(f"\nTotal Fare for {len(passenger_names)} tickets: Rs. {fare}")
                return
            else:
                print(f"\nSorry, only {available_seats} seats are available in the selected class.")
                return
    print("\nInvalid train number.")

# Function to cancel a booking
def cancel_ticket(train_no, seat_type):
    for train in trains:
        if train['train_no'] == train_no:
            if seat_type == "sleeper":
                train['sleeper_seats'] += 1  # Add back one seat to availability
                print("\nTicket cancellation successful. The seat has been freed.")
                return
            elif seat_type == "ac":
                train['ac_seats'] += 1  # Add back one seat to availability
                print("\nTicket cancellation successful. The seat has been freed.")
                return
    print("\nInvalid train number or seat type.")

# Main program
def main():
    while True:
        print("\nWelcome to the Railway Ticket Booking System")
        print("1. View Available Trains")
        print("2. Book Tickets")
        print("3. Cancel a Ticket")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_trains()
        elif choice == "2":
            try:
                train_no = int(input("Enter Train Number: "))
                seat_type = input("Enter Seat Type (sleeper/ac): ").lower()
                passenger_names = input("Enter Passenger Names (comma-separated): ").split(',')
                passenger_names = [name.strip() for name in passenger_names]
                book_tickets(train_no, seat_type, passenger_names)
            except ValueError:
                print("\nInvalid input. Please try again.")
        elif choice == "3":
            try:
                train_no = int(input("Enter Train Number: "))
                seat_type = input("Enter Seat Type (sleeper/ac): ").lower()
                cancel_ticket(train_no, seat_type)
            except ValueError:
                print("\nInvalid input. Please try again.")
        elif choice == "4":
            print("\nThank you for using the Railway Ticket Booking System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
