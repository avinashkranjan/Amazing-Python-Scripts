# Reinforcement Learning with SpaceInvaders-v0

This repository contains code for implementing reinforcement learning using the SpaceInvaders-v0 environment from the OpenAI Gym.

## Prerequisites

To run this code, you need the following dependencies:

- Python 3.x
- Gym: `pip install gym`
- TensorFlow: `pip install tensorflow`
- Keras-RL2: `pip install keras-rl2`

## Getting Started

1. Clone the repository: `git clone https://github.com/your_username/your_repository.git`
2. Navigate to the cloned repository: `cd your_repository`

## Running the Code

1. Open the Python script `space_invaders_rl.py`.
2. Configure the number of episodes and other parameters as needed.
3. Run the script: `python space_invaders_rl.py`.

## Understanding the Code

The code performs the following steps:

1. Imports the necessary libraries and initializes the SpaceInvaders-v0 environment.
2. Runs a specified number of episodes, where each episode represents a game.
3. Resets the environment for each episode and plays the game until completion.
4. Renders the environment to visualize the game.
5. Uses a random policy to select actions.
6. Accumulates the score and prints the episode number and score.
7. Closes the environment after all episodes have been completed.
8. Builds a convolutional neural network model using Keras.
9. Implements the DQN agent using the Keras-RL2 library.
10. Compiles the agent with the Adam optimizer.
11. Trains the agent on the SpaceInvaders-v0 environment.
12. Tests the trained agent on a few episodes and calculates the average score.
13. Saves the trained weights of the DQN agent.
14. Loads the saved weights of the DQN agent.


## Acknowledgments

- [OpenAI Gym](https://gym.openai.com/)
- [Keras-RL2](https://github.com/wau/keras-rl2)

Feel free to modify and adapt this code according to your needs.

