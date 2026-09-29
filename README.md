# Vehicle-Rental-Management-System

## About the Project

Vehicle Rental Management System is a simple Python console-based project.

The main purpose of this project is to manage vehicles, calculate rental costs, store customer rental details, and keep track of vehicle availability.

The project is made using basic Python concepts, so it is easy to understand and run.

## Features

The project currently provides the following options:

1. Show Available Vehicles
2. Show All Vehicles
3. Search Vehicle
4. Rent Vehicle
5. Return Vehicle
6. Show Rental Records
7. Show Total Income
8. Exit

The system contains seven sample vehicles:

| Vehicle Type | Vehicle       | Price Per Day |
| ------------ | ------------- | ------------: |
| Car          | Swift         |      Rs. 1000 |
| Bike         | Activa        |       Rs. 500 |
| Car          | Nexon         |      Rs. 1200 |
| Car          | Baleno        |      Rs. 1100 |
| Bike         | Royal Enfield |       Rs. 800 |
| Bike         | Pulsar        |       Rs. 600 |
| Car          | Creta         |      Rs. 1500 |

## How It Works

When the program starts, it displays a menu.

The user can select an option from the menu.

### 1. Show Available Vehicles

This option displays the vehicles that are currently available for rent along with their type and price per day.

### 2. Show All Vehicles

This option displays all vehicles and shows whether each vehicle is `Available` or `Rented`.

### 3. Search Vehicle

The user can enter a vehicle name to search for a vehicle.

The program displays:

```text
Vehicle Name
Vehicle Type
Rent Per Day
Vehicle Status
```

### 4. Rent Vehicle

The user selects a vehicle and enters:

```text
Customer Name
Phone Number
Number of Days
```

The program calculates the total rental cost using:

```text
Total Rent = Price Per Day × Number of Days
```

For example:

```text
Swift = Rs. 1000 per day
Days = 3

Total Rent = Rs. 1000 × 3
           = Rs. 3000
```

After renting, the vehicle status changes from:

```text
Available
```

to:

```text
Rented
```

### 5. Return Vehicle

This option allows the user to return a rented vehicle.

After returning the vehicle, its status changes back to:

```text
Available
```

### 6. Show Rental Records

This option displays the rental information stored during the program.

It includes:

```text
Customer Name
Phone Number
Vehicle
Number of Days
Total Rent
```

### 7. Show Total Income

This option calculates the total income earned from all rental records.

### 8. Exit

This option closes the program.

## Technologies Used

* Python
* Python Lists
* Nested Lists
* Functions
* For Loop
* While Loop
* If / Elif / Else
* Try / Except
* User Input
* Basic Arithmetic

## Requirements

To run this project, you need:

* Python 3.x
* Any Python IDE or code editor

Examples:

* Python IDLE
* VS Code
* PyCharm

## How to Run

### Step 1

Install Python 3.x on your computer.

### Step 2

Download or clone this repository.

### Step 3

Open the Python file:

```text
Vehicle Rental Management System.py
```

### Step 4

Run the program.

The main menu will appear:

```text
==========================================
       VEHICLE RENTAL MANAGEMENT SYSTEM
==========================================
1. Show Available Vehicles
2. Show All Vehicles
3. Search Vehicle
4. Rent Vehicle
5. Return Vehicle
6. Show Rental Records
7. Show Total Income
8. Exit
==========================================
```

## Example

```text
Enter your choice: 4

========== AVAILABLE VEHICLES ==========

1 | Car | Swift | Rs. 1000 per day
2 | Bike | Activa | Rs. 500 per day
3 | Car | Nexon | Rs. 1200 per day

Enter vehicle number: 1
Enter customer name: Rahul
Enter phone number: 9876543210
Enter number of days: 3

========== RENTAL SUCCESSFUL ==========
Customer: Rahul
Phone: 9876543210
Vehicle: Swift
Rent per Day: Rs. 1000
Days: 3
Total Rent: Rs. 3000
Status: Rented
```

## Project Structure

```text
Vehicle-Rental-Management-System/
│
├── Vehicle Rental Management System.py
└── README.md
```

## Current Limitations

The current version is a basic console-based project.

It does not currently include:

* Database storage
* Permanent file storage
* Online booking
* Online payment
* Login system
* Graphical user interface

The rental information is stored only while the program is running.

## Future Improvements

The project can be improved by adding:

* Customer registration
* Admin login
* Database storage
* File storage
* Vehicle adding and deleting
* Online booking
* Online payment
* Bill/receipt generation
* Graphical user interface

## Learning Outcomes

Through this project, I practiced:

* Creating lists
* Working with nested lists
* Creating functions
* Using loops
* Using conditional statements
* Taking input from users
* Accessing list elements
* Performing calculations
* Using try-except
* Creating a menu-driven Python program

## Conclusion

The Vehicle Rental Management System is a basic Python project that demonstrates how programming can be used to solve a simple real-world problem.

The current version allows users to search, rent, and return vehicles while also keeping rental records and calculating total rental income.

More features can be added in the future to make the system more complete.

---

**Name:** MAYANK MOHAN
**Registration Number:** 26BAI11096
**Course Code:** CSE1021
**Academic Year:** 2026–27