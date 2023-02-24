from funciones import menor_de_arreglo
def test_arreglo():
    arreglo = [0, -1, 4, 6000, 1, 2, 1400, -10, 90, 13, 7, 12, 500, 16]
    assert menor_de_arreglo(arreglo) == -10
    arreglo2 = [0,1,2,3]
    assert menor_de_arreglo(arreglo2) == -10