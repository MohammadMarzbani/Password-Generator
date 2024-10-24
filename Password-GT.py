# Hello this project password generate
import random
import string
import csv

passw = []
sath = []
password = []


def generate_id():
    if passw:
        last_id = int(passw[-1]['ID'])
        return str(last_id + 1)
    else:
        return "1"


def hard():
    t = string.ascii_letters + string.digits + string.punctuation
    generate = "".join(random.sample(t, 16))
    return generate


def easy():
    t = string.ascii_letters
    generate = "".join(random.sample(t, 16))
    return generate


def normal():
    t = string.ascii_letters + string.digits
    generate = "".join(random.sample(t, 16))
    return generate


def open_file():
    try:
        with open("Data/password.csv", "r") as data:
            show = csv.DictReader(data)
            for row in show:
                passw.append(row)
    except FileNotFoundError:
        print("File not found")


def save_contact():
    with open("Data/password.csv", "w", newline="") as data:
        header = ['ID', 'Name', 'Password', 'Application', 'Sath']
        writer = csv.DictWriter(data, fieldnames=header)
        writer.writeheader()
        writer.writerows(passw)


def create_password():
    print("Add Password List Menu:")
    name = input("Name: ").strip()
    password = input("What is your password level? (Hard / Normal / Easy): ").strip()
    if password == "Hard":
        sath = hard()

    elif password == "Normal":
        sath = normal()
    elif password == "Easy":
        sath = easy()
    else:
        print("Invalid password level!")
    application = input("Application: ").strip()

    id_ = generate_id()

    contact = {"ID": id_, "Name": name, "Password": sath, "Application": application, "Sath": password}

    passw.append(contact)
    save_contact()
    print(f"Password for User: {name} Added Successfully with ID: {id_}")


def update_contact():
    admin = input("Are you an admin? Please enter your username: ")
    pwadmin = input("Please insert your password: ")
    if admin == "Admin" and pwadmin == "Admin":
        print("Update Password Menu")
        uname = input("Please insert User ID for update: ").strip()
        for pw in passw:
            if pw['ID'] == uname:
                print("-" * 31)
                print(f"This ID {uname} owned by {pw['Name']}")
                print(f"ID: {pw['ID']} ")
                print(f"Name: {pw['Name']} ")
                print(f"Password: {pw['Password']} ")
                print(f"Application: {pw['Application']} ")
                print("-" * 31)

                ask = input("Which to change: (Name / Password / Application) ").strip()

                if ask == "Name":
                    pw['Name'] = input("New Name: ")
                    print(f"User Name Changed Successfully")
                    print(f"New Name: {pw['Name']} ")
                elif ask == "Password":
                    password1 = input("Please Insert Level Password: ")
                    if password1 == "Hard":
                        sath = hard()

                    elif password1 == "Normal":
                        sath = normal()
                    elif password1 == "Easy":
                        sath = easy()
                    else:
                        print("Invalid password level!")
                    pw['Password'] = sath


                elif ask == "Application":
                    pw['Application'] = input("New Application: ")

                else:
                    print("Error: Wrong parameter (Name / Password / Application)")
                save_contact()
                return
    else:
        print("You are not an admin!")
        print("Contact Not Found")


def view_contact():
    admin = input("Are you an admin? Please enter your username:")
    pwadmin = input("Please insert your password: ")
    if admin == "Admin" and pwadmin == "Admin":
        print("Your Password list: ")
        print("-" * 30)
        for pw in passw:
            print(f"ID: {pw['ID']} ")
            print(f"Name: {pw['Name']} ")
            print(f"Password: {pw['Password']} ")
            print(f"Application: {pw['Application']} ")
            print(f"Sath: {pw['Sath']} ")
            print("-" * 30)
    else:
        print("You are not an admin!")



open_file()
while True:
    print("Hello to Generate Password Application")
    print("1.Create Password.")
    print("2.View Password list (for admin).")
    print("3.Update Password list (for admin).")
    print("4.Exit")
    choice = input("Enter Your Choice: ")
    if choice == "1":
        create_password()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        print("Thank you for using my application")
        break
