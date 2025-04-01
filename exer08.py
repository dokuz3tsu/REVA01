def deslocar_direita(array, deslocamento):
  deslocamento = deslocamento % len(array)  # Garante que o deslocamento esteja dentro do tamanho do array
  array_deslocado = array[-deslocamento:] + array[:-deslocamento]
  return array_deslocado

meu_array = [1, 2, 3, 4, 5]
resultado = deslocar_direita(meu_array, 2)
print(resultado)  # Output: [4, 5, 1, 2, 3]