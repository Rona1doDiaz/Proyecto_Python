def validar(dato):
    if len(dato.replace(" ","")) != 1 or x.isdigit():
        for tipo in tipos:
          try:
              return tipo(dato)
          except ValueError:
              pass
        return True
    else:
        return False

i = input("Ingrese: ")
x = validar(i, (int, float, complex))
if x is True:
    if i==i[::-1]:
        print("Palindromo")
    else:
        print("No palindromo")
else:
  print("ingrese una palabra") 