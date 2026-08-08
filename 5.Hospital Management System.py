class Patient:
    def __init__(self, patient_id, name, treatment_cost, category):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost
        self.category = category

    def display(self):
        print(f"ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Treatment Cost: ₹{self.treatment_cost}")
        print(f"Category: {self.category}")
        print("-" * 30)


class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self):
        patient_id = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        cost = float(input("Enter Treatment Cost: "))

        print("1. General")
        print("2. Special")
        choice = int(input("Enter category: "))

        if choice == 1:
            category = "General"
        elif choice == 2:
            category = "Special"
        else:
            print("Invalid category!")
            return

        patient = Patient(patient_id, name, cost, category)
        self.patients.append(patient)

        print("Patient added successfully!")

    def display_all(self):
        if not self.patients:
            print("No patient records available.")
            return

        print("\n===== PATIENT RECORDS =====")
        for patient in self.patients:
            patient.display()


# Main program
hospital = Hospital()

while True:
    print("\n===== HOSPITAL PATIENT MANAGEMENT =====")
    print("1. Add Patient")
    print("2. Display All Records")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        hospital.add_patient()

    elif choice == 2:
        hospital.display_all()

    elif choice == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")