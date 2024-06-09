# Base Conversion Functions
def decimal_to_base32(decimal_number):
    if decimal_number == 0:
        return '0'
    base32_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUV"
    base32_str = ""
    while decimal_number > 0:
        remainder = decimal_number % 32
        base32_str = base32_chars[remainder] + base32_str
        decimal_number = decimal_number // 32
    return base32_str

def decimal_to_base64(decimal_number):
    if decimal_number == 0:
        return '0'
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    base64_str = ""
    while decimal_number > 0:
        remainder = decimal_number % 64
        base64_str = base64_chars[remainder] + base64_str
        decimal_number = decimal_number // 64
    return base64_str

def decimal_to_base24(decimal_number):
    if decimal_number == 0:
        return '0'
    base24_chars = "0123456789ABCDEFGHIJKLMN"
    base24_str = ""
    while decimal_number > 0:
        remainder = decimal_number % 24
        base24_str = base24_chars[remainder] + base24_str
        decimal_number = decimal_number // 24
    return base24_str

def decimal_to_base14(decimal_number):
    if decimal_number == 0:
        return '0'
    base14_chars = "0123456789ABCD"
    base14_str = ""
    while decimal_number > 0:
        remainder = decimal_number % 14
        base14_str = base14_chars[remainder] + base14_str
        decimal_number = decimal_number // 14
    return base14_str

def decimal_to_base12(decimal_number):
    if decimal_number == 0:
        return '0'
    base12_chars = "0123456789AB"
    base12_str = ""
    while decimal_number > 0:
        remainder = decimal_number % 12
        base12_str = base12_chars[remainder] + base12_str
        decimal_number = decimal_number // 12
    return base12_str

def decimal_to_base16(decimal_number):
    if decimal_number == 0:
        return '0'
    base16_chars = "0123456789ABCDEF"
    base16_str = ""
    while decimal_number > 0:
        remainder = decimal_number % 16
        base16_str = base16_chars[remainder] + base16_str
        decimal_number = decimal_number // 16
    return base16_str

# Binary Coded Decimal (BCD) Function
def bcd(n, code):
    if code == 0000:
        return str(n)
    elif code == 1010:
        return bin(n)[2:]
    elif code == 1212:
        return bin(n)[2:].zfill(4)
    elif code == 1023:
        return bin(n)[2:].zfill(6)
    elif code == 1234:
        return bin(n)[2:].zfill(8)
    elif code == 1298:
        return decimal_to_base12(n)
    elif code == 1462:
        return decimal_to_base14(n)
    elif code == 1636:
        return decimal_to_base16(n)
    elif code == 2412:
        return decimal_to_base24(n)
    elif code == 3268:
        return decimal_to_base32(n)
    elif code == 6486:
        return decimal_to_base64(n)

# Arithmetic Functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a // b

def pow(a, b):
    return a ** b

def squareroot(a):
    return int(a ** 0.5)

def cuberoot(a):
    return int(a ** (1 / 3))

def fact(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * fact(a - 1)

def ncr(n, r):
    if r == 0 or r == n:
        return 1
    elif r == 1:
        return n
    else:
        return fact(n) // (fact(r) * fact(n - r))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Table and Square Table Functions
def table(a, code, i=1):
    while i <= 10:
        print(f"{bcd(a, code)} × {bcd(i, code)} = {bcd(a * i, code)}")
        i += 1

def square(a, code, i=1):
    while i <= a:
        print(f"{bcd(i, code)} × {bcd(i, code)} = {bcd(i * i, code)}")
        i += 1

# Print View Functions
def print_view():
    print("0 for exit")
    print("1 for addition")
    print("2 for subtraction")
    print("3 for multiplication")
    print("4 for division")
    print("5 for power")
    print("6 for square root")
    print("7 for cube root")
    print("8 for factorial")
    print("9 for n choose r")
    print("10 for greatest common divisor")
    print("11 for table")
    print("12 for square table")

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

# Main Control Functions
def if_block(code):
    try:
        choice = int(input("Choose the option: "))
        if choice == 0:
            exit()
        elif choice == 1:
            a = int(input("Enter the number: "))
            b = int(input("Enter the number: "))
            print(f"The addition of {bcd(a, code)} and {bcd(b, code)} is {bcd(add(a, b), code)}")
        elif choice == 2:
            a = int(input("Enter the number: "))
            b = int(input("Enter the number: "))
            print(f"The subtraction of {bcd(a, code)} and {bcd(b, code)} is {bcd(sub(a, b), code)}")
        elif choice == 3:
            a = int(input("Enter the number: "))
            b = int(input("Enter the number: "))
            print(f"The multiplication of {bcd(a, code)} and {bcd(b, code)} is {bcd(mul(a, b), code)}")
        elif choice == 4:
            a = int(input("Enter the number: "))
            b = int(input("Enter the number: "))
            print(f"The division of {bcd(a, code)} and {bcd(b, code)} is {bcd(div(a, b), code)}")
        elif choice == 5:
            a = int(input("Enter the number: "))
            b = int(input("Enter the number: "))
            print(f"The power of {bcd(a, code)} to {bcd(b, code)} is {bcd(pow(a, b), code)}")
        elif choice == 6:
            a = int(input("Enter the number: "))
            print(f"The square root of {bcd(a, code)} is {bcd(squareroot(a), code)}")
        elif choice == 7:
            a = int(input("Enter the number: "))
            print(f"The cube root of {bcd(a, code)} is {bcd(cuberoot(a), code)}")
        elif choice == 8:
            a = int(input("Enter the number: "))
            print(f"The factorial of {bcd(a, code)} is {bcd(fact(a), code)}")
        elif choice == 9:
            a = int(input("Enter the number: "))
            b = int(input("Enter the number: "))
            print(f"{bcd(a, code)} choose {bcd(b, code)} is {bcd(ncr(a, b), code)}")
        elif choice == 10:
            a = int(input("Enter the number: "))
            b = int(input("Enter the number: "))
            print(f"The greatest common divisor of {bcd(a, code)} and {bcd(b, code)} is {bcd(gcd(a, b), code)}")
        elif choice == 11:
            table(int(input("Enter the number: ")), code)
        elif choice == 12:
            square(int(input("Enter the number: ")), code)
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

def decimal(code=0000):
    print("                 _-_-_-_-_-Decimal-_-_-_-_-_")
    print_view()
    if_block(code)

def binary(code=1010):
    print("                 _-_-_-_-_-Binary-_-_-_-_-_")
    print_view()
    if_block(code)

def quaternary(code=1212):
    print("                 _-_-_-_-_-Quaternary-_-_-_-_-_")
    print_view()
    if_block(code)

def senary(code=1023):
    print("                 _-_-_-_-_-Senary-_-_-_-_-_")
    print_view()
    if_block(code)

def octal(code=1234):
    print("                 _-_-_-_-_-Octal-_-_-_-_-_")
    print_view()
    if_block(code)

def duodecimal(code=1298):
    print("                 _-_-_-_-_-Duodecimal-_-_-_-_-_")
    print_view()
    if_block(code)

def quadrodecimal(code=1462):
    print("                 _-_-_-_-_-Quadrodecimal-_-_-_-_-_")
    print_view()
    if_block(code)

def hexadecimal(code=1636):
    print("                 _-_-_-_-_-Hexadecimal-_-_-_-_-_")
    print_view()
    if_block(code)

def quadravigesimal(code=2412):
    print("                 _-_-_-_-_-Quadravigesimal-_-_-_-_-_")
    print_view()
    if_block(code)

def duotrigesimal(code=3268):
    print("                 _-_-_-_-_-Duotrigesimal-_-_-_-_-_")
    print_view()
    if_block(code)

def tetrasexagesimal(code=6486):
    print("                 _-_-_-_-_-Tetrasexagesimal-_-_-_-_-_")
    print_view()
    if_block(code)

def if_main_block():
    try:
        choice_main = int(input("Choose the option: "))
        if choice_main == 999:
            exit()
        elif choice_main == 0:
            decimal()
        elif choice_main == 1:
            binary()
        elif choice_main == 2:
            quaternary()
        elif choice_main == 3:
            senary()
        elif choice_main == 4:
            octal()
        elif choice_main == 5:
            duodecimal()
        elif choice_main == 6:
            quadrodecimal()
        elif choice_main == 7:
            hexadecimal()
        elif choice_main == 8:
            quadravigesimal()
        elif choice_main == 9:
            duotrigesimal()
        elif choice_main == 10:
            tetrasexagesimal()
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

def main():
    print_main()
    print("\n\n\n\n")
    if_main_block()

if __name__ == "__main__":
    main()
