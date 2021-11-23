###IMPORTS
### Fourier transform applied to a song to decompose into the
### constituent frequencies of the song, plotted with dB amplitude scale
### usually run on colab to make use of drive functionality
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
from google.colab import drive
def spectragram(inputPath, outputPath, cmapInput='binary', figsizeInput=(6.4,4.8), hop_lengthInput=512 , n_fftInput=2048, InputOffset=0):
  '''A function to convert an mp3 file to a PNG. 
  inputPath = input folder path
  outputPath = output folder path
  op_length = sample length to apply FFT
  n_fft = length of the windowed signal after padding with zeros, recommended to set to a power of 2.
  cmap = colour map for the resulting image
  pltaxis = if resulting image has axis
  offset = offset from start of song to generate audio
  pre-requisite packages: numpy (as np), matplotlib.pyplot(as plt), librosa, librosa.display, os'''
  
  musicFolder = os.listdir(str(inputPath))
  i=0
  FileAmount = len(musicFolder)
  for musicFile in musicFolder:
    # File handling and output namescheme
    InputPath = str(inputPath) + musicFile
    OutputPath = str(outputPath) + musicFile[0:-4] + '_image.png'
    y, sr = librosa.load(InputPath,offset=InputOffset)
    # Trim Silent Edges
    plt.figure(figsize=figsizeInput)
    song, _ = librosa.effects.trim(y)
    D = np.abs(librosa.stft(song, n_fft=n_fftInput,  hop_length=hop_lengthInput))
    DB = librosa.amplitude_to_db(D, ref=np.max)
    librosa.display.specshow(DB, sr=sr, hop_length=hop_lengthInput, x_axis='time', y_axis='log');
    #Set colourmap of output image.
    plt.set_cmap(str(cmapInput))
    plt.axis('off')
    plt.savefig(OutputPath,bbox_inches='tight')
    ### RUN FUNCTION WITH CORRECT ARGS TO GET OUTPUT, ALL NECESSARY DEFAULT ARGS ARE SET.
