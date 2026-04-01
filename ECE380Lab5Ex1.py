#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import ECE380Lab5Ex1_epy_block_0 as epy_block_0  # embedded python block
import ECE380Lab5Ex1_epy_block_1 as epy_block_1  # embedded python block
import ECE380Lab5Ex1_epy_block_2 as epy_block_2  # embedded python block
import numpy as np
import sip
import threading



class ECE380Lab5Ex1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "ECE380Lab5Ex1")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.num_levels = num_levels = 5
        self.audio_source = audio_source = 0
        self.amplitude_max = amplitude_max = 1
        self.a = a = 1

        ##################################################
        # Blocks
        ##################################################

        self._num_levels_range = qtgui.Range(3, 256, 1, 5, 200)
        self._num_levels_win = qtgui.RangeWidget(self._num_levels_range, self.set_num_levels, "'num_levels'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._num_levels_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        # Create the options list
        self._audio_source_options = [0, 1, 2]
        # Create the labels list
        self._audio_source_labels = ['Wav File', 'Tone', '2']
        # Create the combo box
        self._audio_source_tool_bar = Qt.QToolBar(self)
        self._audio_source_tool_bar.addWidget(Qt.QLabel("Audio Source" + ": "))
        self._audio_source_combo_box = Qt.QComboBox()
        self._audio_source_tool_bar.addWidget(self._audio_source_combo_box)
        for _label in self._audio_source_labels: self._audio_source_combo_box.addItem(_label)
        self._audio_source_callback = lambda i: Qt.QMetaObject.invokeMethod(self._audio_source_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._audio_source_options.index(i)))
        self._audio_source_callback(self.audio_source)
        self._audio_source_combo_box.currentIndexChanged.connect(
            lambda i: self.set_audio_source(self._audio_source_options[i]))
        # Create the radio buttons
        self.top_grid_layout.addWidget(self._audio_source_tool_bar, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._a_range = qtgui.Range(0, 255, 1, 1, 200)
        self._a_win = qtgui.RangeWidget(self._a_range, self.set_a, "a", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._a_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0.enable_tags(True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0.enable_stem_plot(False)


        labels = ['Compressed Signal', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_0_win, 1, 0, 1, 4)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


        labels = ['Expanded Signal', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_win, 2, 0, 1, 4)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.epy_block_2 = epy_block_2.blk(A=a)
        self.epy_block_1 = epy_block_1.blk(A=a)
        self.epy_block_0 = epy_block_0.blk(quant_min=-1*amplitude_max, quant_max=amplitude_max, quant_level=num_levels)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('C:\\Users\\aslator\\Downloads\\Intro_to_the_Universal_Declaration_of_Human_Rights_48k_Alaw.wav', True)
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_selector_0 = blocks.selector(gr.sizeof_float*1,audio_source,0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff((2/(num_levels-1)))
        self.blocks_add_const_vxx_0 = blocks.add_const_ff((-1*(num_levels-1)/2))
        self.audio_sink_0 = audio.sink(samp_rate, '', True)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 400, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_selector_0, 1))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.epy_block_2, 0))
        self.connect((self.blocks_selector_0, 0), (self.epy_block_1, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_selector_0, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.epy_block_1, 0), (self.epy_block_0, 0))
        self.connect((self.epy_block_1, 0), (self.qtgui_time_sink_x_1_0, 0))
        self.connect((self.epy_block_2, 0), (self.audio_sink_0, 0))
        self.connect((self.epy_block_2, 0), (self.qtgui_time_sink_x_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "ECE380Lab5Ex1")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.samp_rate)

    def get_num_levels(self):
        return self.num_levels

    def set_num_levels(self, num_levels):
        self.num_levels = num_levels
        self.blocks_add_const_vxx_0.set_k((-1*(self.num_levels-1)/2))
        self.blocks_multiply_const_vxx_0.set_k((2/(self.num_levels-1)))
        self.epy_block_0.quant_level = self.num_levels

    def get_audio_source(self):
        return self.audio_source

    def set_audio_source(self, audio_source):
        self.audio_source = audio_source
        self._audio_source_callback(self.audio_source)
        self.blocks_selector_0.set_input_index(self.audio_source)

    def get_amplitude_max(self):
        return self.amplitude_max

    def set_amplitude_max(self, amplitude_max):
        self.amplitude_max = amplitude_max
        self.epy_block_0.quant_max = self.amplitude_max
        self.epy_block_0.quant_min = -1*self.amplitude_max

    def get_a(self):
        return self.a

    def set_a(self, a):
        self.a = a
        self.epy_block_1.A = self.a
        self.epy_block_2.A = self.a




def main(top_block_cls=ECE380Lab5Ex1, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
