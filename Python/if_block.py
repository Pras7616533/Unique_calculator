import main as ma
import function as fu


def if_block(code):
    choice = input("Enter your choice : ")
    if choice == "999":
        exit()

    if choice == "1":
        kg = float(input("Enter the weight in kilograms: "))
        print(
            f"{ma.bcd(kg,code)} kilograms is equal to {ma.bcd(fu.kilogramsToPounds(kg),code)} pounds."
        )

    elif choice == "2":
        lb = float(input("Enter the weight in pounds: "))
        print(
            f"{ma.bcd(lb,code)} pounds is equal to {ma.bcd(fu.poundsToKilograms(lb),code)} kilograms."
        )

    elif choice == "3":
        m = float(input("Enter the length in meters: "))
        print(
            f"{ma.bcd(m,code)} meters is equal to {ma.bcd(fu.metersToFeet(m),code)} feet."
        )

    elif choice == "4":
        ft = float(input("Enter the length in feet: "))
        print(
            f"{ma.bcd(ft,code)} feet is equal to {ma.bcd(fu.feetToMeters(ft),code)} meters."
        )

    elif choice == "5":
        li = float(input("Enter the volume in liters: "))
        print(
            f"{ma.bcd(li,code)} liters is equal to {ma.bcd(fu.litersToGallons(li),code)} gallons."
        )

    elif choice == "6":
        g = float(input("Enter the volume in gallons: "))
        print(
            f"{ma.bcd(g,code)} gallons is equal to {ma.bcd(fu.gallonsToLiters(g),code)} liters."
        )

    elif choice == "7":
        m = float(input("Enter the distance in miles: "))
        print(
            f"{ma.bcd(m,code)} miles is equal to {ma.bcd(fu.milesToKilometers(m),code)} kilometers."
        )

    elif choice == "8":
        k = float(input("Enter the distance in kilometers: "))
        print(
            f"{ma.bcd(k,code)} kilometers is equal to {ma.bcd(fu.kilometersToMiles(k),code)} miles."
        )

    elif choice == "9":
        inch = float(input("Enter the length in inches: "))
        print(
            f"{ma.bcd(inch,code)} inches is equal to {ma.bcd(fu.inchesToCentimeters(inch),code)} centimeters."
        )

    elif choice == "10":
        cm = float(input("Enter the length in centimeters: "))
        print(
            f"{ma.bcd(cm,code)} centimeters is equal to {ma.bcd(fu.centimetersToInches(cm),code)} inches."
        )

    elif choice == "11":
        yd = float(input("Enter the length in yards: "))
        print(
            f"{ma.bcd(yd,code)} yards is equal to {ma.bcd(fu.yardsToMeters(yd),code)} meters."
        )

    elif choice == "12":
        m = float(input("Enter the length in meters: "))
        print(
            f"{ma.bcd(m,code)} meters is equal to {ma.bcd(fu.metersToYards(m),code)} yards."
        )

    elif choice == "13":
        mm = float(input("Enter the length in millimeters: "))
        print(
            f"{ma.bcd(mm,code)} millimeters is equal to {ma.bcd(fu.millimetersToInches(mm),code)} inches."
        )

    elif choice == "14":
        inch = float(input("Enter the length in inches: "))
        print(
            f"{ma.bcd(inch)} inches is equal to {ma.bcd(fu.inchesToMillimeters(inch),code)} millimeters."
        )

    elif choice == "15":
        mm = float(input("Enter the length in millimeters: "))
        print(
            f"{ma.bcd(mm,code)} millimeters is equal to {ma.bcd(fu.millimetersToFeet(mm),code)} feet."
        )

    elif choice == "16":
        ft = float(input("Enter the length in feet: "))
        print(
            f"{ma.bcd(ft,code)} feet is equal to {ma.bcd(fu.feetToMillimeters(ft),code)} millimeters."
        )

    elif choice == "17":
        mm = float(input("Enter the length in millimeters: "))
        print(
            f"{ma.bcd(mm,code)} millimeters is equal to {ma.bcd(fu.millimetersToYards(mm),code)} yards."
        )

    elif choice == "18":
        yd = float(input("Enter the length in yards: "))
        print(
            f"{ma.bcd(yd,code)} yards is equal to {ma.bcd(fu.yardsToMillimeters(yd),code)} millimeters."
        )

    elif choice == "19":
        mm = float(input("Enter the length in millimeters: "))
        print(
            f"{ma.bcd(mm,code)} millimeters is equal to {ma.bcd(fu.millimetersToMiles(mm),code)} miles."
        )

    elif choice == "20":
        m = float(input("Enter the length in miles: "))
        print(
            f"{ma.bcd(m,code)} miles is equal to {ma.bcd(fu.milesToMillimeters(m),code)} millimeters."
        )

    elif choice == "21":
        a = int(input("Enter the number: "))
        b = int(input("Enter the number: "))
        print(
            f"The addition of {ma.bcd(a, code)} and {ma.bcd(b, code)} is {ma.bcd(fu.add(a, b), code)}"
        )

    elif choice == "22":
        a = int(input("Enter the number: "))
        b = int(input("Enter the number: "))
        print(
            f"The subtraction of {ma.bcd(a, code)} and {ma.bcd(b, code)} is {ma.bcd(fu.sub(a, b), code)}"
        )

    elif choice == "23":
        a = int(input("Enter the number: "))
        b = int(input("Enter the number: "))
        print(
            f"The multiplication of {ma.bcd(a, code)} and {ma.bcd(b, code)} is {ma.bcd(fu.mul(a, b), code)}"
        )

    elif choice == "24":
        a = int(input("Enter the number: "))
        b = int(input("Enter the number: "))
        print(
            f"The division of {ma.bcd(a, code)} and {ma.bcd(b, code)} is {ma.bcd(fu.div(a, b), code)}"
        )

    elif choice == "25":
        a = int(input("Enter the number: "))
        b = int(input("Enter the number: "))
        print(
            f"The power of {ma.bcd(a, code)} to {ma.bcd(b, code)} is {ma.bcd(fu.pow(a, b), code)}"
        )

    elif choice == "26":
        a = int(input("Enter the number: "))
        print(
            f"The square root of {ma.bcd(a, code)} is {ma.bcd(fu.squareroot(a), code)}"
        )

    elif choice == "27":
        a = int(input("Enter the number: "))
        print(
            f"The cube root of {ma.bcd(a, code)} is {ma.bcd(fu.cuberoot(a), code)}"
        )

    elif choice == "28":
        a = int(input("Enter the number: "))
        print(
            f"The factorial of {ma.bcd(a, code)} is {ma.bcd(fu.fact(a), code)}"
        )

    elif choice == "29":
        a = int(input("Enter the number: "))
        b = int(input("Enter the number: "))
        print(
            f"{ma.bcd(a, code)} choose {ma.bcd(b, code)} is {ma.bcd(fu.ncr(a, b), code)}"
        )

    elif choice == "30":
        a = int(input("Enter the number: "))
        b = int(input("Enter the number: "))
        print(
            f"The greatest common divisor of {ma.bcd(a, code)} and {ma.bcd(b, code)} is {ma.bcd(fu.gcd(a, b), code)}"
        )

    elif choice == "31":
        fu.table(int(input("Enter the number: ")), code)

    elif choice == "32":
        fu.square(int(input("Enter the number: ")), code)

    elif choice == "33":
        fu.cude(int(input("Enter the number: ")), code)

    else:
        print("Invalid choice. Please try again.")
