# FlappyBird
This repository contains the implementation of two OpenAI Gym environments for the Flappy Bird game. The implementation of the game's logic and graphics was based on the FlapPyBird project.<br>

### In this flappy.py file I train the Neural Network model with reinforcement learning approach.
## Performance of trained Agent
https://user-images.githubusercontent.com/51924622/121337387-1dca1080-c93a-11eb-9b9f-61bf00bc327f.mp4 

<br>
To check the performance and visualize the agent uncomment the agent.perform() and comment the agent.train() in the flappy.py file. <br>
if __name__ == '__main__':<br>
    &nbsp; agent = DQNAgent()<br>
    &nbsp; #agent.train()<br>
    &nbsp; agent.perform()<br>
    
    
### Perform Function:<br>

![Capture1](https://user-images.githubusercontent.com/51924622/121318965-5f9e8b00-c929-11eb-86d3-96ea6abb43b6.PNG)

## Train the Agent
 For train the agent uncomment the agent.train() in the .py file.<br>
 if __name__ == '__main__':<br>
    &nbsp; agent = DQNAgent()<br>
    &nbsp; agent.train()<br>
    &nbsp; #agent.perform()<br>
 
 ### Train Function:<br>
![Capture](https://user-images.githubusercontent.com/51924622/121318915-52819c00-c929-11eb-9062-cf8e6ce1c795.PNG)<br>

### After training the model is saved by name "flappybrain.h5" shown in this repository.<br>
## Requirements:
- flappy-bird-gym
- numpy
- tensorflow 
### Fork and Run the flappy.py file to see the result.

