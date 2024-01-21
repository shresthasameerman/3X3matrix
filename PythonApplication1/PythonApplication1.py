import numpy as np

def calculate(input_list):
    matrix = np.array(input_list).reshape(3, 3)

    mean = {
        'row': np.mean(matrix, axis=1),
        'column': np.mean(matrix, axis=0),
        'flattened': np.mean(matrix)
    }

    variance = {
        'row': np.var(matrix, axis=1),
        'column': np.var(matrix, axis=0),
        'flattened': np.var(matrix)
    }

    std_dev = {
        'row': np.std(matrix, axis=1),
        'column': np.std(matrix, axis=0),
        'flattened': np.std(matrix)
    }

    max_val = {
        'row': np.max(matrix, axis=1),
        'column': np.max(matrix, axis=0),
        'flattened': np.max(matrix)
    }

    min_val = {
        'row': np.min(matrix, axis=1),
        'column': np.min(matrix, axis=0),
        'flattened': np.min(matrix)
    }

    sum_val = {
        'row': np.sum(matrix, axis=1),
        'column': np.sum(matrix, axis=0),
        'flattened': np.sum(matrix)
    }

    return {
        'mean': mean,
        'variance': variance,
        'std_dev': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }