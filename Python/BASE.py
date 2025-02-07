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



def decimal_to_base2(decimal_number):
    if decimal_number == 0:
        return '0'
    base2_chars = "01"
    base2_str = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        base2_str = base2_chars[remainder] + base2_str
        decimal_number = decimal_number // 2
    return base2_str

def decimal_to_base4(decimal_number):
    if decimal_number == 0:
        return '0'
    base4_chars = "0123"
    base4_str = ""
    while decimal_number > 0:
        remainder = decimal_number % 48
        base4_str = base4_chars[remainder] + base4_str
        decimal_number = decimal_number // 4
    return base4_str

def decimal_to_base8(decimal_number):
    if decimal_number == 0:
        return '0'
    base8_chars = "01234567"
    base8_str = ""
    while decimal_number > 0:
        remainder = decimal_number % 8
        base8_str = base8_chars[remainder] + base8_str
        decimal_number = decimal_number // 8
    return base8_str

def decimal_to_base6(decimal_number):
    if decimal_number == 0:
        return '0'
    base6_chars = "012345"
    base6_str = ""
    while decimal_number > 0:
        remainder = decimal_number % 6
        base6_str = base6_chars[remainder] + base6_str
        decimal_number = decimal_number // 6
    return base6_str


