# /*
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

def esta_en_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

def main():
    numero = int(input("Introduce un número: "))
    es_par = numero % 2 == 0
    es_prim = es_primo(numero)
    esta_en_fib = esta_en_fibonacci(numero)

    if es_prim and esta_en_fib and es_par:
        print(f"{numero} es primo, fibonacci y es par")
    elif es_prim and esta_en_fib and not es_par:
        print(f"{numero} es primo, fibonacci y es impar")
    elif es_prim and not esta_en_fib and es_par:
        print(f"{numero} es primo, no es fibonacci y es par")
    elif es_prim and not esta_en_fib and not es_par:
        print(f"{numero} es primo, no es fibonacci y es impar")
    elif not es_prim and esta_en_fib and es_par:
        print(f"{numero} no es primo, fibonacci y es par")
    elif not es_prim and esta_en_fib and not es_par:
        print(f"{numero} no es primo, fibonacci y es impar")
    elif not es_prim and not esta_en_fib and es_par:
        print(f"{numero} no es primo, no es fibonacci y es par")
    else:
        print(f"{numero} no es primo, no es fibonacci y es impar")


main()