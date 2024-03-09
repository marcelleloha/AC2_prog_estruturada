""" 
Programação Estruturada
2024.1
AC2- Exercício 1
Autor: Marcelle Lohane Gonçalves Ganimo

Desenvolva duas funções em Python:

- eq_seg_grau(a, b, c), que recebe três valores reais e retorna as raízes de uma equação de segundo grau no 
formato ax² + bx + c = 0, supondo as raízes sempre reais;
- bissexto(ano), que recebe um valor inteiro e retorna um valor booleano, informando se o ano é bissexto ou não.

"""

def eq_segundo_grau(a, b, c):
    delta = b**2 - 4 * a * c 
    raiz1 = (-b + delta**0.5)/ 2 * a 
    raiz2 = (- b - delta ** 0.5)/ 2 * a 
    return (raiz1, raiz2)

print(eq_segundo_grau(1, -5, 6))

print(50 * "-")

def bissexto(ano):
    ano = ano % 400 == 0 and ano % 100 != 0 or ano % 4 == 0 
    return ano

print(bissexto(2000))

def calcula_salario(valor_hora, num_horas):
    irpf= 0.275
    salario_liq = valor_hora * num_horas - irpf * (valor_hora * num_horas)
    return (salario_liq)

print(calcula_salario(90, 100))
