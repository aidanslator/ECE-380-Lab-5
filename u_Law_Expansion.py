import matplotlib.pyplot as plt
import numpy as np
from u_Law_Compression import u_Law_Compress

def u_Law_Expansion(input,u): 
    if(u == 0):
        return input
        
    output = []
    for v in input:
        g = np.sign(v)*((1 + u)**(np.abs(v))-1)/u
        output.append(g)
    return output

if __name__ == "__main__":
    input = np.linspace(-1,1)

    compressed_1 = u_Law_Compress(input,0)
    compressed_5 = u_Law_Compress(input,5)
    compressed_100 = u_Law_Compress(input,100)

    expanded_1 = u_Law_Expansion(input,0)
    expanded_5 = u_Law_Expansion(input,5)
    expanded_100 = u_Law_Expansion(input,100)

    std_expanded_1 = np.std([expanded_1, input])
    std_expanded_5 = np.std([expanded_5, input])
    std_expanded_100 = np.std([expanded_5, input])

    diff_expanded_1 = np.abs(np.subtract(input, expanded_1))
    diff_expanded_5 = np.abs(np.subtract(input, expanded_5))
    diff_expanded_100 = np.abs(np.subtract(input, expanded_100))

    min_diff_expanded_1 = np.min(diff_expanded_1)
    min_diff_expanded_5 = np.min(diff_expanded_5)
    min_diff_expanded_100 = np.min(diff_expanded_100)

    max_diff_expanded_1 = np.max(diff_expanded_1)
    max_diff_expanded_5 = np.max(diff_expanded_5)
    max_diff_expanded_100 = np.max(diff_expanded_100)

    mean_diff_expanded_1 = np.mean(diff_expanded_1)
    mean_diff_expanded_5 = np.mean(diff_expanded_5)
    mean_diff_expanded_100 = np.mean(diff_expanded_100)

    print(f"A = 1, std: {std_expanded_1}, mean: {mean_diff_expanded_1}, min: {min_diff_expanded_1}, max: {max_diff_expanded_1}")
    print(f"A = 2, std: {std_expanded_5}, mean: {mean_diff_expanded_5}, min: {min_diff_expanded_5}, max: {max_diff_expanded_5}")
    print(f"A = 100, std: {std_expanded_100}, mean: {mean_diff_expanded_100}, min: {min_diff_expanded_100}, max: {max_diff_expanded_100}")

