import matplotlib.pyplot as plt
import numpy as np

def delta_modulation(message, step_size)-> np.ndarray: 

    output = []
    curr_val = 0

    for x in message:
        if curr_val < x:
            output.append(True)
            curr_val += step_size
        elif curr_val >= x:
            output.append(False)
            curr_val -= step_size

    return output

def delta_reconstruction(modulated_signal, step_size)-> np.ndarray: 

    output = [0]
    curr_val = 0

    for x in modulated_signal:
        if x == True:
            curr_val += step_size
            output.append(curr_val)
        elif x == False:
            curr_val -= step_size
            output.append(curr_val)

    output.pop()

    return output

if __name__ == "__main__":

    t = np.linspace(0,1, 50)
    x = 2*np.sin(2*np.pi*t)+3*np.sin(6*np.pi*t)

    delta_mod_05step = delta_modulation(x, 0.5)
    delta_mod_1step = delta_modulation(x, 1)
    delta_mod_2step = delta_modulation(x, 2)

    print(f"{delta_mod_05step}")

    reconstruct_05step = delta_reconstruction(delta_mod_05step, 0.5)
    reconstruct_1step = delta_reconstruction(delta_mod_1step, 1)
    reconstruct_2step = delta_reconstruction(delta_mod_2step, 2)

    plt.plot(t, x, label='message',color='blue')
    plt.step(t, reconstruct_05step, label='step = 0.5',color='orange')
    plt.xlabel('time, s')
    plt.title("Delta Mod Step = 0.5")
    plt.legend()
    plt.show()

    plt.plot(t, x, label='message',color='blue')
    plt.step(t, reconstruct_1step, label='step = 1',color='orange')
    plt.xlabel('time, s')
    plt.title("Delta Mod Step = 1")
    plt.legend()
    plt.show()

    plt.plot(t, x, label='message',color='blue')
    plt.step(t, reconstruct_2step, label='step = 2',color='orange')
    plt.xlabel('time, s')
    plt.title("Delta Mod Step = 2")
    plt.legend()
    plt.show()


    
