###IMPORTS
### Fourier transform applied to a song to decompose into the
### constituent frequencies of the song, plotted with dB amplitude scale
### usually run on colab to make use of drive functionality
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
from google.colab import drive
def imageProcessing(inputPath, outputPath, cmapInput='binary', figsizeInput=(6.4,4.8), hop_lengthInput=512 , n_fftInput=2048, offsetInput=0, colourIteration=False):
  '''A function to iterate over a directory filled with .mp3 files and decompose them using an FFT into .pngs. 
  inputPath = input folder path
  outputPath = output folder path
  hop_lengthInput = sample length to apply FFT
  n_fftInput = length of the windowed signal after padding with zeros, recommended to set to a power of 2.
  cmapInput = colour map for the resulting image
  offsetInput = offset from start of song to generate audio
  colourIteration = if you want the program to iterate over all colour maps
  pre-requisite packages: numpy (as np), matplotlib.pyplot(as plt), librosa, librosa.display, os'''
  
  musicFolder = os.listdir(str(inputPath))
  i=0
  FileAmount = len(musicFolder)
  for musicFile in musicFolder: 
    # File handling and output namescheme
    InputPath = str(inputPath) + musicFile
    OutputPath = str(outputPath) + musicFile[0:-4] + '_image.png'
    y, sr = librosa.load(InputPath,offset = offsetInput)
    # Trim Silent Edges
    plt.figure(figsize=figsizeInput)
    song, _ = librosa.effects.trim(y)
    D = np.abs(librosa.stft(song, n_fft=n_fftInput,  hop_length=hop_lengthInput))
    DB = librosa.amplitude_to_db(D, ref=np.max)
    librosa.display.specshow(DB, sr=sr, hop_length=hop_lengthInput, x_axis='time', y_axis='log');
    #Set colourmap of output image.
    if colourIteration == False:
      plt.set_cmap(str(cmapInput))
      plt.axis('off')
      plt.savefig(OutputPath,bbox_inches='tight')
    else:
      for colourmap in matplotlib.plr.colormaps():
        plt.set_cmap(str(colourmap))
        plt.axis('off')
        plt.savefig(OutputPath,bbox_inches='tight')
