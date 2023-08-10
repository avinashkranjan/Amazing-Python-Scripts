import pygame
import random
import time

# Initialize pygame and mixer
pygame.init()
pygame.mixer.init()

# Define musical elements
music_elements = [
    "element1.wav",
    "element2.wav",
    "element3.wav",
    "element4.wav",
    "element5.wav",
    "element6.wav",
    "element7.wav",
    "element8.wav",
    "element9.wav",
    "element10.wav",
    "element11.wav",
    "element12.wav",
    "element13.wav",
    "element14.wav",
    "element15.wav",
    "element16.wav",
    "element17.wav",
    "element18.wav",
    "element19.wav",
    "element20.wav",
    "element21.wav",
    "element22.wav",
    "element23.wav",
    "element24.wav",
    "element25.wav",
    "element26.wav",
    "element27.wav",
    "element28.wav",
    "element29.wav",
    "element30.wav",
    "element31.wav",
    "element32.wav",
    "element33.wav",
    "element34.wav",
    "element35.wav",
    "element36.wav",
    "element37.wav",
    "element38.wav",
    "element39.wav",
    "element40.wav",
    "element41.wav",
    "element42.wav",
    "element43.wav",
    "element44.wav",
    "element45.wav",
    "element46.wav",
    "element47.wav",
    "element48.wav",
    "element49.wav",
    "element50.wav",
    "element51.wav",
    "element52.wav",
    "element53.wav",
    "element54.wav",
    "element55.wav",
    "element56.wav",
    "element57.wav",
    "element58.wav",
    "element59.wav",
    "element60.wav",
    "element61.wav",
    "element62.wav",
    "element63.wav",
    "element64.wav",
    "element65.wav",
    "element66.wav",
    "element67.wav",
    "element68.wav",
    "element69.wav",
    "element70.wav",
    "element71.wav",
    "element72.wav",
    "element73.wav",
    "element74.wav",
    "element75.wav",
    "element76.wav",
    "element77.wav",
    "element78.wav",
    "element79.wav",
    "element80.wav",
    "element81.wav",
    "element82.wav",
    "element83.wav",
    "element84.wav",
    "element85.wav",
    "element86.wav",
    "element87.wav",
    "element88.wav",
    "element89.wav",
    "element90.wav",
    "element91.wav",
    "element92.wav",
    "element93.wav",
    "element94.wav",
    "element95.wav",
    "element96.wav",
    "element97.wav",
    "element98.wav",
    "element99.wav",
    "element100.wav"
]

# Load the music elements
loaded_elements = [pygame.mixer.Sound(element) for element in music_elements]

# Play the initial music element
current_element = random.choice(loaded_elements)
current_element.play()

event_music_mapping = {
    "event1": ["element1.wav", "element2.wav"],
    "event2": ["element3.wav", "element4.wav"],
    "event3": ["element5.wav", "element6.wav"],
    "event4": ["element7.wav", "element8.wav"],
    "event5": ["element9.wav", "element10.wav"],
    "event6": ["element11.wav", "element12.wav"],
    "event7": ["element13.wav", "element14.wav"],
    "event8": ["element15.wav", "element16.wav"],
    "event9": ["element17.wav", "element18.wav"],
    "event10": ["element19.wav", "element20.wav"],
    "event11": ["element21.wav", "element22.wav"],
    "event12": ["element23.wav", "element24.wav"],
    "event13": ["element25.wav", "element26.wav"],
    "event14": ["element27.wav", "element28.wav"],
    "event15": ["element29.wav", "element30.wav"],
    "event16": ["element31.wav", "element32.wav"],
    "event17": ["element33.wav", "element34.wav"],
    "event18": ["element35.wav", "element36.wav"],
    "event19": ["element37.wav", "element38.wav"],
    "event20": ["element39.wav", "element40.wav"],
    "event21": ["element41.wav", "element42.wav"],
    "event22": ["element43.wav", "element44.wav"],
    "event23": ["element45.wav", "element46.wav"],
    "event24": ["element47.wav", "element48.wav"],
    "event25": ["element49.wav", "element50.wav"],
    "event26": ["element51.wav", "element52.wav"],
    "event27": ["element53.wav", "element54.wav"],
    "event28": ["element55.wav", "element56.wav"],
    "event29": ["element57.wav", "element58.wav"],
    "event30": ["element59.wav", "element60.wav"],
    "event31": ["element61.wav", "element62.wav"],
    "event32": ["element63.wav", "element64.wav"],
    "event33": ["element65.wav", "element66.wav"],
    "event34": ["element67.wav", "element68.wav"],
    "event35": ["element69.wav", "element70.wav"],
    "event36": ["element71.wav", "element72.wav"],
    "event37": ["element73.wav", "element74.wav"],
    "event38": ["element75.wav", "element76.wav"],
    "event39": ["element77.wav", "element78.wav"],
    "event40": ["element79.wav", "element80.wav"],
    "event41": ["element81.wav", "element82.wav"],
    "event42": ["element83.wav", "element84.wav"],
    "event43": ["element85.wav", "element86.wav"],
    "event44": ["element87.wav", "element88.wav"],
    "event45": ["element89.wav", "element90.wav"],
    "event46": ["element91.wav", "element92.wav"],
    "event47": ["element93.wav", "element94.wav"],
    "event48": ["element95.wav", "element96.wav"],
    "event49": ["element97.wav", "element98.wav"],
    "event50": ["element99.wav", "element100.wav"],
}

# Simulated in-game events


def simulate_game_events():
    while True:
        yield random.choice(list(event_music_mapping.keys()))

# Main loop


def main():
    events = simulate_game_events()

    for event in events:
        # Handle the in-game event and update the music
        if event in event_music_mapping:
            event_music = event_music_mapping[event]
            new_element = random.choice(event_music)
        else:
            new_element = random.choice(music_elements)

        if new_element != current_element:
            current_element.stop()
            current_element = pygame.mixer.Sound(new_element)
            current_element.play()

        # Simulated delay between events
        time.sleep(random.uniform(5, 15))


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
