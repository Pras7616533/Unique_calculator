let selectedBase = 0;

function selectBase(base) {
    selectedBase = base;
    document.getElementById('main-options').classList.add('hidden');
    document.getElementById('calc-options').classList.remove('hidden');
}

function goBack() {
    document.getElementById('calc-options').classList.add('hidden');
    document.getElementById('main-options').classList.remove('hidden');
    document.getElementById('result').innerHTML = '';
}

function performOperation(operation) {
    let a, b;
    switch(operation) {
        case 1: // Addition
            a = parseInt(prompt("Enter the first number:"));
            b = parseInt(prompt("Enter the second number:"));
            showResult(`The addition of ${convertBase(a)} and ${convertBase(b)} is ${convertBase(a + b)}`);
            break;
        case 2: // Subtraction
            a = parseInt(prompt("Enter the first number:"));
            b = parseInt(prompt("Enter the second number:"));
            showResult(`The subtraction of ${convertBase(a)} and ${convertBase(b)} is ${convertBase(a - b)}`);
            break;
        case 3: // Multiplication
            a = parseInt(prompt("Enter the first number:"));
            b = parseInt(prompt("Enter the second number:"));
            showResult(`The multiplication of ${convertBase(a)} and ${convertBase(b)} is ${convertBase(a * b)}`);
            break;
        case 4: // Division
            a = parseInt(prompt("Enter the first number:"));
            b = parseInt(prompt("Enter the second number:"));
            if (b === 0) {
                alert("Division by zero is not allowed");
                return;
            }
            showResult(`The division of ${convertBase(a)} and ${convertBase(b)} is ${convertBase(Math.floor(a / b))}`);
            break;
        case 5: // Power
            a = parseInt(prompt("Enter the base number:"));
            b = parseInt(prompt("Enter the exponent:"));
            showResult(`The power of ${convertBase(a)} to ${convertBase(b)} is ${convertBase(Math.pow(a, b))}`);
            break;
        case 6: // Square Root
            a = parseInt(prompt("Enter the number:"));
            showResult(`The square root of ${convertBase(a)} is ${convertBase(Math.floor(Math.sqrt(a)))}`);
            break;
        case 7: // Cube Root
            a = parseInt(prompt("Enter the number:"));
            showResult(`The cube root of ${convertBase(a)} is ${convertBase(Math.floor(Math.cbrt(a)))}`);
            break;
        case 8: // Factorial
            a = parseInt(prompt("Enter the number:"));
            showResult(`The factorial of ${convertBase(a)} is ${convertBase(factorial(a))}`);
            break;
        case 9: // N Choose R
            a = parseInt(prompt("Enter n:"));
            b = parseInt(prompt("Enter r:"));
            showResult(`${convertBase(a)} choose ${convertBase(b)} is ${convertBase(ncr(a, b))}`);
            break;
        case 10: // GCD
            a = parseInt(prompt("Enter the first number:"));
            b = parseInt(prompt("Enter the second number:"));
            showResult(`The greatest common divisor of ${convertBase(a)} and ${convertBase(b)} is ${convertBase(gcd(a, b))}`);
            break;
        case 11: // Table
            a = parseInt(prompt("Enter the number:"));
            showResult(generateTable(a));
            break;
        case 12: // Square Table
            a = parseInt(prompt("Enter the number:"));
            showResult(generateSquareTable(a));
            break;
        default:
            alert("Invalid operation");
            break;
    }
}

function showResult(message) {
    document.getElementById('result').innerHTML = message;
}

function convertBase(number) {
    if (selectedBase === 0) return number.toString();
    if (selectedBase === 1) return number.toString(2);
    if (selectedBase === 2) return number.toString(4);
    if (selectedBase === 3) return number.toString(6);
    if (selectedBase === 4) return number.toString(8);
    if (selectedBase === 5) return decimalToBase(number, 12);
    if (selectedBase === 6) return decimalToBase(number, 14);
    if (selectedBase === 7) return number.toString(16);
    if (selectedBase === 8) return decimalToBase(number, 24);
    if (selectedBase === 9) return decimalToBase(number, 32);
    if (selectedBase === 10) return decimalToBase(number, 64);
}

function decimalToBase(number, base) {
    const chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/";
    let result = "";
    while (number > 0) {
        result = chars[number % base] + result;
        number = Math.floor(number / base);
    }
    return result || "0";
}

function factorial(n) {
    if (n === 0 || n === 1) return 1;
    return n * factorial(n - 1);
}

function ncr(n, r) {
    return factorial(n) / (factorial(r) * factorial(n - r));
}

function gcd(a, b) {
    while (b !== 0) {
        const temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

function generateTable(n) {
    let result = "";
    for (let i = 1; i <= 10; i++) {
        result += `${convertBase(n)} × ${convertBase(i)} = ${convertBase(n * i)}<br>`;
    }
    return result;
}

function generateSquareTable(n) {
    let result = "";
    for (let i = 1; i <= n; i++) {
        result += `${convertBase(i)} × ${convertBase(i)} = ${convertBase(i * i)}<br>`;
    }
    return result;
}
