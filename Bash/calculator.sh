#!/bin/bash

# Function to convert decimal number to base 32
decimal_to_base32() {
  decimal_number=$1
  base32_chars="0123456789ABCDEFGHIJKLMNOPQRSTUV"
  base32_str=""
  if [[ $decimal_number -eq 0 ]]; then
    echo "0"
    return
  fi
  while [[ $decimal_number -gt 0 ]]; do
    remainder=$((decimal_number % 32))
    base32_str="${base32_chars:$remainder:1}$base32_str"
    decimal_number=$((decimal_number / 32))
  done
  echo "$base32_str"
}

# Function to convert decimal number to base 64
decimal_to_base64() {
  decimal_number=$1
  base64_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  base64_str=""
  if [[ $decimal_number -eq 0 ]]; then
    echo "0"
    return
  fi
  while [[ $decimal_number -gt 0 ]]; do
    remainder=$((decimal_number % 64))
    base64_str="${base64_chars:$remainder:1}$base64_str"
    decimal_number=$((decimal_number / 64))
  done
  echo "$base64_str"
}

# Function to convert decimal number to base 24
decimal_to_base24() {
  decimal_number=$1
  base24_chars="0123456789ABCDEFGHIJKLMN"
  base24_str=""
  if [[ $decimal_number -eq 0 ]]; then
    echo "0"
    return
  fi
  while [[ $decimal_number -gt 0 ]]; do
    remainder=$((decimal_number % 24))
    base24_str="${base24_chars:$remainder:1}$base24_str"
    decimal_number=$((decimal_number / 24))
  done
  echo "$base24_str"
}

# Function to convert decimal number to base 14
decimal_to_base14() {
  decimal_number=$1
  base14_chars="0123456789ABCD"
  base14_str=""
  if [[ $decimal_number -eq 0 ]]; then
    echo "0"
    return
  fi
  while [[ $decimal_number -gt 0 ]]; do
    remainder=$((decimal_number % 14))
    base14_str="${base14_chars:$remainder:1}$base14_str"
    decimal_number=$((decimal_number / 14))
  done
  echo "$base14_str"
}

# Function to convert decimal number to base 12
decimal_to_base12() {
  decimal_number=$1
  base12_chars="0123456789AB"
  base12_str=""
  if [[ $decimal_number -eq 0 ]]; then
    echo "0"
    return
  fi
  while [[ $decimal_number -gt 0 ]]; do
    remainder=$((decimal_number % 12))
    base12_str="${base12_chars:$remainder:1}$base12_str"
    decimal_number=$((decimal_number / 12))
  done
  echo "$base12_str"
}

# Function to convert decimal number to base 16
decimal_to_base16() {
  decimal_number=$1
  base16_chars="0123456789ABCDEF"
  base16_str=""
  if [[ $decimal_number -eq 0 ]]; then
    echo "0"
    return
  fi
  while [[ $decimal_number -gt 0 ]]; do
    remainder=$((decimal_number % 16))
    base16_str="${base16_chars:$remainder:1}$base16_str"
    decimal_number=$((decimal_number / 16))
  done
  echo "$base16_str"
}

# Function to handle BCD conversions
bcd() {
  n=$1
  code=$2
  case $code in
    0000) echo "$n";;
    1010) echo "obase=2; $n" | bc;;
    1212) echo "obase=4; $n" | bc | cut -c 2-;;
    1023) echo "obase=6; $n" | bc | cut -c 3-;;
    1234) echo "obase=8; $n" | bc | cut -c 2-;;
    1298) decimal_to_base12 $n;;
    1462) decimal_to_base14 $n;;
    1636) decimal_to_base16 $n;;
    2412) decimal_to_base24 $n;;
    3268) decimal_to_base32 $n;;
    6486) decimal_to_base64 $n;;
  esac
}

# Arithmetic functions

add() {
  echo "$(( $1 + $2 ))"
}

sub() {
  echo "$(( $1 - $2 ))"
}

mul() {
  echo "$(( $1 * $2 ))"
}

div() {
  echo "$(( $1 / $2 ))"
}

pow() {
  echo "$(( $1 ** $2 ))"
}

squareroot() {
  echo "sqrt($1)" | bc
}

cuberoot() {
  echo "c($1)" | bc -l
}

fact() {
  seq -s'*' 1 $1 | bc
}

ncr() {
  echo "scale=0; factorial($1)/(factorial($2)*factorial($1-$2))" | bc
}

gcd() {
  echo "$1,$2" | tr ',' '\n' | sort -n | factor | awk 'END{print $(NF-1)}'
}

table() {
  for ((i=1; i<=10; i++)); do
    echo "$1 × $i = $(( $1 * $i ))"
  done
}

square() {
  for ((i=1; i<=$1; i++)); do
    echo "$i × $i = $(( $i * $i ))"
  done
}

print_view() {
  echo "0 for exit"
  echo "1 for addition"
  echo "2 for subtraction"
  echo "3 for multiplication"
  echo "4 for division"
  echo "5 for power"
  echo "6 for square root"
  echo "7 for cube root"
  echo "8 for factorial"
  echo "9 for n choose r"
  echo "10 for greatest common divisor"
  echo "11 for table"
  echo "12 for square table"
}

print_main() {
  echo "0 for base-10 or decimal"
  echo "1 for base-2 or binary"
  echo "2 for base-4 or Quaternary"
  echo "3 for base-6 or Senary"
  echo "4 for base-8 or octal"
  echo "5 for base-12 or Duodecimal"
  echo "6 for base-14 or quadrodecimal"
  echo "7 for base-16 or Hexadecimal"
  echo "8 for base-24 or Quadravigesimal"
  echo "9 for base-32 or Duotrigesimal"
  echo "10 for base-64 or Tetrasexagesimal"
  echo "999 for exit"
}

if_main_block() {
  read -p "choose the option: " gusse_main
  if [[ $gusse_main == 999 ]]; then
    exit
  fi
  case $gusse_main in
    0) decimal;;
    1) binary;;
    2) quaternary;;
    3) senary;;
    4) octal;;
    5) duodecimal;;
    6) quadrodecimal;;
    7) hexadecimal;;
    8) quadravigesimal;;
    9) duotrigesimal;;
    10) tetrasexagesimal;;
  esac
}

if_block() {
  local code=$1
  read -p "choose the option: " gusse
  if [[ $gusse -eq 0 ]]; then
    exit
  elif [[ $gusse -ge 1 && $gusse -le 10 ]]; then
    local a b
    read -p "Enter the number: " a
    if [[ $gusse -ne 6 && $gusse -ne 7 && $gusse -ne 8 ]]; then
      read -p "Enter the number: " b
    fi
    case $gusse in
      1) echo "the addition of $(bcd $a $code) and $(bcd $b $code) is $(bcd $(add $a $b) $code)";;
      2) echo "the subtraction of $(bcd $a $code) and $(bcd $b $code) is $(bcd $(sub $a $b) $code)";;
      3) echo "the multiplication of $(bcd $a $code) and $(bcd $b $code) is $(bcd $(mul $a $b) $code)";;
      4) echo "the division of $(bcd $a $code) and $(bcd $b $code) is $(bcd $(div $a $b) $code)";;
      5) echo "the power of $(bcd $a $code) and $(bcd $b $code) is $(bcd $(pow $a $b) $code)";;
      6) echo "the square root of $(bcd $a $code) is $(bcd $(squareroot $a) $code)";;
      7) echo "the cube root of $(bcd $a $code) is $(bcd $(cuberoot $a) $code)";;
      8) echo "the factorial of $(bcd $a $code) is $(bcd $(fact $a) $code)";;
      9) echo "the $(bcd $a $code) choose $(bcd $b $code) is $(bcd $(ncr $a $b) $code)";;
      10) echo "the greatest common divisor of $(bcd $a $code) and $(bcd $b $code) is $(bcd $(gcd $a $b) $code)";;
    esac
  elif [[ $gusse -eq 11 || $gusse -eq 12 ]]; then
    read -p "Enter the number: " a
    case $gusse in
      11) table $a $code;;
      12) square $a $code;;
    esac
  else
    echo "Invalid option"
  fi
}

decimal() {
  echo "                 _-_-_-_-_-Decimal-_-_-_-_-_"
  print_view
  if_block 0000
}

binary() {
  echo "                 _-_-_-_-_-Binary-_-_-_-_-_"
  print_view
  if_block 1010
}

quaternary() {
  echo "                 _-_-_-_-_-Quaternary-_-_-_-_-_"
  print_view
  if_block 1212
}

senary() {
  echo "                 _-_-_-_-_-Senary-_-_-_-_-_"
  print_view
  if_block 1023
}

octal() {
  echo "                 _-_-_-_-_-Octal-_-_-_-_-_"
  print_view
  if_block 1234
}

duodecimal() {
  echo "                 _-_-_-_-_-Duodecimal-_-_-_-_-_"
  print_view
  if_block 1298
}

quadrodecimal() {
  echo "                 _-_-_-_-_-Quadrodecimal-_-_-_-_-_"
  print_view
  if_block 1462
}

hexadecimal() {
  echo "                 _-_-_-_-_-Hexadecimal-_-_-_-_-_"
  print_view
  if_block 1636
}

quadravigesimal() {
  echo "                 _-_-_-_-_-Quadravigesimal-_-_-_-_-_"
  print_view
  if_block 2412
}

duotrigesimal() {
  echo "                 _-_-_-_-_-Duotrigesimal-_-_-_-_-_"
  print_view
  if_block 3268
}

tetrasexagesimal() {
  echo "                 _-_-_-_-_-Tetrasexagesimal-_-_-_-_-_"
  print_view
  if_block 6486
}

main() {
  print_main
  echo -e "\n\n\n\n"
  if_main_block
}

# Invoke main function
main

