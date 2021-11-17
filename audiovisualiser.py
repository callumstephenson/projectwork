###IMPORTS
### Fourier transform applied to a song to decompose into the
### constituent frequencies of the song, plotted with dB amplitude scale
### usually run on colab to make use of drive functionality
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
from google.colab import drive
###IMPORT SONG
music_file =  #filepath here
####MEL PLOT TYPE
y, sr = librosa.load(music_file)
# trim silent edges
song, _ = librosa.effects.trim(y)
n_fft = 2048
hop_length = 512
plt.figure(figsize=(150,100))
D = np.abs(librosa.stft(song, n_fft=n_fft,  hop_length=hop_length))
DB = librosa.amplitude_to_db(D, ref=np.max)
librosa.display.specshow(DB, sr=sr, hop_length=hop_length, x_axis='time', y_axis='log');
plt.set_cmap("ocean")
plt.axis('off')
plt.savefig('/content/decomposition.png',bbox_inches='tight')