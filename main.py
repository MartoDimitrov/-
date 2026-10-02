10number = input("Въведи число: ").upper()
base_from = int(input("От коя бройна система е: "))
base_to = int(input("В коя бройна система го искаш: "))

decimal_num = int(number, base_from)

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

while decimal_num > 0:
    remainder = decimal_num % base_to
    result = digits[remainder] + result
    decimal_num = decimal_num // base_to

if result == "":
    result = "0"

print(f"Резултат: {result}")
