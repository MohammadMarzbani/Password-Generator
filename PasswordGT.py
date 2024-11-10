# Hello this project password generate
import random
import string
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import email
from datetime import datetime
import pytz

passwordlist = []
password_level = []
user_password = []

def time():
    timezone = pytz.timezone('Asia/Tehran')
    time = datetime.now(timezone)
    duration = time.strftime("%Y-%m-%d %H:%M:%S")
    return duration

def generate_id():
    if passwordlist:
        last_id = int(passwordlist[-1]['ID'])
        return str(last_id + 1)
    else:
        return "1"


def hard():
    characterlength = int(input("How many characters do you want? "))
    t = string.ascii_letters + string.digits + string.punctuation
    generate = "".join(random.sample(t,  characterlength))
    return generate


def easy():
    characterlength = int(input("How many characters do you want? "))
    t = string.ascii_letters
    generate = "".join(random.sample(t, characterlength))
    return generate


def normal():
    characterlength = int(input("How many characters do you want? "))
    t = string.ascii_letters + string.digits
    generate = "".join(random.sample(t, characterlength))
    return generate


def open_file():
    try:
        with open("Data/password.csv", "r") as data:
            show = csv.DictReader(data)
            for row in show:
                passwordlist.append(row)
    except FileNotFoundError:
        print("File not found")


def save_password():
    with open("Data/password.csv", "w", newline="") as data:
        header = ['ID','CreationTime', 'Name', 'Password', 'Application', 'PasswordLevel', 'Gmail']
        writer = csv.DictWriter(data, fieldnames=header)
        writer.writeheader()
        writer.writerows(passwordlist)


def create_password():
    print("Add Password List Menu:")
    name = input("Name: ").strip()
    user_password = input("What is your password password level? (1-Hard / 2-Normal / 3-Easy): ").strip()
    create_password_level = []
    if user_password == "Hard" or user_password == "hard" or user_password == "1":
        create_password_level = hard()
        if user_password == "1":
            user_password = "Hard"
    elif user_password == "Normal" or user_password == "normal" or user_password == "2":
        create_password_level = normal()
        if user_password == "2":
            user_password = "Normal"
    elif user_password == "Easy" or user_password == "easy" or user_password == "3":
        create_password_level = easy()
        if user_password == "3":
            user_password = "Easy"
    else:
        print("Invalid password password_level!")
    application = input("Application: ").strip()
    user_email = input("Enter your email: ").strip()
    id_ = generate_id()

    contact = {"ID": id_,'Time':time() ,"Name": name, "Password": create_password_level, "Application": application, "PasswordLevel": user_password.capitalize() ,"Gmail":user_email}

    passwordlist.append(contact)
    save_password()
    print(f"Password for User: {name} Added Successfully with ID: {id_}")
    subject = f"Your password has been generated sir {name}"
    body = f"Creation time:{time()}\nID {id_}\nName: {name} \nPassword: {create_password_level} \nApplication: {application} \nPasswordLevel:{user_password.capitalize()}\nGmail: {user_email}"
    send_smtp_email(subject,body,user_email)


def send_smtp_email(subject, body,gmail):
    smtp_server = email['Host']
    smtp_port = 465
    username = email['user']
    password = email['password']

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = gmail
    msg['Subject'] = subject

    body = body
    msg.attach(MIMEText(body, 'plain'))
    server = None
    try:

        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(username, password)
        server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        if server is not None:
            server.quit()

def update_password():
    admin = input("Are you an admin? Please enter your username: ")
    adminpassword = input("Please insert your password: ")
    if admin == "Admin" and adminpassword == "Admin":
        print("Update Password Menu")
        uname = input("Please insert User ID for update: ").strip()
        for pw in passwordlist:
            if pw['ID'] == uname:
                print("-" * 31)
                print(f"This ID {uname} owned by {pw['Name']}")
                print(f"ID: {pw['ID']} ")
                print(f"Name: {pw['Name']} ")
                print(f"Password: {pw['Password']} ")
                print(f"Application: {pw['Application']} ")
                print("-" * 31)

                ask = input("Which to change: (1-Name / 2-Password / 3-Application) ").strip()

                if ask == "Name" or ask == "name" or ask == "1":
                    pw['Name'] = input("New Name: ")
                    print(f"User Name Changed Successfully")
                    print(f"New Name: {pw['Name']} ")
                elif ask == "Password" or ask == "password" or ask == "2":
                    user_password_level = ["Hard", "Normal", "Easy"]
                    password_for_update = input("Please Insert Level Password: (1-Hard / 2-Normal / 3-Easy) ").strip()
                    if password_for_update == "Hard" or password_for_update == "hard" or password_for_update == "1":
                        user_password_level = hard()
                        if password_for_update == "1":
                            password_for_update = "Hard"
                    elif password_for_update == "Normal" or password_for_update == "normal" or password_for_update == "2":
                        user_password_level = normal()
                        if password_for_update == "2":
                            password_for_update = "Normal"
                    elif password_for_update == "Easy" or password_for_update == "easy" or password_for_update == "3":
                        user_password_level = easy()
                        if password_for_update == "3":
                            password_for_update = "Easy"
                    else:
                        print("Invalid password password level!")
                    pw['Password'] = user_password_level
                    pw['PasswordLevel'] = password_for_update.capitalize()


                elif ask == "Application" or ask == "application" or ask == "3":
                    pw['Application'] = input("New Application: ")

                else:
                    print("Error: Wrong parameter (Name / Password / Application)")
                save_password()
                return
    else:
        print("You are not an admin!")


def view_password():
    admin = input("Are you an admin? Please enter your username:")
    adminpassword = input("Please insert your password: ")
    if admin == "Admin" and adminpassword == "Admin":
        print("Your Password list: ")
        print("-" * 30)
        for pw in passwordlist:
            print(f"ID: {pw['ID']} ")
            print(f"Name: {pw['Name']} ")
            print(f"Password: {pw['Password']} ")
            print(f"Application: {pw['Application']} ")
            print(f"password level: {pw['password_level']} ")
            print(f"Gmail: {pw['Gmail']} ")
            print("-" * 30)
    else:
        print("You are not an admin!")



open_file()
while True:

    print("Current time in Tehran:",time())
    print("Hello to Generate Password Application")
    print("1.Create Password.")
    print("2.View Password list (for admin).")
    print("3.Update Password list (for admin).")
    print("4.Exit")
    choice = input("Enter Your Choice: ")
    if choice == "1" or choice == "Create Password":
        create_password()
    elif choice == "2" or choice == "View Password":
        view_password()
    elif choice == "3" or choice == "Update Password":
        update_password()
    elif choice == "4" or choice == "Exit":
        print("Thank you for using my application")
        break
