# for contador in range(0,6,2):
#   print(contador)
def recorrer():
  nombre = input('ingrese un nombre: ')
  for letra in nombre:
    print(letra)


def continuar():
  for contador in range(1000):
    if contador % 2 != 0:
      continue
    print(contador)

def romper():
  for i in range(1000):
    print(i)
    if i == 564:
      break

def run():
  romper()


if __name__ == '__main__':
  run()