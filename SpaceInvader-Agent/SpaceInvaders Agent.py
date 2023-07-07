# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 13:06:20 2021
@author: Ayush
"""

import numpy as np
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy
from rl.memory import SequentialMemory
from rl.agents import DQNAgent
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras.models import Sequential
import gym
env = gym.make("SpaceInvaders-v0")

episodes = 10

for episode in range(1, episodes):
    state = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        state, reward, done, info = env.step(env.action_space.sample())
        score += reward
    print('Episode: {}\nScore: {}'.format(episode, score))
env.close()

# Import Neural Network Packages


def build_model(height, width, channels, actions):
    model = Sequential()
    model.add(Conv2D(32, (8, 8), strides=(4, 4), activation='relu',
              input_shape=(3, height, width, channels)))
    model.add(Conv2D(64, (4, 4), strides=(2, 2), activation='relu'))
    model.add(Conv2D(64, (4, 4), strides=(2, 2), activation='relu'))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(256, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model


height, width, channels = env.observation_space.shape
actions = env.action_space.n

model = build_model(height, width, channels, actions)


# Importing keras-rl2 reinforcement learning functions

def build_agent(model, actions):
    policy = LinearAnnealedPolicy(EpsGreedyQPolicy(
    ), attr='eps', value_max=1., value_min=.1, value_test=.2, nb_steps=10000)
    memory = SequentialMemory(limit=2000, window_length=3)
    dqn = DQNAgent(model=model, memory=memory, policy=policy, enable_dueling_network=True,
                   dueling_type='avg', nb_actions=actions, nb_steps_warmup=1000)
    return dqn


dqn = build_agent(model, actions)


dqn.compile(Adam(lr=0.001))

dqn.fit(env, nb_steps=40000, visualize=True, verbose=1)

scores = dqn.test(env, nb_episodes=10, visualize=True)
print(np.mean(scores.history['episode_reward']))

dqn.save_weights('models/dqn.h5f')
dqn.load_weights('models/dqn.h5f')
