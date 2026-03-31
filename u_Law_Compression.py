import matplotlib.pyplot as plt
import numpy as np

def u_Law_Compress(input,u) -> np.ndarray:
    if(u <= 0):
        return input
    return np.sign(input) * np.log(1+u*np.abs(input))/(np.log(1+u))

if __name__ == "__main__":
    input = np.linspace(-1,1)
    compressed_0 = u_Law_Compress(input,0)
    compressed_5 = u_Law_Compress(input,5)
    compressed_100 = u_Law_Compress(input,100)

    plt.plot(input,compressed_0,label='u = 0',color='blue')
    plt.plot(input,compressed_5,label='u = 5',color='orange')
    plt.plot(input,compressed_100,label='u = 100',color='green')
    plt.xlabel('Normalized input, g')
    plt.ylabel('Normalized output, v')
    plt.title("Mu-Law Compression")
    plt.legend()
    #plt.saveFig("u_Law.png")
    plt.show()
    
