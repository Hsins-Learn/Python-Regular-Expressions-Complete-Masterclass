import re

#Asking the user for the first name and checking the format
while True:
    fname = input("\nPlease enter your First Name: ")

    check = re.fullmatch(r"[A-Z][a-z]+", fname)

    if check == None:
        print("Wrong format! Please try again.")
        continue
    else:
        break

#Asking the user for the last name and checking the format
while True:
    lname = input("\nPlease enter your Last Name: ")

    check = re.fullmatch(r"[A-Z][a-z]+", lname)

    if check == None:
        print("Wrong format! Please try again.")
        continue
    else:
        break

#Asking the user for the date of birth and checking the format
while True:
    date = input("\nPlease enter your Date of Birth (mm/dd/yyyy): ")

    check = re.fullmatch(r"(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/(19[0-9][0-9]|200[01])", date)

    if check == None:
        print("Wrong format! Please try again.")
        continue
    else:
        break

#Asking the user for the email address and checking the format
while True:
    email = input("\nPlease enter your Email Address: ")

    check = re.fullmatch(r"(\w|\.)+@[a-z]+\.[a-z]{2,4}", email)

    if check == None:
        print("Wrong format! Please try again.")
        continue
    else:
        break

#Asking the user for the username and checking the format
while True:
    user = input("\nPlease enter your Username: ")

    check = re.fullmatch(r"\w{6,12}", user)

    if check == None:
        print("Wrong format! Please try again.")
        continue
    else:
        break

#Asking the user for the password and checking the format
while True:
    passw = input("\nPlease enter your Password: ")

    check = re.fullmatch(r"^[a-z](?=.{7,})(?=.*[A-Z])(?=.*\d)(?=.*[$&?!%])[a-zA-Z0-9$&?!%]+$", passw)

    if check == None:
        print("Wrong format! Please try again.")
        continue
    else:
        break

#Asking the user for the credit card number and checking the format
while True:
    ccnum = input("\nPlease enter your Credit Card Number (no spaces): ")

    check = re.fullmatch(r"^(4|5)\d{15}", ccnum)

    if check == None:
        print("Wrong format! Please try again.")
        continue
    else:
        break

#Asking the user for the credit card expiration date and checking the format
while True:
    ccdat = input("\nPlease enter your Credit Card Expiration Date (mm/yy): ")

    check = re.fullmatch(r"(0[5-9]|1[0-2])/24|(0[1-9]|1[0-2])/(2[5-9]|[3-9][0-9])", ccdat)

    if check == None:
        print("Wrong format! Please try again.")
        continue
    else:
        break

#Asking the user for the credit card verification code and checking the format
while True:
    cccvc = input("\nPlease enter your Credit Card Verification Code: ")

    check = re.fullmatch(r"\d{3}", cccvc)

    if check == None:
        print("Wrong format! Please try again.")
        continue
    else:
        break

userinfo = ["First Name: " + fname,
            "Last Name: " + lname,
            "Date of birth: " + date,
            "Email address: " + email,
            "Username: " + user,
            "Password: " + passw,
            "Card number: " + ccnum,
            "Expiration date: " + ccdat,
            "CVC: " + cccvc]

string = "\n".join(userinfo)

print(f"This is your user account information:\n\n{string}")