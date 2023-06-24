# Q-Learning with Taxi-v3 Environment

This repository contains code for implementing the Q-Learning algorithm using the Taxi-v3 environment from the OpenAI Gym.

## Prerequisites

To run this code, you need the following dependencies:

- Python 3.x
- Gym: `pip install gym`
- NumPy: `pip install numpy`

## Getting Started

1. Clone the repository: `git clone https://github.com/your_username/your_repository.git`
2. Navigate to the cloned repository: `cd your_repository`

## Running the Code

1. Open the Python script `q_learning_taxi.py`.
2. Configure the number of episodes, learning parameters, and other settings as needed.
3. Run the script: `python q_learning_taxi.py`.

## Understanding the Code

The code performs the following steps:

1. Imports the necessary libraries and initializes the Taxi-v3 environment.
2. Runs a specified number of episodes, where each episode represents a learning iteration.
3. Resets the environment for each episode and plays the game until completion.
4. Renders the environment to visualize the game.
5. Selects actions randomly for exploration or based on the learned Q-values for exploitation.
6. Updates the Q-table based on the Q-Learning algorithm.
7. Adjusts the exploration rate over time to balance exploration and exploitation.
8. Stores the rewards obtained in each episode.
9. Prints the Q-table after training.
10. Calculates and prints the average reward per thousand episodes.
11. Visualizes the agent's performance in a few test episodes.



## Acknowledgments

- [OpenAI Gym](https://gym.openai.com/)

Feel free to modify and adapt this code according to your needs.

