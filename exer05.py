def contar_pares_impares(array):
  pares = 0
  impares = 0
  for numero in array:
    if numero % 2 == 0:
      pares += 1
    else:
      impares += 1
  print(f"Pares: {pares}")
  print(f"Ímpares: {impares}")

meu_array = [1, 2, 3, 4, 5]
contar_pares_impares(meu_array)