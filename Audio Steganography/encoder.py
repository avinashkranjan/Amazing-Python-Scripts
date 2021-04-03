import wave
from os import path
from pydub import AudioSegment

#asking user to enter file name
file_name_mp3 = input("Enter the .mp3 file name : ")
destination = "generated_wav.wav"

#convet .mp3 file to the .wav file
ss = AudioSegment.from_mp3(file_name_mp3)
ss.export(destination, format = "wav")

#opening .wav file
audio_file = wave.open(destination, mode='rb')

#converting audio to byte array by reading the n frames

#getting number of frames
n_frames = audio_file.getnframes()
#reading the frames
arr_read_nframe = audio_file.readframes(n_frames)
#conversion to byte array
audio_byte_arr = bytearray(list(arr_read_nframe))

#asking user to enter the secret message
secret_message = input("Enter the message you want to hide : ")

#Total frame we have devided by eight we have total number of 8-byte segment
#from each 8-byte we have to replace LSB by secret message.
#for that we need a secret message length of (total bytes/8).
#so we are appending the special chars in secret message.
secret_message = secret_message + '~' * int((len(audio_byte_arr)-(len(secret_message)*8*8))/8)

#convert secret message to corresponding bits.
sb = list(map(int, ''.join([bin(ord(c)).lstrip('0b').rjust(8,'0') for c in secret_message])))

#replacing the last bit of all frames with secret message bit
for index,c_bit in enumerate(sb):
    audio_byte_arr[index] = (audio_byte_arr[index] & 254) | c_bit

#wrinting into .wav file
f = wave.open('modified.wav', 'wb')
par = audio_file.getparams()
f.setparams(par)
f.writeframes(bytes(audio_byte_arr))

audio_file.close()
f.close()

print("\nYour text is hidden in audio file successfully.\n")