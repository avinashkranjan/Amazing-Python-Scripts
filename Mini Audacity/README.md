
# Removing background noise from an audio file just like "Audacity"

Used some of the python libraries to filter the background noise to get a clear audio file

* scipy
* NumPy
* librosa
* scipy.io.wavfile
* Matplotlib
* scipy.io


## Steps:
* Imported the required libraries (scipy, NumPy, librosa, scipy.io.wavfile, Matplotlib, scipy.io)
* Read the input audio file using librosa library

### Methods applied 
* Converting the audio file into an array containg all the information of the given audio file.
* Calculating short time fourier transform of both pure audio file as well as noisy audio file 
* Subtracting the noise spectral mean from input spectral, and istft (Inverse Short-Time Fourier Transform)
* Applying phase transformation to convert it into time domain signal
* Finally getting an audio file with reduction in the background noise at a much higher extent




