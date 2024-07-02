import numpy as np

def calcular_inversa(matriz):
    linhas, colunas = matriz.shape
    if linhas != colunas:
        raise ValueError("A matriz deve ser quadrada para calcular a inversa.")

    determinante = np.linalg.det(matriz)
    if determinante == 0:
        raise ValueError("A matriz não é inversível porque o determinante é zero.")

    matriz_inversa = np.linalg.inv(matriz)
    return matriz_inversa


def obter_matriz_usuario(tamanho):
    matriz = []
    print(f"Por favor, insira os elementos para uma matriz {tamanho}x{tamanho}:")
    for i in range(tamanho):
        while True:
            try:
                linha = input(f"Digite os elementos da linha {i + 1}, separados por espaço: ")
                valores = list(map(float, linha.split()))
                if len(valores) != tamanho:
                    raise ValueError("A quantidade de elementos inseridos não é igual ao tamanho da matriz.")
                matriz.append(valores)
                break
            except ValueError as ve:
                print(f"Entrada inválida: {ve}. Tente novamente.")
    return np.array(matriz)


def main():
    while True:
        try:
            tamanho = int(input("Digite o tamanho da matriz quadrada (n para uma matriz nxn): "))
            if tamanho < 1:
                raise ValueError("O tamanho da matriz deve ser maior que zero.")
            break
        except ValueError as ve:
            print(f"Entrada inválida: {ve}. Tente novamente.")

    matriz = obter_matriz_usuario(tamanho)

    try:
        inversa = calcular_inversa(matriz)
        print("Matriz Inversa:")
        print(inversa)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
