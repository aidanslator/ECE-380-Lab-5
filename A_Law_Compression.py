import matplotlib.pyplot as plt
import numpy as np

def A_Law_Compress(input,A): 
    if(A == 1):
        return input
    
    denominator = 1+np.log(A)
    
    output = []
    for g in input:
        if(np.abs(g) < 1/A):
            v = np.sign(g)*A*np.abs(g)/denominator
        else:
            v = np.sign(g)*(1+np.log(A*np.abs(g)))/denominator    
        output.append(v)
    return output

if __name__ == "__main__":
    input = np.linspace(-1,1)
    compressed_1 = A_Law_Compress(input,1)
    compressed_2 = A_Law_Compress(input,2)
    compressed_100 = A_Law_Compress(input,100)

    plt.plot(input,compressed_1,label='A = 1',color='blue')
    plt.plot(input,compressed_2,label='A = 2',color='orange')
    plt.plot(input,compressed_100,label='A = 100',color='green')
    plt.xlabel('Normalized input, g')
    plt.ylabel('Normalized output, v')
    plt.title("A-Law Compression")
    plt.legend()
    #plt.saveFig("A_Law.png")
    plt.show()
    
