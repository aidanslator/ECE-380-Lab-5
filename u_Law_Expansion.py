import matplotlib.pyplot as plt
import numpy as np
from u_Law_Compression import u_Law_Compress

def u_Law_Expansion(input,u) -> np.ndarray: 
    if(u <= 0):
        return input
        
    output = []
    for v in input:
        g = np.sign(v)*((1 + u)**(np.abs(v))-1)/u
        output.append(g)
    return output

if __name__ == "__main__":
    input = np.linspace(-1,1)

    compressed_0 = u_Law_Compress(input,0)
    compressed_5 = u_Law_Compress(input,5)
    compressed_100 = u_Law_Compress(input,100)

    expanded_0 = u_Law_Expansion(compressed_0,0)
    expanded_5 = u_Law_Expansion(compressed_5,5)
    expanded_100 = u_Law_Expansion(compressed_100,100)

    std_expanded_0 = np.std([expanded_0, input])
    std_expanded_5 = np.std([expanded_5, input])
    std_expanded_100 = np.std([expanded_5, input])

    diff_expanded_0 = np.abs(np.subtract(input, expanded_0))
    diff_expanded_5 = np.abs(np.subtract(input, expanded_5))
    diff_expanded_100 = np.abs(np.subtract(input, expanded_100))

    min_diff_expanded_0 = np.min(diff_expanded_0)
    min_diff_expanded_5 = np.min(diff_expanded_5)
    min_diff_expanded_100 = np.min(diff_expanded_100)

    max_diff_expanded_0 = np.max(diff_expanded_0)
    max_diff_expanded_5 = np.max(diff_expanded_5)
    max_diff_expanded_100 = np.max(diff_expanded_100)

    mean_diff_expanded_0 = np.mean(diff_expanded_0)
    mean_diff_expanded_5 = np.mean(diff_expanded_5)
    mean_diff_expanded_100 = np.mean(diff_expanded_100)

    print(f"u = 0, std: {std_expanded_0}, mean: {mean_diff_expanded_0}, min: {min_diff_expanded_0}, max: {max_diff_expanded_0}")
    print(f"u = 5, std: {std_expanded_5}, mean: {mean_diff_expanded_5}, min: {min_diff_expanded_5}, max: {max_diff_expanded_5}")
    print(f"u = 100, std: {std_expanded_100}, mean: {mean_diff_expanded_100}, min: {min_diff_expanded_100}, max: {max_diff_expanded_100}")

