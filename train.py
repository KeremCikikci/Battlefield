"""
Burada ilk etapta düsman olarak belirledigi nesnelere ates eden bir tank egitilecek
"""

from attr import asdict
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

import random
import os


from gym import Env
from gym.spaces import Discrete, Box

import numpy as np
import random

import pygame
import math

from ursina import *
from npc import Tank
from terrain import vis_rect_terrain, vis_target, blocks

WIDTH, HEIGHT = 100, 100
FPS = 10
# Initialize rendering requirements
pygame.init()
pygame.display.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Test")
clock = pygame.time.Clock()

app = Ursina()
class target:
    def __init__(self):
        self.pos = [random.randint(0, 9), 1, random.randint(0, 9)]

class ENV(Env):
    def __init__(self):
        self.frame = 0

        # Gym
        self.action_space = Discrete(4) # turn left, turn right, go forward, fire
        # deltaX, deltaY, deltaZ, rotation, speed
        self.observation_space = Box(np.array([0,0,0,0,0], dtype=int), np.array([10, 10, 10, 360, 5], dtype=int))
        
        # Agent
        self.tank = Tank()
        self.tank.x, self.tank.y, self.tank.z = random.randint(0, 9), 1, random.randint(0, 9)
        
        # Target
        target = target()
        vis_target((target.x, target.y, target.z))

        self.delta = [blocks[0].pos[0] - self.tank.x, blocks[1].pos[1] - self.tank.y, blocks[2].pos[2] - self.tank.z]

        self.state = [self.delta[0], self.delta[1], self.delta[2], self.tank.rotation_y, target.speed]

        # Terrain
        vis_rect_terrain(10, 10)
    
    def step(self, action):
        self.frame += 1

        # Action
        if action == 0:
            self.tank.turn(1)
        elif action == 1:
            self.tank.turn(-1)
        elif action == 2:
            self.tank.go()
        elif action == 3:
            self.tank.fire()

        self.tank.update()

        terminate = False
        if self.frame > 1000:
            terminate = True

        reward = 0
        if len(blocks) == 0:
            reward = 1
            terminate = True
        
        return self.state, reward, terminate, {}

    def render(self):
        pass

    def reset(self):
        
        return self.state


env = ENV()

def check():
    episodes = 50
    for episode in range(1, episodes+1):
        state = env.reset()
        done = False
        score = 0 
        
        while not done:
            action = env.action_space.sample()
            n_state, reward, done, info = env.step(action)
            score+=reward
            env.render()
        print('Episode:{} Score:{}'.format(episode, score))
    #env.close()

def train():
    #log_path = os.path.join('Training', 'Logs')
    model = PPO("MlpPolicy", env, verbose=1)#, tensorboard_log=log_path)
    model.learn(total_timesteps=50000)
    model.save('PPO-100000')

def test():
    log_path = os.path.join('Saved Models', 'PPO-100000.zip')
    model = PPO.load(log_path, env)
    evaluate_policy(model, env, n_eval_episodes=10, render=True)

def use():
    obs = env.reset()
    log_path = os.path.join('PPO-100000.zip')
    model = PPO.load(log_path, env)
    model2 = PPO.load(log_path, env)
    for i in range(1000):
        action, _states = model.predict(obs)
        action2, _states2 = model2.predict(obs)
        obs, rewards, dones, info = env.step(action, action2)
        

        env.render()

app.run()