#Autor: Luis Javier Montiel
#Desc: conversion de monedas 

def conversor(tipoMoneda,valorDolar):
  pesos = float(input("cuantos pesos " + tipoMoneda + " tienes: "))
  dolares = pesos / valorDolar
  dolares = str(round(dolares,2))
  print("tienes $" + dolares + "dolares")

menu = """
Bienvenido al conversor de monedas

1 - pesos colombianos
2 - pesos argentinos
3 - pesos mexicanos

"""
print(menu)
opcion = int(input("Elija una opcion: "))

if opcion == 1:
  conversor("colombianos",3875)
elif opcion == 2:
  conversor("argentinos",65)
elif opcion == 3:
  conversor("Mexicanos",24)
