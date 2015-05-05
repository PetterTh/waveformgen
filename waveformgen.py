import pygame
import time
from pygame.locals import *

import math
import numpy


def main():
    
    size = (480, 360)
      
    bits = 16

    pygame.mixer.pre_init(44100, -bits, 2)   
    _display_surf = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    
    pygame.init()
    
    
    s = sound()
    _running = True
    while _running:
    
    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_KP_PLUS]:
                    s.freq=s.freq+50
                    s.update()
                    print(s.freq)
                if key[pygame.K_KP_MINUS]:
                    s.freq=s.freq-50
                    s.update()
                    print(s.freq)
            if event.type == pygame.QUIT:
                _running = False
                break
    
    pygame.quit()

class sound():
    
    freq=550
    waveform="Sine"
    s=0
    bits=16
    
    def __init__(self):        
        self.update()
        
        
    def update(self):
        self.genSample()
        if self.s!=0:
            self.stop()
        self.play()
        
    def genSample(self):
        
        duration = 0.1          # in seconds
        frequency = self.freq    
  
        sample_rate = 44100
    
        n_samples = int(round(duration*sample_rate))
    
        #setup our numpy array to handle 16 bit ints, which is what we set our mixer to expect with "bits" up above
        buf = numpy.zeros((n_samples, 2), dtype = numpy.int16)
        max_sample = 2**(self.bits - 1) - 1
    
        for s in range(n_samples):
            t = float(s)/sample_rate    # time in seconds
    
            #grab the x-coordinate of the sine wave at a given time, while constraining the sample to what our mixer is set to with "bits"
            buf[s][0] = int(round(max_sample*math.sin(2*math.pi*frequency*t)))        # left
            buf[s][1] = int(round(max_sample*math.sin(2*math.pi*frequency*t)))    # right
        self.buf = buf

    def play(self):
    
        self.s = pygame.sndarray.make_sound(self.buf)
        #play once, then loop forever
        self.s.play(loops = -1)
    
    def stop(self):
        
        self.s.stop()
        
main()    






    
