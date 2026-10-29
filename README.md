Patient Record Management System

1. Project Overview

The Patient Record Management System is a simple Python application developed for the Object-Oriented Programming (OOP1) assignment. The system helps users create, display, search, and update patient records through a menu-driven interface.

The project demonstrates how object-oriented programming can be used to organise information and perform basic record management tasks.

2. Objectives

The main objectives of this project are to:

* Apply object-oriented programming concepts in Python.
* Create classes and objects to represent patients and manage records.
* Store multiple patient records in a list.
* Add, search, display, and update patient information.
* Demonstrate instance methods, a class method, and a static method.
* Practise input validation and error handling.

3. Technologies Used

* Programming language: Python
* Code editor: Visual Studio Code
* Interface: Command-line menu
* Data storage: Python list in computer memory

4. Main Features

The system allows users to:

1. Add a new patient record.
2. Display all patient records.
3. Search for a patient using their ID.
4. Update an existing patient’s information.
5. View the total number of patient records created during the current program session.
6. Exit the application.

5. Object-Oriented Programming Concepts

Patient Class

The Patient class represents an individual patient. It stores the patient’s ID, name, age, and reason for visiting the clinic.

PatientRecordSystem Class

The PatientRecordSystem class manages the collection of patient records. It contains methods for adding, displaying, searching, and updating records.

Instance Methods

Instance methods work with individual objects or the data stored in a particular system object. Examples include display_info(), add_patient(), and update_patient().

Class Method

The get_total_records_created() class method returns the total number of patient objects created during the current program session.

Static Method

The is_valid_age() static method checks whether a patient’s age is zero or greater.

List

The system uses a list to store patient objects. This makes it possible to manage multiple records within the same program session.

6. How to Run the Program

1. Install Python on your computer if it is not already installed.
2. Open Visual Studio Code.
3. Open the Patient_Record_Management_System project folder.
4. Open patient_record_management.py.
5. Open the VS Code terminal by selecting Terminal → New Terminal.
6. Enter the following command:
    python patient_record_management.py
7. Press Enter to start the program.

If the command does not work on Windows, try:

py patient_record_management.py

Follow the menu instructions to use the system.

7. Input Validation

The program checks that the age entered is a valid number and is not negative. It also checks that the patient’s name and reason for visiting are not empty. Invalid menu choices and patient IDs are handled with appropriate messages.

8. Limitations

The current version stores records in memory rather than in a permanent database or file. Therefore, the records are lost when the program closes. The application is designed for learning and demonstration and is not intended for storing real medical information.

9. Possible Future Improvements

Future versions could include a database for permanent storage, login and access controls, deletion of records, a graphical user interface, and more detailed reporting features. Appropriate privacy and security measures would be necessary before using a system like this in a real healthcare environment.

10. Conclusion

The Patient Record Management System demonstrates the practical use of Python classes, objects, lists, methods, and input validation. It provides a foundation for understanding how object-oriented programming can be applied to a simple record management task.

Note: Use fictional patient information when testing this project.
