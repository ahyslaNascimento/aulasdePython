tuple = (1, 2, 3, 4, 5, 6)
metade = len(tuple) // 2 #calculando o indice da metada da tupla
tuple1 = tuple[:metade] # obtendo as metades da tupla usando slicing
tuple2 = tuple[metade:] 
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
