The script you provided is a comprehensive calculator that can perform various arithmetic operations and conversions
between different numerical bases. It includes functions for addition, subtraction, multiplication, division, 
exponentiation, square roots, cube roots, factorials, combinations (nCr), greatest common divisors, multiplication tables,
and squares. Additionally, it supports conversions to and from several numerical bases, including binary, quaternary, 
senary, octal, duodecimal, quadrodecimal, hexadecimal, quadravigesimal, duotrigesimal, and tetrasexagesimal.

Here’s a brief breakdown of how the script is organized and how it operates:

### Base Conversion Functions
These functions convert a decimal number to a specified base:
- `decimal_to_base32(decimal_number)`
- `decimal_to_base64(decimal_number)`
- `decimal_to_base24(decimal_number)`
- `decimal_to_base14(decimal_number)`
- `decimal_to_base12(decimal_number)`
- `decimal_to_base16(decimal_number)`

### Binary Coded Decimal (BCD) Function
- `bcd(n, code)`: Converts the number `n` to different bases depending on the `code` provided.

### Arithmetic Functions
These functions perform basic arithmetic operations:
- `add(a, b)`
- `sub(a, b)`
- `mul(a, b)`
- `div(a, b)`
- `pow(a, b)`
- `squareroot(a)`
- `cuberoot(a)`
- `fact(a)`: Calculates the factorial of `a`.
- `ncr(n, r)`: Calculates the combination of `n` items taken `r` at a time.
- `gcd(a, b)`: Calculates the greatest common divisor of `a` and `b`.

### Table and Square Table Functions
- `table(a, code, i=1)`: Prints the multiplication table for `a` in the specified base.
- `square(a, code, i=1)`: Prints the square of numbers up to `a` in the specified base.

### Print View Functions
- `print_view()`: Prints the list of available arithmetic operations.
- `print_main()`: Prints the list of available numerical bases.

### Main Control Functions
- `if_block(code)`: Controls the flow of arithmetic operations based on user input.
- `decimal(code=0000)`
- `binary(code=1010)`
- `quaternary(code=1212)`
- `senary(code=1023)`
- `octal(code=1234)`
- `duodecimal(code=1298)`
- `quadrodecimal(code=1462)`
- `hexadecimal(code=1636)`
- `quadravigesimal(code=2412)`
- `duotrigesimal(code=3268)`
- `tetrasexagesimal(code=6486)`

### Main Execution Function
- `if_main_block()`: Determines the base to work in based on user input.
- `main()`: Entry point of the script which starts the program.

### Usage
When the script is run, it first prints the list of bases available for use. The user can then select a base, 
and based on the selection, the corresponding function is called to handle further operations. The operations
range from simple arithmetic to more complex operations like finding factorials or combinations, all while 
converting the results to the specified 

Overall, this script is a powerful tool for performing various mathematical operations in different numerical bases.
