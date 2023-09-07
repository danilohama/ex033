"""Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR"""
from time import sleep

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor:'))
# primeiro bloco Verificando quem é o menor!
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Segundo bloco verificando quem é o maior!
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('\033[0:33mAGUARDE\033[0:0m...')
sleep(3)
print('O \033[0:31mMENOR\033[0:0m valor digitado foi {}'.format(menor))
print('O \033[0:31mMAIOR\033[0:0m valor digitado foi {}'.format(maior))
