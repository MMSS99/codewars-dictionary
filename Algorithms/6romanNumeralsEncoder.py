#https://www.codewars.com/kata/51b62bf6a9c58071c600001b

def solution(n):
    NUMEROS_ROMANOS = { 1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I" }
    
    romanizacion = ''
    while n > 0:
        for numero in NUMEROS_ROMANOS:
            while n >= numero:
                romanizacion += NUMEROS_ROMANOS.get(numero)
                n += -numero
    
    return romanizacion