import numpy as np

def calculate(list_of_numbers):
    if len(list_of_numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    # Converte a lista em um array 3x3
    matrix = np.array(list_of_numbers).reshape(3, 3)

    # Calcula as estatísticas
    mean = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.flatten().mean()]
    variance = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.flatten().var()]
    std_dev = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.flatten().std()]
    max_values = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.flatten().max()]
    min_values = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.flatten().min()]
    sum_values = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.flatten().sum()]

    # Retorna um dicionário com as estatísticas
    return {
        'mean': [mean[0], mean[1], float(mean[2])],  # converter para float
        'variance': [variance[0], variance[1], float(variance[2])],  # converter para float
        'standard deviation': [std_dev[0], std_dev[1], float(std_dev[2])],  # converter para float
        'max': [max_values[0], max_values[1], int(max_values[2])],  # converter para int
        'min': [min_values[0], min_values[1], int(min_values[2])],  # converter para int
        'sum': [sum_values[0], sum_values[1], int(sum_values[2])]  # converter para int
    }

# Testando a função
if __name__ == "__main__":
    result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    print(result)
