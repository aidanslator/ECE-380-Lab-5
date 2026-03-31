import matplotlib.pyplot as plt
import numpy as np
from u_Law_Compression import u_Law_Compress
from A_Law_Compression import A_Law_Compress
from u_Law_Expansion import u_Law_Expansion
from A_Law_Expansion import A_Law_Expansion

if __name__ == "__main__":
    input = np.linspace(-1,1)

    u_compressed_100 = u_Law_Compress(input,100)
    a_compressed_100 = A_Law_Compress(input,100)

    u_quantized_compressed_100_3bits = 
    a_quantized_compressed_100

    u_expanded_100 = u_Law_Expansion(u_compressed_100,100)
    a_expanded_100 = A_Law_Expansion(a_compressed_100,100)
