import matplotlib.pyplot as plt
import numpy as np
from A_Law_Compression import A_Law_Compress

def A_Law_Expansion(input,A): 
        
    output = []
    for v in input:
        if(np.abs(v) < 1/(1 + np.log(A))):
            g = np.sign(v)*np.abs(v)*(1 + np.log(A))/A
        else:
            g = np.exp(-1 + np.abs(v)*(1 + np.log(A)))/A    
        output.append(g)
    return output

if __name__ == "__main__":
    input = np.linspace(-1,1)

    compressed_1 = A_Law_Compress(input,1)
    compressed_2 = A_Law_Compress(input,2)
    compressed_100 = A_Law_Compress(input,100)

    expanded_1 = A_Law_Expansion(input,1)
    expanded_2 = A_Law_Expansion(input,2)
    expanded_100 = A_Law_Expansion(input,100)

    std_expanded_1 = np.std([expanded_1, input])
    std_expanded_2 = np.std([expanded_2, input])
    std_expanded_100 = np.std([expanded_2, input])

    diff_expanded_1 = np.abs(np.subtract(input, expanded_1))
    diff_expanded_2 = np.abs(np.subtract(input, expanded_2))
    diff_expanded_100 = np.abs(np.subtract(input, expanded_100))

    min_diff_expanded_1 = np.min(diff_expanded_1)
    min_diff_expanded_2 = np.min(diff_expanded_2)
    min_diff_expanded_100 = np.min(diff_expanded_100)

    max_diff_expanded_1 = np.max(diff_expanded_1)
    max_diff_expanded_2 = np.max(diff_expanded_2)
    max_diff_expanded_100 = np.max(diff_expanded_100)

    mean_diff_expanded_1 = np.mean(diff_expanded_1)
    mean_diff_expanded_2 = np.mean(diff_expanded_2)
    mean_diff_expanded_100 = np.mean(diff_expanded_100)

    print(f"A = 1, std: {std_expanded_1}, mean: {mean_diff_expanded_1}, min: {min_diff_expanded_1}, max: {max_diff_expanded_1}")
    print(f"A = 2, std: {std_expanded_2}, mean: {mean_diff_expanded_2}, min: {min_diff_expanded_2}, max: {max_diff_expanded_2}")
    print(f"A = 100, std: {std_expanded_100}, mean: {mean_diff_expanded_100}, min: {min_diff_expanded_100}, max: {max_diff_expanded_100}")

