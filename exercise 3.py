
# 1 Write a program that asks a fisher the length of a zander in centimeters. If the zander does not fulfill the size lim....

length = float(input("Enter the length of the zander in centimeter : "))

if length <= 41:
    print("The fish is below size limit. Please release the fish back to the lake.")
else:
    print("The fish is in size limit.")

# 2 Write a program that asks the user to enter the cabin class of a cruise ship and t.......

vars_class = str(input("Enter class cabin  : ")).upper()

if vars_class == "LUX":
    print("Upper-deck cabin with a balcony.")
elif vars_class == "A":
    print("Above the car deck, equipped with a window.")
elif vars_class == "B":
    print("Windowless cabin above the car deck")
elif vars_class == "C":
    print("Windowless cabin below the car deck.")
else:
    print("INVALID CABIN CLASS. Please enter valid cabin class ")

# 3 Write a program that asks for the biological gender and hemoglobin value (g/l). The program the notifies the user if the hemoglobin va....

gender = str(input('Enter Gender, "F" for female and "M" for male : ')).upper()

HG = float(input("Enter your Hemoglobin value : "))

if gender == "F":
    if HG <= 117:
        print("Your hemoglobin value is low ")
    elif HG >= 155:
        print("Your hemoglobin value is high")
    else:
        print("Your hemoglobin value is Normal")

elif gender == "M":
    if HG <= 134:
        print("Your hemoglobin value is low ")
    elif HG >= 167:
        print("Your hemoglobin value is high")
    else:
        print("Your hemoglobin value is Normal")

# 4.Write a program that asks the user to enter a year and notifies the user whether the input year is a leap...
leap_year = int(input("Enter year to check leap year: "))

if (leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0):
    print("leap year")
else:
    print(("not a leap year"))
