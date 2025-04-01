def media_aritmetica(array):
  soma = sum(array)
  media = soma / len(array)
  return media

meu_array = [1, 2, 3, 4, 5]
resultado = media_aritmetica(meu_array)
print(resultado)  # Output: 3.0