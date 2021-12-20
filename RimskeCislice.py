def int_to_rim(x):
    cisla = [1, 4, 5, 9, 10, 40, 50, 90,
             100, 400, 500, 900, 1000, 4000, 5000, 9000,
             10000, 40000, 50000, 90000,
             100000, 400000, 500000, 900000,
             1000000, 4000000, 5000000, 9000000,
             10000000, 40000000, 50000000, 90000000,
             100000000, 400000000, 500000000, 900000000, 1000000000]
    rimskecislice = ["I", "IV", "V", "IX", "X", "XL", "L", "XC",  # 1-90
                     "C", "CD", "D", "CM", "M", "I/V/", "V/", "I/X/",  # 100-9.000
                     "X/", "X/L/", "L/", "X/C/",  # 10.000-90.000
                     "C/", "C/D/", "D/", "C/M/",  # 100.000-900.000
                     "M/", "M/V//", "V//", "M/X//",  # 1.000.000-9.000.000
                     "X//", "X//L//", "L//", "X//C//",  # 10.000.000-90.000.000
                     "C//", "C//D//", "D//", "C//M//", "M//"]  # 100.000.000-1.000.000.000
    # lomitko znamena cara nad rimskou cislici

    i = 36  # pocet pozic
    rimske_cisla = ''
    while x != 0:
        if cisla[i] <= x:
            rimske_cisla += rimskecislice[i]
            x = x - cisla[i]
        else:
            i -= 1
    return rimske_cisla


x = 2
if x == 0:
    raise Exception("číslo se nesmí rovnat nule")
elif x < 0:
    raise Exception("číslo nesmí být nižší než nula!")
else:
    print("Převod do římského čísla: " + int_to_rim(x))
