vehicles = [
    ["Car", "Swift", 1000],
    ["Bike", "Activa", 500],
    ["Car", "Nexon", 1200]
]

while True:

    print("\n--- Vehicle Rental System ---")
    print("1. Show Vehicles")
    print("2. Rent Vehicle")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        print("\nAvailable Vehicles:")

        for i in range(len(vehicles)):
            print(
                i + 1,
                vehicles[i][0],
                vehicles[i][1],
                "₹", vehicles[i][2], "per day"
            )

    elif choice == "2":

        print("\nChoose a Vehicle:")
        for i in range(len(vehicles)):
            print(
                i + 1,
                vehicles[i][1],
                "₹", vehicles[i][2], "per day"
            )

        number = int(input("Enter vehicle number: "))
        days = int(input("Enter number of days: "))

        price = vehicles[number - 1][2]
        total = price * days

        print("\nVehicle:", vehicles[number - 1][1])
        print("Days:", days)
        print("Total Rent: ₹", total)

    elif choice == "3":

        print("Thank you!")
        break

    else:

        print("Wrong choice!")
        