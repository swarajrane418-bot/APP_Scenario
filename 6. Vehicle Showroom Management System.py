

class Vehicle:
    def __init__(self, vehicle_number, brand, price, category):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price
        self.category = category

    def display(self):
        print("\nVehicle Number :", self.vehicle_number)
        print("Brand          :", self.brand)
        print("Price          : ₹", self.price)
        print("Category       :", self.category)
        print("-" * 35)


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self):
        number = input("Enter Vehicle Number: ")
        brand = input("Enter Brand: ")
        price = float(input("Enter Price: "))

        print("\n1. Luxury")
        print("2. Economy")

        choice = int(input("Enter Category: "))

        if choice == 1:
            category = "Luxury"
        elif choice == 2:
            category = "Economy"
        else:
            print("Invalid category!")
            return

        vehicle = Vehicle(number, brand, price, category)
        self.vehicles.append(vehicle)

        print("Vehicle added successfully!")

    def display_all(self):
        if not self.vehicles:
            print("No vehicles available.")
            return

        print("\n===== VEHICLE SHOWROOM =====")

        for vehicle in self.vehicles:
            vehicle.display()




showroom = Showroom()

while True:
    print("\n===== VEHICLE SHOWROOM MANAGEMENT =====")
    print("1. Add Vehicle")
    print("2. Display All Vehicles")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        showroom.add_vehicle()

    elif choice == 2:
        showroom.display_all()

    elif choice == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")