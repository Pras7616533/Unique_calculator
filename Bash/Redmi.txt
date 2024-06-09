which includes various mathematical operations and conversions between different number bases.
Let's break down the script into its components and explain each part:

1. **Functions for Mathematical Operations:**
   - `add`, `sub`, `mul`, `div`, `pow`, `squareroot`, `cuberoot`, `fact`, `ncr`, and `gcd` are 
functions defined to perform addition, subtraction, multiplication, division, exponentiation, 
square root, cube root, factorial, combination (n choose r), and greatest common divisor operations,
respectively. 

2. **Functions for Base Conversions:**
   - `decimal_to_base32`, `decimal_to_base64`, `decimal_to_base24`, `decimal_to_base14`, `decimal_to_base12`,
and `decimal_to_base16` are functions defined to convert a decimal number to base-32, base-64, base-24,
base-14, base-12, and base-16, respectively. 

3. **Main Menu and User Input Handling:**
   - The `print_view` and `print_main` functions display the main menu options for mathematical operations 
and base conversions, respectively.
   - The `if_main_block` function handles user input for selecting mathematical operations or base conversions.
It prompts the user to choose an option and calls the corresponding function based on the input.

4. **Conversion and Operation Execution:**
   - The `if_block` function takes a code representing the number base and executes the selected operation or 
conversion based on user input. It handles user input for performing arithmetic operations or base conversions 
and calls the appropriate function accordingly.

5. **Main Function:**
   - The `main` function serves as the entry point of the script. It displays the main menu, handles user input,
and executes the selected operation or conversion until the user chooses to exit.

Overall, this Bash script provides a command-line interface for performing mathematical operations and base
conversions, allowing users to interactively choose the desired operation or conversion.
