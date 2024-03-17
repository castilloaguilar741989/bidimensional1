def search_value(matrix, value):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == value:
                return True, (i, j)  # Valor encontrado, devuelve True y la posición (i, j)
    return False, None  # Valor no encontrado, devuelve False y None como posición

# Define una matriz bidimensional de 3x3 con valores numéricos
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor que queremos buscar en la matriz
target_value = 5

# Llama a la función search_value para buscar el valor target_value en la matriz
found, position = search_value(matrix, target_value)

# Muestra un mensaje dependiendo de si se encontró o no el valor, junto con su posición si se encontró
if found:
    print(f"El valor {target_value} se encontró en la posición {position}")
else:
    print(f"El valor {target_value} no se encontró en la matriz")
