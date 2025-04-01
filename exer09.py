def intersecao_arrays(array1, array2):
  intersecao = list(set(array1) & set(array2))
  return intersecao

array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]
resultado = intersecao_arrays(array1, array2)
print(resultado)  # Output: [4, 5]