import BASE as base
import Base_code as bc


def bcd(n, code):
    if code == 0000:
        return str(n)
    elif code == 1010:
        return base.decimal_to_base2(n)
    elif code == 1212:
        return base.decimal_to_base4(n)
    elif code == 1023:
        return base.decimal_to_base6(n)
    elif code == 1234:
        return base.decimal_to_base8(n)
    elif code == 1298:
        return base.decimal_to_base12(n)
    elif code == 1462:
        return base.decimal_to_base14(n)
    elif code == 1636:
        return base.decimal_to_base16(n)
    elif code == 2412:
        return base.decimal_to_base24(n)
    elif code == 3268:
        return base.decimal_to_base32(n)
    elif code == 6486:
        return base.decimal_to_base64(n)


def print_main():
    print("0 for base-10 or decimal")
    print("1 for base-2 or binary")
    print("2 for base-4 or Quaternary")
    print("3 for base-6 or Senary")
    print("4 for base-8 or octal")
    print("5 for base-12 or Duodecimal")
    print("6 for base-14 or quadrodecimal")
    print("7 for base-16 or Hexadecimal")
    print("8 for base-24 or Quadravigesimal")
    print("9 for base-32 or Duotrigesimal")
    print("10 for base-64 or Tetrasexagesimal")
    print("999 for exit")


def if_main_block():
    try:
        choice_main = int(input("Choose the option: "))
        if choice_main == 999:
            exit()
        elif choice_main == 0:
            bc.decimal()
        elif choice_main == 1:
            bc.binary()
        elif choice_main == 2:
            bc.quaternary()
        elif choice_main == 3:
            bc.senary()
        elif choice_main == 4:
            bc.octal()
        elif choice_main == 5:
            bc.duodecimal()
        elif choice_main == 6:
            bc.quadrodecimal()
        elif choice_main == 7:
            bc.hexadecimal()
        elif choice_main == 8:
            bc.quadravigesimal()
        elif choice_main == 9:
            bc.duotrigesimal()
        elif choice_main == 10:
            bc.tetrasexagesimal()
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

def main():
    print("\n\n\n\n\n")
    print_main()
    if_main_block()

if __name__ == "__main__":
    main()
