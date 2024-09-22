import numpy as np

def calcular(numeros):
    if len(numeros) != 9: # Contagem da quantidade de números na lista
        raise ValueError("A lista deve conter nove números.")

    # Converte a lista em um array 3x3, para ser utilizado nas estatísticas
    matriz = np.array(numeros).reshape(3, 3)

    # Calcula as estatísticas
    media = [matriz.mean(axis=0).tolist(), matriz.mean(axis=1).tolist(), matriz.flatten().mean()] # tolist: converte a matriz para lista. axis define a coluna para as operações
    varianca = [matriz.var(axis=0).tolist(), matriz.var(axis=1).tolist(), matriz.flatten().var()]
    desviopadrao = [matriz.std(axis=0).tolist(), matriz.std(axis=1).tolist(), matriz.flatten().std()]
    val_max = [matriz.max(axis=0).tolist(), matriz.max(axis=1).tolist(), matriz.flatten().max()]
    val_min = [matriz.min(axis=0).tolist(), matriz.min(axis=1).tolist(), matriz.flatten().min()]
    soma = [matriz.sum(axis=0).tolist(), matriz.sum(axis=1).tolist(), matriz.flatten().sum()]

    # Retorna um dicionário com as estatísticas
    return {
        'media': [media[0], media[1], float(media[2])],  # retorna o valor das operações para cada coluna, e converte a media total para float
        'varianca': [varianca[0], varianca[1], float(varianca[2])],  # retorna o valor das operações para cada coluna, e converte a varianca total para float
        'desviopadrao': [desviopadrao[0], desviopadrao[1], float(desviopadrao[2])],  # retorna o valor das operações para cada coluna, e converte o desvio padrão total para float
        'val_max': [val_max[0], val_max[1], int(val_max[2])],  # retorna o valor das operações para cada coluna, e converte o valor máximo total para float
        'val_min': [val_min[0], val_min[1], int(val_min[2])],   # retorna o valor das operações para cada coluna, e converte o valor mínimo total para float
        'soma': [soma[0], soma[1], int(soma[2])]  # retorna o valor das operações para cada coluna, e converte a soma total para float
    }

# Testando a função
if __name__ == "__main__":
    resultado = calcular([0, 1, 2, 3, 4, 5, 6, 7, 8])
    print(resultado)
