class Patient:
    total_patients = 0

    def __init__(self, patient_id, name, age, visit_reason):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.visit_reason = visit_reason
        Patient.total_patients += 1

    def display_info(self):
        print("\n--- Patient Information ---")
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Reason for Visit: {self.visit_reason}")

    def update_record(self, name, age, visit_reason):
        self.name = name
        self.age = age
        self.visit_reason = visit_reason
        print("Patient record updated successfully!")


class PatientRecordSystem:
    def __init__(self):
        self.patients = []
        self.next_id = 1

    @staticmethod
    def is_valid_age(age):
        return age >= 0
    
    def add_patient(self):
        print("\n--- Add New Patient ---")

        name = input("Enter patient name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return
        
        try:
            age = int(input("Enter patient age: "))

            if not self.is_valid_age(age):
                print("Age cannot be negative.")
                return
            
        except ValueError:
            print("Please enter a valid age.")
            return
        
        reason = input("Enter reason for visit: ").strip()

        if not reason:
            print("Reason for visit cannot be empty.")
            return
        
        patient = Patient(self.next_id, name, age, reason)
        self.patients.append(patient)

        print(f"Patient added successfully! Patient ID: {self.next_id}")
        self.next_id += 1

    def display_all_records(self):
        if not self.patients:
            print("\nNo patient records available.")
            return
        
        print("\n===== ALL PATIENT RECORDS =====")
        for patient in self.patients:
            patient.display_info()

    def find_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
            
        return None
    
    def search_patient(self):
        try:
            patient_id = int(input("Enter patient ID to search: "))
        except ValueError:
            print("Please enter a valid patient ID.")
            return
        
        patient = self.find_patient(patient_id)

        if patient:
            patient.display_info()
        else:
            print("Patient not found.")

    def update_patient(self):
        try:
            patient_id = int(input("Enter patient ID to update: "))
        except ValueError:
            print("Please enter a valid patient ID.")
            return
        
        patient = self.find_patient(patient_id)

        if not patient:
            print("Patient not found.")
            return
        
        name = input("Enter new patient name: ").strip()

        try:
            age = int(input("Enter new age: "))

            if not self.is_valid_age(age):
                print("Age cannot be negative.")
                return

        except ValueError:
            print("Please enter a valid age.")
            return
        
        reason = input("Enter new reason for visit: ").strip()

        if not name or not reason:
            print("Name and reason for visit cannot be empty.")
            return
        
        patient.update_record(name, age, reason)

    @classmethod
    def get_total_records_created(cls):
        return Patient.total_patients
    
    def run(self):
        while True:
            print("\n===== PATIENT RECORD MANAGEMENT SYSTEM =====")
            print("1. Add Patient")
            print("2. Display All Patients")
            print("3. Search Patient")
            print("4. Update Patient")
            print("5. View Total Records Created")
            print("6. Exit")

            choice = input("Choose an option (1-6): ").strip()

            if choice == "1":
                self.add_patient()

            elif choice == "2":
                self.display_all_records()

            elif choice == "3":
                self.search_patient()

            elif choice == "4":
                self.update_patient()

            elif choice == "5":
                print(
                    "Total patient records created:",
                    self.get_total_records_created()
                )

            elif choice == "6":
                print("Thank you for using the Patient Record Management System!")
                break

            else:
                print("Invalid option. Please choose a number from 1 to 6.")
                
if __name__ == "__main__":
    system = PatientRecordSystem()
    system.run()