import main as ma
import function as fu
import db
import Print_view as pv


def if_block(code):
    while True:
        pv.print_view()
        choice = input("Enter your choice : ")
        if choice == "999":
            ma.main()

        if choice == "2007":
            db.fread()

        elif choice == "1":
            a = int(input("Enter the number: "))
            b = int(input("Enter the number: "))
            r = f"The addition of {ma.bcd(a, code)} and {ma.bcd(b, code)} is {ma.bcd(fu.add(a, b), code)}"
            db.fwrite(r)
            print(r)

        elif choice == "2":
            a = int(input("Enter the number: "))
            b = int(input("Enter the number: "))
            r = f"The subtraction of {ma.bcd(a, code)} and {ma.bcd(b, code)} is {ma.bcd(fu.sub(a, b), code)}"
            db.fwrite(r)
            print(r)

        elif choice == "3":
            a = int(input("Enter the number: "))
            b = int(input("Enter the number: "))
            r = f"The multiplication of {ma.bcd(a, code)} and {ma.bcd(b, code)} is {ma.bcd(fu.mul(a, b), code)}"
            db.fwrite(r)
            print(r)

        elif choice == "4":
            a = int(input("Enter the number: "))
            b = int(input("Enter the number: "))
            r = f"The division of {ma.bcd(a, code)} and {ma.bcd(b, code)} is {ma.bcd(fu.div(a, b), code)}"
            db.fwrite(r)
            print(r)

        elif choice == "5":
            a = int(input("Enter the number: "))
            b = int(input("Enter the number: "))
            r = f"The power of {ma.bcd(a, code)} to {ma.bcd(b, code)} is {ma.bcd(fu.pow(a, b), code)}"
            db.fwrite(r)
            print(r)

        elif choice == "6":
            a = int(input("Enter the number: "))
            r = f"The square root of {ma.bcd(a, code)} is {ma.bcd(fu.squareroot(a), code)}"
            db.fwrite(r)
            print(r)

        elif choice == "7":
            a = int(input("Enter the number: "))
            r = f"The cube root of {ma.bcd(a, code)} is {ma.bcd(fu.cuberoot(a), code)}"
            db.fwrite(r)
            print(r)

        elif choice == "8":
            a = int(input("Enter the number: "))
            r = f"The factorial of {ma.bcd(a, code)} is {ma.bcd(fu.fact(a), code)}"
            db.fwrite(r)
            print(r)

        elif choice == "9":
            a = int(input("Enter the number: "))
            b = int(input("Enter the number: "))
            r = f"{ma.bcd(a, code)} choose {ma.bcd(b, code)} is {ma.bcd(fu.ncr(a, b), code)}"
            db.fwrite(r)
            print(r)

        elif choice == "10":
            a = int(input("Enter the number: "))
            b = int(input("Enter the number: "))
            r = f"The greatest common divisor of {ma.bcd(a, code)} and {ma.bcd(b, code)} is {ma.bcd(fu.gcd(a, b), code)}"
            db.fwrite(r)
            print(r)

        elif choice == "11":
            fu.table(int(input("Enter the number: ")), code)

        elif choice == "12":
            fu.square(int(input("Enter the number: ")), code)

        elif choice == "13":
            fu.cude(int(input("Enter the number: ")), code)

        if choice == "14":
            if_meger(code)

        else:
            print("Invalid choice. Please try again.")


def if_meger(code):
    pv.meger()
    choice = input("Enter your choice : ")
    if choice == "1":
        kg = float(input("Enter the weight in kilograms: "))
        r = f"{ma.bcd(kg,code)} kilograms is equal to {ma.bcd(fu.kilogramsToPounds(kg),code)} pounds."
        db.fwrite(r)
        print(r)
    elif choice == "2":
        lb = float(input("Enter the weight in pounds: "))
        r = f"{ma.bcd(lb,code)} pounds is equal to {ma.bcd(fu.poundsToKilograms(lb),code)} kilograms."
        db.fwrite(r)
        print(r)
    elif choice == "3":
        m = float(input("Enter the length in meters: "))
        r = f"{ma.bcd(m,code)} meters is equal to {ma.bcd(fu.metersToFeet(m),code)} feet."
        db.fwrite(r)
        print(r)
    elif choice == "4":
        ft = float(input("Enter the length in feet: "))
        r = f"{ma.bcd(ft,code)} feet is equal to {ma.bcd(fu.feetToMeters(ft),code)} meters."
        db.fwrite(r)
        print(r)
    elif choice == "5":
        li = float(input("Enter the volume in liters: "))
        r = f"{ma.bcd(li,code)} liters is equal to {ma.bcd(fu.litersToGallons(li),code)} gallons."
        db.fwrite(r)
        print(r)
    elif choice == "6":
        g = float(input("Enter the volume in gallons: "))
        r = f"{ma.bcd(g,code)} gallons is equal to {ma.bcd(fu.gallonsToLiters(g),code)} liters."
        db.fwrite(r)
        print(r)
    elif choice == "7":
        m = float(input("Enter the distance in miles: "))
        r = f"{ma.bcd(m,code)} miles is equal to {ma.bcd(fu.milesToKilometers(m),code)} kilometers."
        db.fwrite(r)
        print(r)
    elif choice == "8":
        k = float(input("Enter the distance in kilometers: "))
        r = f"{ma.bcd(k,code)} kilometers is equal to {ma.bcd(fu.kilometersToMiles(k),code)} miles."
        db.fwrite(r)
        print(r)
    elif choice == "9":
        inch = float(input("Enter the length in inches: "))
        r = f"{ma.bcd(inch,code)} inches is equal to {ma.bcd(fu.inchesToCentimeters(inch),code)} centimeters."
        db.fwrite(r)
        print(r)
    elif choice == "10":
        cm = float(input("Enter the length in centimeters: "))
        r = f"{ma.bcd(cm,code)} centimeters is equal to {ma.bcd(fu.centimetersToInches(cm),code)} inches."
        db.fwrite(r)
        print(r)
    elif choice == "11":
        yd = float(input("Enter the length in yards: "))
        r = f"{ma.bcd(yd,code)} yards is equal to {ma.bcd(fu.yardsToMeters(yd),code)} meters."
        db.fwrite(r)
        print(r)
    elif choice == "12":
        m = float(input("Enter the length in meters: "))
        r = f"{ma.bcd(m,code)} meters is equal to {ma.bcd(fu.metersToYards(m),code)} yards."
        db.fwrite(r)
        print(r)
    elif choice == "13":
        mm = float(input("Enter the length in millimeters: "))
        r = f"{ma.bcd(mm,code)} millimeters is equal to {ma.bcd(fu.millimetersToInches(mm),code)} inches."
        db.fwrite(r)
        print(r)
    elif choice == "14":
        inch = float(input("Enter the length in inches: "))
        r = f"{ma.bcd(inch)} inches is equal to {ma.bcd(fu.inchesToMillimeters(inch),code)} millimeters."
        db.fwrite(r)
        print(r)
    elif choice == "15":
        mm = float(input("Enter the length in millimeters: "))
        r = f"{ma.bcd(mm,code)} millimeters is equal to {ma.bcd(fu.millimetersToFeet(mm),code)} feet."
        db.fwrite(r)
        print(r)
    elif choice == "16":
        ft = float(input("Enter the length in feet: "))
        r = f"{ma.bcd(ft,code)} feet is equal to {ma.bcd(fu.feetToMillimeters(ft),code)} millimeters."
        db.fwrite(r)
        print(r)
    elif choice == "17":
        mm = float(input("Enter the length in millimeters: "))
        r = f"{ma.bcd(mm,code)} millimeters is equal to {ma.bcd(fu.millimetersToYards(mm),code)} yards."
        db.fwrite(r)
        print(r)
    elif choice == "18":
        yd = float(input("Enter the length in yards: "))
        r = f"{ma.bcd(yd,code)} yards is equal to {ma.bcd(fu.yardsToMillimeters(yd),code)} millimeters."
        db.fwrite(r)
        print(r)
    elif choice == "19":
        mm = float(input("Enter the length in millimeters: "))
        r = f"{ma.bcd(mm,code)} millimeters is equal to {ma.bcd(fu.millimetersToMiles(mm),code)} miles."
        db.fwrite(r)
        print(r)
    elif choice == "20":
        m = float(input("Enter the length in miles: "))
        r = f"{ma.bcd(m,code)} miles is equal to {ma.bcd(fu.milesToMillimeters(m),code)} millimeters."
        db.fwrite(r)
        print(r)
