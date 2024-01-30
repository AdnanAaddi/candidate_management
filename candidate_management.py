def add_candidate(user_date):
    email = input("Please Enter your email ")
    if email in user_data:
        print("Candidate Already Exists with this email")
        return
    name = input("Enter Candidate Name: ")
    age = int(input("Enter Candidate Age: "))
    address = input("Enter the Candidate Address: ")
    user_data[email] = {"name": name, "age": age, "address": address}
    print("Data added successfully!")

user_data= {}
while True:
    print("1. For Data Addition ")
    print("2. For Data Removal ")
    print("3. For Data Searching ")
    print("5. Display all data ")
    print("4. For Exit ")
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        add_candidate(user_data)
