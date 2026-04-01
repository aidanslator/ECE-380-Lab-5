"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr

def A_Law_Expansion(input,A) -> np.ndarray: 

    if(A <= 0):
        return input
        
    output = []
    for v in input:
        if(np.abs(v) < 1/(1 + np.log(A))):
            g = np.sign(v)*np.abs(v)*(1 + np.log(A))/A
        else:
            g = np.sign(v)*np.exp(-1 + np.abs(v)*(1 + np.log(A)))/A    
        output.append(g)
    return output

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, A=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='A Log Expander',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.A = A

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        output_items[0][:] = A_Law_Expansion(input_items[0],self.A)
        return len(output_items[0])
