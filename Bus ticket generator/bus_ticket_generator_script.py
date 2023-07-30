import time


def print_delay(text, delay=1):
    print(text)
    time.sleep(delay)


def calculate_fare(service_type, distance):
    seater_rate_per_km = 0.4  # Modify this value for the seater service fare per kilometer
    # Modify this value for the sleeper service fare per kilometer
    sleeper_rate_per_km = 0.8

    if service_type.lower() == "seater":
        return seater_rate_per_km * distance
    elif service_type.lower() == "sleeper":
        return sleeper_rate_per_km * distance
    else:
        return None


def generate_bus_ticket():
    print("Welcome to the Bus Ticket Generator!")
    print("Please enter the following details to generate your bus ticket.")

    passenger_name = input("Passenger Name: ")
    destination = input("Destination: ")
    date_of_travel = input("Date of Travel: ")
    seat_number = input("Seat Number: ")

    print("Select the type of ticket:")
    print("1. One-way")
    print("2. Round trip")
    ticket_type = input("Enter the option number (1 or 2): ")

    if ticket_type == "1":
        ticket_type = "One-way"
        distance = float(input("Enter the distance (in kilometers): "))
        service_type = input("Select the bus service type (seater/sleeper): ")
        fare = calculate_fare(service_type, distance)
        if fare is not None:
            print("\n***********************")
            print("      BUS TICKET")
            print("***********************")
            print(f"Passenger Name: {passenger_name}")
            print(f"Destination: {destination}")
            print(f"Date of Travel: {date_of_travel}")
            print(f"Seat Number: {seat_number}")
            print(f"Ticket Type: {ticket_type}")
            print(f"Bus Service: {service_type}")
            print(f"Distance: {distance} km")
            print(f"Fare: ${fare:.2f}")
            print("***********************")
            print("   Have a safe trip!")
            print("***********************")
        else:
            print("Invalid bus service type. Please enter 'seater' or 'sleeper'.")
            return
    elif ticket_type == "2":
        ticket_type = "Round trip"
        print("\nRound trip tickets are not currently available. Please check back later.")
    else:
        print("Invalid option. Please enter '1' or '2' for ticket type.")
        return


if __name__ == "__main__":
    generate_bus_ticket()
