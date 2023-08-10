import librosa
import matplotlib.pyplot as plt

audio = 'path/to/your/audio/file'  #replace this with the path to your file

x, sr = librosa.load(audio)
X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize = (10, 5))
librosa.display.specshow(Xdb, sr = sr, x_axis = 'time', y_axis = 'hz')
plt.colorbar()
plt.title('Spectrogram of '+ audio)
plt.show()  # This will show the plot