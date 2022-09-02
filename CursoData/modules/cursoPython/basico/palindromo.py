def palindromo(palabra):
  palabra = palabra.replace(' ','')
  palabra = palabra.lower()
  palabraInversa = palabra[::-1]
  return True if palabra == palabraInversa else False

def run():
  palabra = input("Ingrese una palabra: ")
  esPalindromo = palindromo(palabra)
  if esPalindromo:
    print("es palindromo")
  else:
    print("no es palindromo")


if __name__ == '__main__':
  run()