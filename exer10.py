def maior_subarray_soma(array):
  max_atual = max_global = array[0]
  for i in range(1, len(array)):
    max_atual = max(array[i], max_atual + array[i])
    max_global = max(max_global, max_atual)
  return max_global

meu_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
resultado = maior_subarray_soma(meu_array)
print(resultado)  # Output: 6