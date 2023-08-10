import random
import time
import numpy as np
import pyaudio

# Dictionary to hold sound characteristics
sounds = {
    "raindrops": {"min_freq": 100, "max_freq": 300, "min_duration": 0.1, "max_duration": 0.5},
    "rustling_leaves": {"min_freq": 500, "max_freq": 1500, "min_duration": 0.2, "max_duration": 0.7},
    "chirping_birds": {"min_freq": 1000, "max_freq": 5000, "min_duration": 0.2, "max_duration": 0.4}
}


def play_sound(frequency, duration, volume=1.0):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    audio_data = np.sin(2 * np.pi * frequency * t)
    audio_data *= volume

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    stream.write(audio_data.tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()


def main():
    num_channels = 3  # Number of simultaneous channels
    channel_volume = 0.5  # Volume for each channel (adjust as needed)

    while True:
        user_input = input("Enter sound(s) you want to hear (comma-separated) "
                           "or 'all' for all sounds (e.g., 'raindrops,chirping_birds'): ")

        if user_input.lower() == 'all':
            selected_sounds = list(sounds.keys())
        else:
            selected_sounds = [sound.strip()
                               for sound in user_input.split(",")]

        random.shuffle(selected_sounds)  # Randomize sound order

        for _ in range(num_channels):
            if not selected_sounds:
                break

            sound_choice = selected_sounds.pop()
            sound_params = sounds[sound_choice]

            # Add slight variations to frequency and duration
            frequency = random.uniform(
                sound_params["min_freq"], sound_params["max_freq"])
            duration = random.uniform(
                sound_params["min_duration"], sound_params["max_duration"])

            # Volume variation for each channel
            volume = channel_volume + random.uniform(-0.2, 0.2)
            volume = max(0.0, min(1.0, volume))

            print(f"Playing {sound_choice}...")
            play_sound(frequency, duration, volume)

            # Random delay between sounds
            time.sleep(random.uniform(1, 4))


if __name__ == "__main__":
    main()
