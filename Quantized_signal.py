import matplotlib.pyplot as plt
import numpy as np
from u_Law_Compression import u_Law_Compress
from A_Law_Compression import A_Law_Compress
from u_Law_Expansion import u_Law_Expansion
from A_Law_Expansion import A_Law_Expansion

if __name__ == "__main__":
    input = np.linspace(-1,1)

    u_compressed_100 = np.array(u_Law_Compress(input,100))
    a_compressed_100 = np.array(A_Law_Compress(input,100))

    u_quantized_compressed_100_3bits = np.round(2**3*u_compressed_100)/(2**3)
    u_quantized_compressed_100_6bits = np.round(2**6*u_compressed_100)/(2**6)
    u_quantized_compressed_100_8bits = np.round(2**8*u_compressed_100)/(2**8)
    
    a_quantized_compressed_100_3bits = np.round(2**3*a_compressed_100)/(2**3)
    a_quantized_compressed_100_6bits = np.round(2**6*a_compressed_100)/(2**6)
    a_quantized_compressed_100_8bits = np.round(2**8*a_compressed_100)/(2**8)

    u_expanded_100_3bits = u_Law_Expansion(u_quantized_compressed_100_3bits,100)
    u_expanded_100_6bits = u_Law_Expansion(u_quantized_compressed_100_6bits,100)
    u_expanded_100_8bits = u_Law_Expansion(u_quantized_compressed_100_8bits,100)

    a_expanded_100_3bits = A_Law_Expansion(a_quantized_compressed_100_3bits,100)
    a_expanded_100_6bits = A_Law_Expansion(a_quantized_compressed_100_6bits,100)
    a_expanded_100_8bits = A_Law_Expansion(a_quantized_compressed_100_8bits,100)
    
    std_u_expanded_3bit = np.std([u_expanded_100_3bits, input])
    std_u_expanded_6bit = np.std([u_expanded_100_6bits, input])
    std_u_expanded_8bit = np.std([u_expanded_100_8bits, input])

    std_a_expanded_3bit = np.std([a_expanded_100_3bits, input])
    std_a_expanded_6bit = np.std([a_expanded_100_6bits, input])
    std_a_expanded_8bit = np.std([a_expanded_100_8bits, input])

    diff_u_expanded_3bit = np.abs(np.subtract(input, u_expanded_100_3bits))
    diff_u_expanded_6bit = np.abs(np.subtract(input, u_expanded_100_6bits))
    diff_u_expanded_8bit = np.abs(np.subtract(input, u_expanded_100_8bits))

    diff_a_expanded_3bit = np.abs(np.subtract(input, a_expanded_100_3bits))
    diff_a_expanded_6bit = np.abs(np.subtract(input, a_expanded_100_6bits))
    diff_a_expanded_8bit = np.abs(np.subtract(input, a_expanded_100_8bits))

    min_diff_u_expanded_3bit = np.min(diff_u_expanded_3bit)
    min_diff_u_expanded_6bit = np.min(diff_u_expanded_6bit)
    min_diff_u_expanded_8bit = np.min(diff_u_expanded_8bit)

    min_diff_a_expanded_3bit = np.min(diff_a_expanded_3bit)
    min_diff_a_expanded_6bit = np.min(diff_a_expanded_6bit)
    min_diff_a_expanded_8bit = np.min(diff_a_expanded_8bit)

    max_diff_u_expanded_3bit = np.max(diff_u_expanded_3bit)
    max_diff_u_expanded_6bit = np.max(diff_u_expanded_6bit)
    max_diff_u_expanded_8bit = np.max(diff_u_expanded_8bit)

    max_diff_a_expanded_3bit = np.max(diff_a_expanded_3bit)
    max_diff_a_expanded_6bit = np.max(diff_a_expanded_6bit)
    max_diff_a_expanded_8bit = np.max(diff_a_expanded_8bit)

    mean_diff_u_expanded_3bit = np.mean(diff_u_expanded_3bit)
    mean_diff_u_expanded_6bit = np.mean(diff_u_expanded_6bit)
    mean_diff_u_expanded_8bit = np.mean(diff_u_expanded_8bit)

    mean_diff_a_expanded_3bit = np.mean(diff_a_expanded_3bit)
    mean_diff_a_expanded_6bit = np.mean(diff_a_expanded_6bit)
    mean_diff_a_expanded_8bit = np.mean(diff_a_expanded_8bit)

    print(f"u bits = 3, std: {std_u_expanded_3bit}, mean: {mean_diff_u_expanded_3bit}, min: {min_diff_u_expanded_3bit}, max: {max_diff_u_expanded_3bit}")
    print(f"u bits = 6, std: {std_u_expanded_6bit}, mean: {mean_diff_u_expanded_6bit}, min: {min_diff_u_expanded_6bit}, max: {max_diff_u_expanded_6bit}")
    print(f"u bits = 8, std: {std_u_expanded_8bit}, mean: {mean_diff_u_expanded_8bit}, min: {min_diff_u_expanded_8bit}, max: {max_diff_u_expanded_8bit}")

    print(f"a bits = 3, std: {std_a_expanded_3bit}, mean: {mean_diff_a_expanded_3bit}, min: {min_diff_a_expanded_3bit}, max: {max_diff_a_expanded_3bit}")
    print(f"a bits = 6, std: {std_a_expanded_6bit}, mean: {mean_diff_a_expanded_6bit}, min: {min_diff_a_expanded_6bit}, max: {max_diff_a_expanded_6bit}")
    print(f"a bits = 8, std: {std_a_expanded_8bit}, mean: {mean_diff_a_expanded_8bit}, min: {min_diff_a_expanded_8bit}, max: {max_diff_a_expanded_8bit}")

