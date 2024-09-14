import numpy as np
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # Definindo a lista de números
    list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # Exemplo de entrada
    result = calculate(list_of_numbers)
    return jsonify(result)  # Retorna o resultado como JSON

def calculate(list_of_numbers):
    if len(list_of_numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    # Converte a lista em um array 3x3
    matrix = np.array(list_of_numbers).reshape(3, 3)

    # Calcula as estatísticas
    mean = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), float(matrix.flatten().mean())]
    variance = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), float(matrix.flatten().var())]
    std_dev = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), float(matrix.flatten().std())]
    max_values = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), int(matrix.flatten().max())]
    min_values = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), int(matrix.flatten().min())]
    sum_values = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), int(matrix.flatten().sum())]

    # Retorna um dicionário com as estatísticas
    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_values,
        'min': min_values,
        'sum': sum_values
    }

# Testando a função
if __name__ == "__main__":
    app.run(debug=True)
