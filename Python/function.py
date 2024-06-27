import main as ma


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
    return a**b


def squareroot(a):
    return int(a**0.5)


def cuberoot(a):
    return int(a**(1 / 3))


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
        print(f"{ma.bcd(a, code)} × {ma.bcd(i, code)} = {ma.bcd(a * i, code)}")
        i += 1


def square(a, code, i=1):
    while i <= a:
        print(f"{ma.bcd(i, code)} × {ma.bcd(i, code)} = {ma.bcd(i * i, code)}")
        i += 1

def cude(a, code, i=1):
    while i <= a:
        print(f"{ma.bcd(i, code)} × {ma.bcd(i, code)} = {ma.bcd(i ** 3, code)}")
        i += 1


#Dictionaries
def kilogramsToPounds(kg):
    return kg * 2.20462


def poundsToKilograms(lb):
    return lb / 2.20462


def metersToFeet(m):
    return m * 3.28084


def feetToMeters(ft):
    return ft / 3.28084


def litersToGallons(l):
    return l / 3.78541


def gallonsToLiters(g):
    return g * 3.78541


def milesToKilometers(m):
    return m * 1.60934


def kilometersToMiles(k):
    return k / 1.60934


def inchesToCentimeters(inch):
    return inch * 2.54


def centimetersToInches(cm):
    return cm / 2.54


def yardsToMeters(yd):
    return yd * 0.9144


def metersToYards(m):
    return m / 0.9144


def millimetersToInches(mm):
    return mm / 25.4


def inchesToMillimeters(inch):
    return inch * 25.4


def millimetersToFeet(mm):
    return mm / 304.8


def feetToMillimeters(ft):
    return ft * 304.8


def millimetersToYards(mm):
    return mm / 914.4


def yardsToMillimeters(yd):
    return yd * 914.4


def millimetersToMiles(mm):
    return mm / 1609344


def milesToMillimeters(m):
    return m * 1609344
