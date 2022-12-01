##################################################################################################################################################
__author__ = "Cristian Fernando Laynez Bachez"
__copyright__ = "Copyright 2021 - Universidad del Valle de Guatemala"
__credits__ = "Matemática Discreta"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = ["cristianlaynezbachez@gmail.com", "lay201281@uvg.edu.gt"]
__status__ = "Student of Computer Science"

# Proyecto Corto #4 - Relaciones ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# -> Propiedades de una relación: Se debe determinar si la relación es reflexiva, simétrica, antisimétrica y/o transitiva.
# -> Composición de relaciones: Encontrar si las relaciones R ° S y S ° R
#################################################################################################################################################
# IMPORTANTE: ES NECESARIO TENER INSTALADO NUMPY PARA EJECUTAR DE MANERA CORRECTA ESTE PROGRAMA
#################################################################################################################################################

import numpy as np

# -----------------------------------------------------------------------------------------------------------------------------------------------
# --> Función para ejecutar el programa entero --------------------------------------------------------------------------------------------------


def main() -> None:
    print("-------------------------------------------------------------------------------------")
    print("----------------------------------PROYECTO CORTO #4----------------------------------")

    print("\n--> Conjuntos (Obtener contraseña): -------------------------------------------------\n")
    R = analyze_set(1, 100, ">")
    S = analyze_set(1, 100, "!=")
    print(f"R: {R}, S: {S}, Suma: {(R + S)}")

    print("\n--> Propiedades de una Relación: ----------------------------------------------------\n")
    # print(relation_properties([[0, 1, 2], [0, 1], [2], [0, 2]]))
    print(relation_properties([[0, 1, 2, 3], [0, 1], [0, 1], [2], [3]]))
    print(relation_properties(
        [[0, 1, 2, 3], [0, 1, 3], [0, 2], [1, 2, 3], [0, 2, 3]]))
    # Debe de ser transitiva también
    print(relation_properties([[0, 1, 2, 3], [0, 1, 2], [1], [2, 3], [0, 3]]))

    print("\n--> Composición de Relaciones: ------------------------------------------------------\n")
    # print(composition_of_relationsships(
    #   [[1], [1, 2], [0, 1, 2]], [[1], [0, 1, 2], [0]]))
    print(composition_of_relationsships(
        [[0, 1, 2], [1], [0, 1, 2], [0]], [[0, 1, 2], [1], [1, 2], [0, 1, 2]]))
    print(composition_of_relationsships(
        [[0, 1, 2], [1], [1, 2], [0, 1, 2]], [[0, 1, 2], [1], [0, 1, 2], [0]]))

    print("\n-----------------------------------FIN PROGRAMA :)-----------------------------------")
    print("-------------------------------------------------------------------------------------")

# -----------------------------------------------------------------------------------------------------------------------------------------------
###############Todos los métodos/funciones que son AUXILIARES para obtener la RELACIONES DE PROPIEDADES y COMPOSICIÓN DE RELACIONES##############
# -----------------------------------------------------------------------------------------------------------------------------------------------
# --> Obtener matriz ----------------------------------------------------------------------------------------------------------------------------
# @param digrafo: Será representado como lista de adyacencia
# @return [list]: Matriz generada junto con valores solicitados


def _get_matrix(digraph: list) -> list:
    values = {}
    # Definir los valores
    for i in digraph[0]:
        values[i] = []

    # Agregar los valores que estan dentro de los valores
    for i in range(len(values)):
        j = i + 1
        for elem in digraph[j]:
            values[i].append(elem)

    # Imprimir la lista
    matrix = []
    for i in values:
        m = []
        for j in range(len(values)):
            m.append("1") if j in values[i] else m.append("0")
        matrix.append(m)

    return values, matrix

# --> Obtener producto --------------------------------------------------------------------------------------------------------------------------
# @param matrix1 & matrix2: Matrices que serán analizadas
# @return [list]: Matriz generada del producto


def _get_product(matrix1: list, matrix2: list) -> list:
    matrix_product = []  # matrix1 ° matrix2 = [M:matriz2] ° [M:matrix1]
    for i in range(len(matrix1)):
        columns_to_sum = []
        for j in range(len(matrix1[i])):
            if matrix1[j][i] == "1":
                columns_to_sum.append(j)

        if len(columns_to_sum) > 1:  # Sumar los números requerridos
            the_sum = {}
            for l in columns_to_sum:
                for k in range(len(matrix2[i])):
                    numero = int(matrix2[k][l])
                    the_sum[k] = numero if not k in the_sum else the_sum[k] + numero
                    if the_sum[k] > 1:
                        the_sum[k] = 1

            matrix_product.append([str(the_sum[i]) for i in the_sum])

        elif len(columns_to_sum) == 1:  # Solamente copiar
            matrix_product.append([str(matrix2[k][columns_to_sum[0]])
                                  for k in range(len(matrix2[i]))])

    return np.array(matrix_product).transpose()

# -----------------------------------------------------------------------------------------------------------------------------------------------
###############################Todos los métodos/funciones que servirán para obtener las PROPIEDADES DE UNA RELACIÓN#############################
# -----------------------------------------------------------------------------------------------------------------------------------------------
# --> Propiedades de una relación ---------------------------------------------------------------------------------------------------------------
# @param digrafo: Será representado como lista de adyacencia
# @return [str]: Lista y que tipo de relación es


def relation_properties(digraph: list) -> str:
    digraph_result = _get_matrix(digraph)
    values = digraph_result[0]
    matrix = digraph_result[1]

    # Analizar si la relación es reflexiva, simétrica, antisimétrica y/o transitiva
    yes = []
    no = []
    # Reflexiva:
    yes.append("REFLEXIVA") if _check_if_is_reflexive(
        values) else no.append("REFLEXIVA")
    # Simétrica
    yes.append("SIMETRICA") if _check_if_is_symmetric(
        matrix) else no.append("SIMETRICA")
    # # Antisimétrica
    yes.append("ANTISIMETRICA") if _check_if_is_antisymmetric(
        matrix) else no.append("ANTISIMETRICA")
    # # Transitiva
    yes.append("TRANSITIVA") if _check_if_is_transitive(
        matrix) else no.append("TRANSITIVA")

    bits = []
    # Reflexiva:
    bits.append(1) if _check_if_is_reflexive(values) else bits.append(0)
    # Simétrica
    bits.append(1) if _check_if_is_symmetric(matrix) else bits.append(0)
    # # Antisimétrica
    bits.append(1) if _check_if_is_antisymmetric(matrix) else bits.append(0)
    # # Transitiva
    bits.append(1) if _check_if_is_transitive(matrix) else bits.append(0)

    return f"==> {digraph}\nLa Matriz P = {matrix} indica que la relación es:\nSI: {yes}\nNO: {no}\nLista Binaria: {bits}\n"

# --> Revisar si es Reflexiva -------------------------------------------------------------------------------------------------------------------
# @param valores: Los valores que se encontraron relacionados
# @return [bool]: Se retonará si la relación es reflexiva o no


def _check_if_is_reflexive(values: list) -> bool:
    for i in values:
        if not i in values[i]:
            return False
    return True

# --> Revisar si es Simetrica -------------------------------------------------------------------------------------------------------------------
# @param matrix: Matriz que será analizada
# @return [bool]: Se retonará si la relación es simetrica o no


def _check_if_is_symmetric(matrix: list) -> bool:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j:
                if matrix[i][j] != matrix[j][i]:
                    return False
    return True

# --> Revisar si es Antisimetrica ---------------------------------------------------------------------------------------------------------------
# @param matrix: Matriz que será analizada
# @return [bool]: Se retonará si la relación es antisimetrica o no


def _check_if_is_antisymmetric(matrix: list) -> bool:
    matrix1 = np.array(matrix)
    matrix2 = np.array(matrix).transpose()

    count = 0
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            if i != j:
                if matrix1[i][j] == matrix2[i][j]:
                    count += 1

    return True if count <= len(matrix) else False

# --> Revisar si es transitiva ------------------------------------------------------------------------------------------------------------------
# @param matrix: Matriz que será analizada
# @return [bool]: Se retonará si la relación es transitiva o no


def _check_if_is_transitive(matrix: list) -> bool:
    m_power_2 = _get_product(matrix, matrix)
    matrix = np.array(matrix)

    check = matrix == m_power_2
    return check.all()

# -----------------------------------------------------------------------------------------------------------------------------------------------
###############################Todos los métodos/funciones que servirán para obtener la COMPOSICIÓN DE UNA RELACION##############################
# -----------------------------------------------------------------------------------------------------------------------------------------------
# --> Composición de relaciones -----------------------------------------------------------------------------------------------------------------
# @param digrafo R: Representa el primer digrafo (Lista de adyacencia)
# @param digrafo S: Representa el segundo digrafo (Lista de adyacencia)
# @return [str]: Relaciones R ° S y S ° R, representadas como listas de aristas


def composition_of_relationsships(digraph_r: list, digraph_s: list) -> list:
    res_digraph1 = _get_matrix(digraph_r)
    res_digraph2 = _get_matrix(digraph_s)

    matrix1 = res_digraph1[1]
    matrix2 = res_digraph2[1]

    # Se procederá a multiplicar las matrices
    # R ° S
    product_r_to_s = _get_product(matrix1, matrix2)
    edge_list_r_to_s = _make_edge_list(product_r_to_s)
    # S ° R
    product_s_to_r = _get_product(matrix2, matrix1)
    edge_list_s_to_r = _make_edge_list(product_s_to_r)

    results = "\n"
    results += f"R = {digraph_r},\nS = {digraph_s}\n"
    results += f"R ° S\n{product_r_to_s}\n-> Lista de aristas: {edge_list_r_to_s}\n\nS ° R\n{product_s_to_r}"
    return results + f"\n-> Lista de aristas: {edge_list_s_to_r}\n"

# --> Crear lista de aristas --------------------------------------------------------------------------------------------------------------------
# --> Crear lista de aristas (Aux) --------------------------------------------------------------------------------------------------------------
# @param matrix: Matriz que será procesada
# @return [list]: Se retonará la lista de aristas en base de la matriz enviada


def _make_edge_list(matrix: list) -> list:
    edge_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "1":
                edge_list.append([i, j])
    return edge_list

# -----------------------------------------------------------------------------------------------------------------------------------------------
##############################Todo(s) los métodos/funciones que servirán para obtener la CONTRASEÑA DE ESTE PROYECTO#############################
# -----------------------------------------------------------------------------------------------------------------------------------------------
# --> Analizar conjunto -------------------------------------------------------------------------------------------------------------------------
# @param start set: Punto de inicio del conjunto
# @param finish set: Punto final del conjunto
# @param tipo de analisis: El tipo de condición que se desea analizar
# @return [int]: Se retonará la suma de todas las coincidencias encontradas


def analyze_set(start_set: int, finish_set: int, type_of_analyze: str) -> int:
    coincidences = 0
    for i in range(start_set, finish_set+1):
        for j in range(start_set, finish_set+1):
            if _check_condition(i, j, type_of_analyze):
                coincidences += 1
    return coincidences

# --> Revisar condición del conjunto (Aux) ------------------------------------------------------------------------------------------------------
# @param i: numero i del primer ciclo iterado
# @param j: numero j del segundo ciclo iterado
# @param tipo de analisis: El tipo de condición que se desea analizar
# @return [bool]: Se retonará si la condición se cumple


def _check_condition(i: int, j: int, type_of_analyze: str) -> bool:
    if type_of_analyze == ">":
        if i > j:
            return True
    if type_of_analyze == "!=":
        if i != j:
            return True
    return False


# -----------------------------------------------------------------------------------------------------------------------------------------------
# --> Principal----------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
