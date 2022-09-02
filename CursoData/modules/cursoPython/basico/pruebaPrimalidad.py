def esPrimo(numero):
  contador = 0
  for i in range(1,numero+1):
    if i == 1 or i == numero:
      continue
    if(numero % i == 0):
      contador += 1
  return True if contador == 0 else False


def run():
  numero = int(input("Escribe un numero: "))
  if esPrimo(numero):
    print("es primo")
  else:
    print("no es primo")


if __name__ == '__main__':
  run()