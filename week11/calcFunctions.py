from math import factorial as fact


def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r


def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r


def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

romans = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
          100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}


roman = [[(1000, 'M'), (900, 'CM'), (800, 'DCCC'), (700, 'DCC'), (600, 'DC'), (500, 'D'), (400, 'CD'), (300, 'CCC'),
          (200, 'CC'), (100, 'C')],
         [(90, 'XC'), (80, 'LXXX'), (70, 'LXX'), (60, 'LX'), (50, 'L'), (40, 'XL'), (30, 'XXX'), (20, 'XX'), (10, 'X')],
         [(9, 'IX'), (8, 'VIII'), (7, 'VII'), (6, 'VI'), (5, 'V'), (4, 'IV'), (3, 'III'), (2, 'II'), (1, 'I')]]


def decToRoman(numStr):
    n = int(numStr)
    result = ''
    for value in sorted(romans.keys(), reverse=True):
        while n >= value:
            result += romans[value]
            n -= value
    return str(result)


def romanToDec(numStr):
    result = 0
    for i in range(0, len(roman)):
        for value, letter in roman[i]:
            idx = numStr.find(letter)
            if idx == 0:
                result += value
                numStr = numStr[len(letter):len(numStr)]
    return str(result)
