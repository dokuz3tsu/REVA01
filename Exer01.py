def soma_array(array):
  soma = 0
  for numero in array:
    soma += numero
  return soma

meu_array = [1, 2, 3, 4, 5]
resultado = soma_array(meu_array)
print(resultado)  # Output: 15