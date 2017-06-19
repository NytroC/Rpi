import sys, pygame, pyaudio, numpy
import math
import struct
import time
pygame.init()

size = width, height = 1080, 720
black = 0, 0, 0
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 4410
CHUNK = 1024
RECORD_SECONDS = 5
 
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)

screen = pygame.display.set_mode(size)
counter = 0
while 1:
    stream.start_stream()
    data = stream.read(CHUNK)
    stream.stop_stream()
    numpydata = numpy.fromstring(data, dtype=numpy.int16)
    y = numpydata[1]
    screen.fill(black)
    for x in range(width):
        if numpydata[x] > 0:
            pygame.draw.rect(screen, (255,255,255), (x, (numpydata[x] * -1) + 300, 5, 100),0)
        else:
            pygame.draw.rect(screen, (255,255,255), (x,300, 5, 100),0)
    pygame.display.update()
    counter = counter + 1
    #time.sleep(5)