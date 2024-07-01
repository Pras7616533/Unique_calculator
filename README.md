#Unique Calculator

##Overview
The Unique Calculator is a versatile and comprehensive calculator capable of performing a wide range of arithmetic operations and numerical base conversions. It supports conversions between various numerical bases and offers a rich set of arithmetic functions, making it a valuable tool for both basic and advanced mathematical computations.

#Features

#Base Conversion Functions:
Convert decimal numbers to several bases, including binary, octal, hexadecimal, and less common bases such as quaternary, senary, duodecimal, etc.

#Binary Coded Decimal (BCD) Function:
Convert numbers to different bases based on a provided code.

#Arithmetic Functions:
Perform basic operations like addition, subtraction, multiplication, and division.
Calculate exponentiation, square roots, cube roots, factorials, combinations (nCr), and greatest common divisors.

#Table and Square Table Functions:
Print multiplication tables and squares of numbers in the specified base.

#User Interaction:
Display available arithmetic operations and numerical bases to guide the user.
Usage

#Base Conversion Functions
Convert a decimal number to a specified base:

decimal_to_base32(decimal_number)
decimal_to_base64(decimal_number)
decimal_to_base24(decimal_number)
decimal_to_base14(decimal_number)
decimal_to_base12(decimal_number)
decimal_to_base16(decimal_number)

#Binary Coded Decimal (BCD) Function
Convert the number n to different bases depending on the provided code:

bcd(n, code)


#Arithmetic Functions
Perform basic and advanced arithmetic operations:

add(a, b)
sub(a, b)
mul(a, b)
div(a, b)
pow(a, b)
squareroot(a)
cuberoot(a)
fact(a)
ncr(n, r)
gcd(a, b)

#Table and Square Table Functions
Print multiplication tables and squares of numbers:

table(a, code, i=1)
square(a, code, i=1)


##Main Control Functions
Control the flow of operations based on the selected base:

if_block(code)
decimal(code=0000)
binary(code=1010)
quaternary(code=1212)
senary(code=1023)
octal(code=1234)
duodecimal(code=1298)
quadrodecimal(code=1462)
hexadecimal(code=1636)
quadravigesimal(code=2412)
duotrigesimal(code=3268)
tetrasexagesimal(code=6486)


#Main Execution Function
Determine the base to work in and start the program:

if_main_block()
main()


#How to Run
Clone the repository:

|git clone https://github.com/Pras7616533/Unique_calculator.git

#Navigate to the Python folder:

|cd Unique_calculator/Python

#Run the main script:


|python main.py

Follow the on-screen instructions to select a base and perform operations.

#Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

#License
This project is licensed under the MIT License.

#Contact
For any questions or suggestions, please contact Prashant Deshmukh at [prashdesh555@gmail.com].

