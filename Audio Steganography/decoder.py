import wave

#asking user to enter filename
file_name_wav = input("Enter the .wav file name : ")

#opening wav file
audio_file = wave.open(file_name_wav, mode='rb')

#converting audio to byte array by reading the n frames

#getting number of frames
n_frames = audio_file.getnframes()
#reading the frames
arr_read_nframe = audio_file.readframes(n_frames)
#conversion to byte array
audio_byte_arr = bytearray(list(arr_read_nframe))

#Now we have to extract the LSB so by anding with 1 we get LSB.
bytes_a = [audio_byte_arr[i] & 1 for i in range(len(audio_byte_arr))]

#Now we have secret message in byte from so converting to string includes binary to decimal by taking 8 binary,
se = "".join(chr(int("".join(map(str,bytes_a[i:i+8])),2)) for i in range(0,len(bytes_a),8))

#removing the added special char
secret_msg = se.split("~~")[0]

#printing the hide msg
print("Hidden Message: "+secret_msg)
audio_file.close()