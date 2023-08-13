num_check = int(input("Enter number: "))
hex_digits = "0123456789abcdef"
res_16 = ""
num = num_check
while num > 0:
    res_16 = hex_digits[num % 16] + res_16
    num //= 16
print(res_16, hex(num_check).replace("0x", ''))