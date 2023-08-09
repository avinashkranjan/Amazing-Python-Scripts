# AI-based Music Composer

This project is an AI-based music composer that generates unique pieces of music based on user preferences or specific genres. The script uses the `magenta` library, which provides pre-trained models for music generation.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [User Input](#user-input)
- [Chord Progressions](#chord-progressions)
- [Drum Accompaniment](#drum-accompaniment)
- [Generated Music](#generated-music)
- [Contributing](#contributing)

## Introduction

Music is an integral part of human expression, and this project aims to create an AI-based music composer that can generate melodies in various genres. The generated music can be saved as MIDI files and can serve as a starting point for further music composition and creativity.

## Features

- Generates unique melodies based on pre-trained models.
- Allows user input for preferred genre and tempo.
- Adds chord progressions based on the chosen genre to create harmonic accompaniments.
- Includes a simple drum pattern for rhythmic accompaniment.
- Outputs generated music as MIDI files.

## Installation

1. Clone the repository to your local machine:

2. Install the required dependencies:

```bash
pip install magenta
```

## Usage
To generate music pieces using the AI-based music composer, run the following command:

```bash
python music_composer.py
```
The script will prompt you to enter your preferred genre and tempo (BPM) for music generation.

## User Input
The script allows you to input your preferred genre, which can be one of the following:

- Classical
- Jazz
- Rock
Additionally, you can specify the tempo (in BPM) for the generated music.

## Chord Progressions
The chosen genre determines the chord progression for the generated music. Currently, the supported chord progressions are:

- Classical: ["C", "Am", "F", "G"]
- Jazz: ["Cmaj7", "Dm7", "Em7", "A7"]
- Rock: ["C", "G", "Am", "F"]
You can modify or extend these chord progressions in the music_composer.py file.

## Drum Accompaniment
The music pieces include a basic drum pattern for rhythmic accompaniment. The drum pattern consists of a kick drum (36) and hi-hat (42). You can adjust the drum pattern in the music_composer.py file to create different rhythms.

## Generated Music
The generated music will be saved as MIDI files in the generated_music directory. Each music piece will have a unique file name, such as music_piece_1.mid, music_piece_2.mid, and so on.

## Contributing
If you have any ideas, improvements, or bug fixes, feel free to open an issue or submit a pull request. We appreciate your contributions!


