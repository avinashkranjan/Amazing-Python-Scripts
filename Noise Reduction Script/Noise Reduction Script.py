# Spectral Subtraction: Method used for noise reduction 
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt

file = input("Enter the file path: ")
sr, data = wav.read(file)
fl = 400 #frame_length
frames = []  #empty list 
for i in range(0,int(len(data)/(int(fl/2))-1)):
    arr = data[int(i*int(fl/2)):int(i*int(fl/2)+fl)]  
    frames.append(arr)    #appending each array data into the frames list
frames = np.array(frames)   #converting the frames list into an array
ham_window = np.hamming(fl)    #using np.hamming 
windowed_frames = frames*ham_window    #multiplying frames array with ham_window
dft = []   #empty list containing fft of windowed_frames
for i in windowed_frames:
    dft.append(np.fft.fft(i))   #now taking the first fourier transform of each window
dft = np.array(dft)  #converting dft into array

dft_mag_spec = np.abs(dft)      #converting dft into absolute values
dft_phase_spec = np.angle(dft)   #finding dft angle
noise_estimate = np.mean(dft_mag_spec,axis=0)    #mean
noise_estimate_mag = np.abs(noise_estimate)   #absolute value

estimate_mag = (dft_mag_spec-2*noise_estimate_mag)   #subtraction method
estimate_mag[estimate_mag<0]=0
estimate = estimate_mag*np.exp(1j*dft_phase_spec)  #calculating the final estimate
ift = []   #taking ift as input list containing inverse fourier transform of estimate
for i in estimate:
    ift.append(np.fft.ifft(i))    #appending in ift list 

clean_data = []
clean_data.extend(ift[0][:int(fl/2)])     #extending clean_data containg ift list
for i in range(len(ift)-1):   
    clean_data.extend(ift[i][int(fl/2):]+ift[i+1][:int(fl/2)])
clean_data.extend(ift[-1][int(fl/2):])   #extending clean_data containing ift list
clean_data = np.array(clean_data)  #converting it into array

#finally plotting the graph showing the diffrence in the noise
fig = plt.figure(figsize=(8,5))
ax = plt.subplot(1,1,1)
ax.plot(np.linspace(0,64000,64000),data,label='Original',color="orange")
ax.plot(np.linspace(0,64000,64000),clean_data,label='Filtered',color="purple")
ax.legend(fontsize=12)
ax.set_title('Spectral Subtraction Method', fontsize=15)
filename = os.path.basename(file)
cleaned_file = "(Filtered_Audio)"+filename   #final filtered audio
wav.write(cleaned_file,rate=sr, data = clean_data.astype(np.int16))
plt.savefig(filename+"(Spectral Subtraction graph).jpg")  #saved file name as audio.wav(Spectral Subtraction graph).jpg
