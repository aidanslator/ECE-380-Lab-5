import matplotlib.pyplot as plt
import numpy as np

def delta_modulation(message, step_size)-> np.ndarray: 

    output = []
    
    mq = 0
    e = 0
    
    for m in message:
        e = m - mq
        sign = np.sign(e)
        
        if sign > 0:
            output.append(True)
        else:
            output.append(False)
        mq += step_size*(1 if output[-1] == True else -1)
        print(f"mq: {mq}, m: {m}, sign: {sign}")

    return output

def delta_reconstruction(modulated_signal, step_size)-> np.ndarray: 

    output = []
    curr_val = 0

    for x in modulated_signal:
        if x == True:
            curr_val += step_size
        elif x == False:
            curr_val -= step_size

        output.append(curr_val)

    return output

if __name__ == "__main__":

    t = np.linspace(0, 1, 50)
    x = 2*np.sin(2*np.pi*t)+3*np.sin(6*np.pi*t)

    delta_mod_05step = delta_modulation(x, 0.5)
    delta_mod_1step = delta_modulation(x, 1)
    delta_mod_2step = delta_modulation(x, 2)

    reconstruct_05step = delta_reconstruction(delta_mod_05step, 0.5)
    reconstruct_1step = delta_reconstruction(delta_mod_1step, 1)
    reconstruct_2step = delta_reconstruction(delta_mod_2step, 2)

    for i in range(0, 50):
        print(f"x: {x[i]}, u: {reconstruct_05step[i]}")

    plt.plot(t, x, label='message',color='blue')
    plt.step(t, reconstruct_05step, label='step = 0.5',color='orange', where='post')
    plt.xlabel('time, s')
    plt.title("Delta Mod Step = 0.5")
    plt.legend()
    plt.show()

    plt.plot(t, x, label='message',color='blue')
    plt.step(t, reconstruct_1step, label='step = 1',color='orange', where='post')
    plt.xlabel('time, s')
    plt.title("Delta Mod Step = 1")
    plt.legend()
    plt.show()

    plt.plot(t, x, label='message',color='blue')
    plt.step(t, reconstruct_2step, label='step = 2',color='orange',where='post')
    plt.xlabel('time, s')
    plt.title("Delta Mod Step = 2")
    plt.legend()
    plt.show()


    
