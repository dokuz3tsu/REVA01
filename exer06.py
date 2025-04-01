def remover_duplicados(array):
  array_sem_duplicados = list(set(array))
  return array_sem_duplicados

meu_array = [1, 2, 2, 3, 4, 4, 5]
resultado = remover_duplicados(meu_array)
print(resultado)  # Output: [1, 2, 3, 4, 5]