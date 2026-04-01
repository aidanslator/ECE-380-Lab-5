"""Uniform quantization

    Source : Based on Section 2.2.2.2 of Meinhard Mueller's Fundamentals of Music Processing
    
    https://www.audiolabs-erlangen.de/resources/MIR/FMP/C2/C2S2_DigitalSignalQuantization.html

    Notebook: C2/C2S2_DigitalSignalQuantization.ipynb

    Args:
        x (np.ndarray): Original signal
        quant_min (float): Minimum quantization level (Default value = -1.0)
        quant_max (float): Maximum quantization level (Default value = 1.0)
        quant_level (int): Number of quantization levels (Default value = 5)

    Returns:
        x_quant (np.ndarray): Quantized signal
"""

import numpy as np
import math
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block implementing quantization up to 8 bits"""

    def __init__(self, quant_min=-1.0, quant_max=1.0, quant_level=5):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Quantize Block',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.int8]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.quant_min = quant_min
        self.quant_max = quant_max
        self.quant_level = quant_level
        print(quant_level)

    def work(self, input_items, output_items):
        """Using the provided parameters, normalize, quantize, and scale the input samples"""
        x_normalize = (input_items[0] - self.quant_min) * (self.quant_level-1) / (self.quant_max-self.quant_min)
        x_normalize[x_normalize > self.quant_level - 1] = self.quant_level - 1
        x_normalize[x_normalize < 0] = 0
        """We want integer values, so round to the nearest integer"""
        x_normalize_quant = np.around(x_normalize)
        
        output_items[0][:] = x_normalize_quant
        return len(output_items[0])
