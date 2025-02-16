passport = int(input("Enter passport validity in months: "))
if passport < 1:
    print("Passport validity too short! Cannot board.")
    exit()
elif passport < 6:
    while True:
        dest = input("Enter destination type Domestic/Dom or International/Int: ").lower()
        if dest in ["dom", "int"] or dest in ["domestic", "international"]:
            break
        else:
            print("Invalid input. Please enter 'Domestic'/'Dom' or 'International'/'Int'.")

    if dest == "int":
        print("Passport validity less than 6 months! Cannot board international flights.")
        exit()
else:
    while True:
        dest = input("Domestic(dom)/International(int): ").lower()
        if dest in ["dom", "int"] or dest in ["domestic", "international"]:
            break
        else:
            print("Invalid input. Please enter 'Domestic'/'Dom' or 'International'/'Int'.")

if dest == "int" or dest == "international":
    visa = input("Do you have a visa? (Yes/No): ").lower()
    if visa == "n" or visa == "no":
        print("Visa required for international travel! Cannot board.")
        exit()

bweight = float(input("Enter baggage weight (kg): "))
bfee = 0
if bweight <= 20:
    bfee = 0
elif bweight <= 30:
    bfee = 20
elif bweight <= 40:
    bfee = 40
else:
    print("Baggage over 40 kg! Not allowed to board.")
    exit()

age = int(input("Enter passanger age: "))
if age < 2:
    ticket = "Infant ticket"
elif 2 <= age < 12:
    ticket = "Child ticket"
elif 12 <= age < 18:
    ticket = "Teen ticket"
else:
    ticket = "Adult ticket"

print("")
print(f"{ticket}")
if bfee == 0:
    print("Check-in successful!" " " "No extra fee for baggage." " " "Safe travels!")
else:
    print("Check-in successful!" " " f"Your baggage fee is {bfee} AZN." " " "Safe travels!")
