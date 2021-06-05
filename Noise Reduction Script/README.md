# Noise Reduction Script
Implementing a feature that helps to filter an audio file by reducing the background noise similar to "Audacity".

## Libraries used
Firstly import the following python libraries 
* NumPy
* scipy.io.wavfile
* Matplotlib
* Os
Save the audio files and your code in the same folder
Run the python code

## Detailed explanation of method used for "Noise Reduction Script" 
* Imported the required libraries (NumPy, scipy.io.wavfile, and Matplotlib)
* Read the input audio file using scipy.io.wavfile library
* Converting the audio file into an array containg all the information of the given audio file and intiallizing the frame value.
* Calculating the first fourier transform of each window of the noisy audio file 
* Subtracting the noise spectral mean from input spectral, and istft (Inverse Short-Time Fourier Transform)
* Finally getting an audio file with reduction in the background noise at a much higher extent

## Output
<img src="Graph/test_noise.wav(Spectral Subtraction graph).jpg" height="500px">

## Author(s)
[Akriti](https://github.com/A-kriti)
