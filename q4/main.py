# Questão 4 - Verificador de Números Pares e Ímpares
# Crie uma função que receba um número inteiro e retorne se ele é par ou ímpar.

def verificador_pares_impares(numero: int) -> str:
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")    

numero = int(input("Digite um número: "))

verificador_pares_impares(numero)
