medical_cause = input("did you have any medical cause? (yes/no): ")
# take input of attendance
atten = input("Enter your attendance percentage: ")

# check if attendance is less than 75%
if medical_cause == "yes":
    print("You are allowed.")  # checking the condition 1
else:
    if int(atten) >= 75:
        print("You are allowed.")
    else:
        print("You are not allowed.")  # checking the condition 2

        # actovity 2

        # electricity bill calculation
units = int(input("Enter the number of units consumed: "))

if units < 50:
    amount = units * 2.60
    surcharge = 25
elif units <= 100:
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35
elif units <= 200:
    amount = 292.5 + ((units - 100) * 5.26)
    surcharge = 45
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

    total = amount + surcharge
    print("\nElectricity Bill = %.2f" % total)

    # activity 3

print("select your ride")
print("1. auto")
print("2. taxi")

    #select your ride
ride = int(input("Enter your choice: "))

if(ride == 1):
    print("You have selected auto")
elif ride == 2:
    print("you have selected taxi")

print("what type of auto you want?")
print("1. normal")
print("2. luxury")
if ride == 1:
    auto_type = int(input("Enter your choice: "))
    if auto_type == 1:
        print("You have selected normal auto")
    elif auto_type == 2:
        print("You have selected luxury auto")

print("what type of taxi you want?")
print("1. normal")
print("2. luxury")
elif ride == 2:
    taxi_type = int(input("Enter your choice: "))
    if taxi_type == 1:
        print("You have selected normal taxi")
    elif taxi_type == 2:
        print("You have selected luxury taxi")