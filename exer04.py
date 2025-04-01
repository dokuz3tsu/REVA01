def inverter_array(array):
  array_invertido = array[::-1]
  return array_invertido

meu_array = [1, 2, 3, 4, 5]
resultado = inverter_array(meu_array)
print(resultado)  # Output: [5, 4, 3, 2, 1]