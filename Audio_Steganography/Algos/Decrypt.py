import os
import wave
import simpleaudio as sa
import numpy as np
from scipy.io import wavfile
import binascii

"""

 [NOTE] In this decryption algorithm we simply read the path of the audio from the user and we 
 get a numpy array from the same. We then read the LSB of the binary representation of the data and get a string 
 of binary data. Finally we convert this string to ascii charecters and write it to a file.

"""


class Decrypt:

    def __init__(self, audio_path):
        self.audio_path = audio_path
        self.audio_wave_obj = wave.open(audio_path)

    """ 
      This function is there for playing audio.
    """

    def play_audio(self) -> None:

        playing = sa.WaveObject.from_wave_read(self.audio_wave_obj)
        obj = playing.play()

        if obj.is_playing():
            print(f"Playing audio")

        obj.wait_done()

    """
      The decryption is done here.
    """

    def decrypt_audio(self, output_dir: str, file_name: str, gen_file_status: bool) -> (str, bool):
        if gen_file_status:
            curr_dir_path = os.getcwd()
            output_dir_path = os.path.join(curr_dir_path, output_dir)

            try:
                os.mkdir(output_dir_path)
            except:
                pass

        print(f"This might take some while if your secret message is big and might contain some rubbish data.")

        # Reading the data from the wav file
        samplerate, data = wavfile.read(self.audio_path)
        m, n = data.shape
        # Reshaping it to make the data easier to handle
        data_reshaped = data.reshape(m*n, 1)

        s = ""
        zeros = 0

        # Getting the LSB from each number
        for i in range(m*n):
            t = str(data_reshaped[i][0] & 1)
            if zeros < 9:
                s += t
            else:
                break
            if t == '0':
                zeros += 1
            if t == '1':
                zeros = 0

        # Making sure the bit-string is of length divisible by 8 as we have stored the input-secret as 8-bits only
        s = s[:((len(s)//8)*8)]

        # Converting bbinary string to utf-8
        in_bin = int(s, 2)
        byte_num = in_bin.bit_length() + 7 // 8
        bin_arr = in_bin.to_bytes(byte_num, "big")
        result = bin_arr.decode("utf-8", "ignore")

        # Writing to output file if status was given true
        if gen_file_status:
            try:
                with open(os.path.join(output_dir_path, file_name), "w", encoding="utf-8") as f:
                    f.write(result)
                print("Success !!!")
                return result, True
            except:
                print(("Error !!!"))
                pass
                return None, False
        else:
            return result, True
