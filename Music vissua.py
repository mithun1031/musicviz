import pyaudio
import librosa
import matplotlib.pyplot as plt
import IPython.display as ipd
import librosa.display
import numpy as np

from playsound import playsound
playsound('music.mp3')
x= playsound                 
audio, sr = librosa.load(x) 
plt.figure(figsize=(10,5))
librosa.display.waveplot(audio)  
plt.title("audio")
plt.ylim((-1,1))
plt.show()