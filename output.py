vehicles = [
    ["Car", "Swift", 1000, "Available"],
    ["Bike", "Activa", 500, "Available"],
    ["Car", "Nexon", 1200, "Available"],
    ["Car", "Baleno", 1100, "Available"],
    ["Bike", "Royal Enfield", 800, "Available"],
    ["Bike", "Pulsar", 600, "Available"],
    ["Car", "Creta", 1500, "Available"],
]

rentals = []


def show_vehicles():
    """Displays all available vehicles for rent."""
    print("\n========== AVAILABLE VEHICLES ==========")
    found = False

    for i in range(len(vehicles)):
        if vehicles[i][3] == "Available":
            print(
                f"{i + 1} | {vehicles[i][0]} | {vehicles[i][1]} | Rs. {vehicles[i][2]} per day"
            )
            found = True

    if not found:
        print("No vehicles are available.")


def show_all_vehicles():
    """Displays the entire vehicle inventory with current statuses."""
    print("\n========== ALL VEHICLES ==========")
    for i in range(len(vehicles)):
        print(
            f"{i + 1} | {vehicles[i][0]} | {vehicles[i][1]} | Rs. {vehicles[i][2]} per day | {vehicles[i][3]}"
        )


def search_vehicle():
    """Searches for a vehicle by name."""
    name = input("\nEnter vehicle name: ")
    found = False

    for i in range(len(vehicles)):
        if name.lower() in vehicles[i][1].lower():
            print("\nVehicle Found")
            print("Vehicle:", vehicles[i][1])
            print("Type:", vehicles[i][0])
            print("Rent: Rs.", vehicles[i][2], "per day")
            print("Status:", vehicles[i][3])
            found = True

    if not found:
        print("Vehicle not found.")


def rent_vehicle():
    """Handles vehicle rental processing and updates status."""
    show_vehicles()

    try:
        number = int(input("\nEnter vehicle number: "))

        if number < 1 or number > len(vehicles):
            print("Invalid vehicle number.")
            return

        if vehicles[number - 1][3] == "Rented":
            print("This vehicle is already rented.")
            return

        customer_name = input("Enter customer name: ")
        phone = input("Enter phone number: ")
        days = int(input("Enter number of days: "))

        if days <= 0:
            print("Days should be greater than 0.")
            return

        price = vehicles[number - 1][2]
        total = price * days

        # Update status to Rented
        vehicles[number - 1][3] = "Rented"

        # Record rental details
        rental = [customer_name, phone, vehicles[number - 1][1], days, total]
        rentals.append(rental)

        print("\n========== RENTAL SUCCESSFUL ==========")
        print("Customer:", customer_name)
        print("Phone:", phone)
        print("Vehicle:", vehicles[number - 1][1])
        print("Rent per Day: Rs.", price)
        print("Days:", days)
        print("Total Rent: Rs.", total)
        print("Status: Rented")
        print("=======================================")

    except ValueError:
        print("Please enter numbers correctly.")


def return_vehicle():
    """Processes returning a rented vehicle."""
    print("\n========== RETURN VEHICLE ==========")
    found = False

    for i in range(len(vehicles)):
        if vehicles[i][3] == "Rented":
            print(f"{i + 1} | {vehicles[i][1]} | {vehicles[i][0]}")
            found = True

    if not found:
        print("No vehicle is currently rented.")
        return

    try:
        number = int(input("\nEnter vehicle number: "))

        if number < 1 or number > len(vehicles):
            print("Invalid vehicle number.")
            return

        if vehicles[number - 1][3] == "Available":
            print("This vehicle is already available.")
            return

        vehicles[number - 1][3] = "Available"
        print("\nVehicle returned successfully!")
        print("Vehicle:", vehicles[number - 1][1])
        print("Status: Available")

    except ValueError:
        print("Please enter a valid number.")


def show_rental_records():
    """Displays all rental history transactions."""
    print("\n========== RENTAL RECORDS ==========")

    if not rentals:
        print("No rental records available.")
        return

    for i, rental in enumerate(rentals, 1):
        print(f"\nRental {i}")
        print("Customer Name:", rental[0])
        print("Phone Number:", rental[1])
        print("Vehicle:", rental[2])
        print("Number of Days:", rental[3])
        print("Total Rent: Rs.", rental[4])


def total_income():
    """Calculates total revenue generated from all rentals."""
    total = sum(rental[4] for rental in rentals)
    print("\n========== TOTAL INCOME ==========")
    print(f"Total rental income: Rs. {total}")


def main():
    """Main program control loop."""
    while True:
        print("\n==========================================")
        print("       VEHICLE RENTAL MANAGEMENT SYSTEM")
        print("==========================================")
        print("1. Show Available Vehicles")
        print("2. Show All Vehicles")
        print("3. Search Vehicle")
        print("4. Rent Vehicle")
        print("5. Return Vehicle")
        print("6. Show Rental Records")
        print("7. Show Total Income")
        print("8. Exit")
        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_vehicles()
        elif choice == "2":
            show_all_vehicles()
        elif choice == "3":
            search_vehicle()
        elif choice == "4":
            rent_vehicle()
        elif choice == "5":
            return_vehicle()
        elif choice == "6":
            show_rental_records()
        elif choice == "7":
            total_income()
        elif choice == "8":
            print(
                "\nThank you for using Vehicle Rental Management System!\nHave a nice day!"
            )
            break
        else:
            print("\nWrong choice!\nPlease enter a number from 1 to 8.")


if __name__ == "__main__":
    main()