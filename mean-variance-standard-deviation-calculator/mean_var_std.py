import numpy as np

def calculate(input_list):

    if len(input_list) != 9:
        raise ValueError('List must contain nine numbers.')
    
    else:
        input_vector = np.array(input_list)
        input_matrix = input_vector.reshape((3, 3))
        
        statistics = [
            ('mean', 'mean'),
            ('variance', 'var'),
            ('standard deviation', 'std'),
            ('max', 'max'),
            ('min', 'min'),
            ('sum', 'sum')
        ]

        out = {
            statistic[0]: [
                getattr(input_matrix, statistic[1])(axis=0).tolist(),
                getattr(input_matrix, statistic[1])(axis=1).tolist(),
                getattr(input_vector, statistic[1])().tolist()
            ] for statistic in statistics
        }

        return out
