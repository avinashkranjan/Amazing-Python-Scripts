import gym 

env = gym.make("CartPole-v1", render_mode = "human")



class PID:
    def __init__(self):
        self.kp, self.ki, self.kd, self.last_error, self.E = 1, 1, 100, 0, 0
        self.i_error = 0
    def get_action(self, x):
        error = x
        self.d_error = error - self.last_error
        self.i_error += error 
        self.last_error = error
        return self.kp * error + self.kd * self.d_error + self.ki * self.i_error
    

if __name__ == "__main__":
    sim = PID()
    obs = env.reset()
    state = obs[0]
    done = False
    while not done:
        angle = state[2]
        action = 1 if sim.get_action(angle) > 0 else 0
        state= env.step(action)[0]