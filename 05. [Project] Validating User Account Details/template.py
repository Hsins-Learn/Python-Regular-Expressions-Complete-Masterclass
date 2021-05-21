import re

#Asking the user for the first name and checking the format
while True:
    fname = input("\nPlease enter your First Name: ")

    check = re.fullmatch(r"", fname)

    if check == None:
        print("Wrong format! Please try again.")
        continue
    else:
        break

#Asking the user for the last name and checking the format
while True:
    lname = input("\nPlease enter your Last Name: ")

    check = re.fullmatch(r"", lname)

    if check == None:
        print("Wrong format! Please try again.")
        continue
    else:
        break

#Asking the user for the date of birth and checking the format
while True:
    date = input("\nPlease enter your Date of Birth (mm/dd/yyyy): ")

    check = re.fullmatch(r"", date)

    if check == None:
        print("Wrong format! Please try again.")
        continue
    else:
        break

#Asking the user for the email address and checking the format
while True:
    email = input("\nPlease enter your Email Address: ")

    check = re.fullmatch(r"", email)

    if check == None:
        print("Wrong format! Please try again.")
        continue
    else:
        break

#Asking the user for the username and checking the format
while True:
    user = input("\nPlease enter your Username: ")

    check = re.fullmatch(r"", user)

    if check == None:
        print("Wrong format! Please try again.")
        continue
    else:
        break

#Asking the user for the password and checking the format
while True:
    passw = input("\nPlease enter your Password: ")

    check = re.fullmatch(r"", passw)

    if check == None:
        print("Wrong format! Please try again.")
        continue
    else:
        break

#Asking the user for the credit card number and checking the format
while True:
    ccnum = input("\nPlease enter your Credit Card Number (no spaces): ")

    check = re.fullmatch(r"", ccnum)

    if check == None:
        print("Wrong format! Please try again.")
        continue
    else:
        break

#Asking the user for the credit card expiration date and checking the format
while True:
    ccdat = input("\nPlease enter your Credit Card Expiration Date (mm/yy): ")

    check = re.fullmatch(r"", ccdat)

    if check == None:
        print("Wrong format! Please try again.")
        continue
    else:
        break

#Asking the user for the credit card verification code and checking the format
while True:
    cccvc = input("\nPlease enter your Credit Card Verification Code: ")

    check = re.fullmatch(r"", cccvc)

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

print("This is your user account information: \n\n" + string)