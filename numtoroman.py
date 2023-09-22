number = {
    1 : "I",
    4 : "IV",
    5 : "V",
    9 : "IX",
    10 : "X",
    40 : "XL",
    50 : "L",
    90 : "XC",
    100 : "C",
    400 : "CD",
    500 : "D",
}
n = 4
roman = ''

for value, numeral in sorted(number.items(), reverse = True):
    while n >= value:
        roman += numeral
        n -= value
print(roman)