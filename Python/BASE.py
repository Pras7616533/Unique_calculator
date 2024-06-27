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
