
#Test
import pyaudio
import numpy as np
from numpy import zeros,linspace,short,fromstring,hstack,transpose,log, ndarray
from scipy import fft
from time import sleep
import time
import piplates.DAQC2plate as DAQC2
#import openpyxl
#from openpyxl import Workbook
import struct
import scipy.fftpack
#import matplotlib.pyplot as plt
import piplates.RELAYplate as RELAY



global button_pressed
button_pressed=0
global which1
whcih1=[]
global row_index
row_index=4

# Set up audio sampler -
NUM_SAMPLES = 6144#12288 #24576 #previously 6144
SAMPLING_RATE = 48000
pa = pyaudio.PyAudio()
_stream = pa.open(format=pyaudio.paInt16,
                  channels=1, rate=SAMPLING_RATE,
                  input=True,
                  frames_per_buffer=NUM_SAMPLES)

print("Frequency detector working. Press CTRL-C to quit.")


def get_audio(): #Initiates audio stream and stores top 3 frequencies to top[]

    for i in range (0,4):
        while _stream.get_read_available()< NUM_SAMPLES: pass # sleep(0.005)
        audio_data  = fromstring(_stream.read(
             _stream.get_read_available(),exception_on_overflow=False), dtype=short)[-NUM_SAMPLES:]

        data = np.array(audio_data)

        w = np.fft.fft(data)
        freqs = np.fft.fftfreq(len(w))
        #print(freqs.min(), freqs.max())
        # (-0.5, 0.499975)

        # Find the peak in the coefficients
        idx = np.argmax(np.abs(w))
        freq = freqs[idx]
        freq_in_hertz = abs(freq * SAMPLING_RATE)
        print(int(freq_in_hertz))

    return

def button():
    if DAQC2.getDINbit(0,0) == 0:
        global button_pressed
        button_pressed = 1
        DAQC2.setDOUTbit(0,0)
        sleep(0.02)
        DAQC2.clrDOUTbit(0,0)
        sleep(0.015)
        relay()
        get_audio()
        
        button_pressed = 0
    return

def relay():
    global button_pressed
    
    
    if button_pressed ==1:
        RELAY.getID(1)
        'Pi-Plate RELAY'
        RELAY.relayON(1,1)
        sleep(0.02)
        RELAY.relayOFF(1,1)
        return()

run = None
while not run:
    button()
    
    
    
    matched_freq=[0,0,0,0,0,0,0,0,0,0]
