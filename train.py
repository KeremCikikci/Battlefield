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
from terrain import *

app = Ursina()  

x_pos, y_pos, z_pos = 17, 12, -14
x_angle, y_angle, z_angle = 30, -30, 0
camera.position = (x_pos, y_pos, z_pos)
camera.rotation = (x_angle, y_angle, z_angle)

window.borderless = False

class ENV(Env):
    def __init__(self):
        self.frame = 0

        # Gym
        self.action_space = Discrete(4) # turn left, turn right, go forward, fire
        # deltaX, deltaY, deltaZ, deltaRotationY, speed
        self.observation_space = Box(np.array([0,0,0,0,0], dtype=int), np.array([10, 10, 10, 360, 1], dtype=int))
        
        # Agent
        self.tank = Tank()
        self.tank.x, self.tank.y, self.tank.z = random.randint(0, 9), 1.5, random.randint(0, 9)
        
        # Target
        vis_target([random.randint(0, 9), 1, random.randint(0, 9)])

        self.delta = self.tank.get_position(relative_to=blocks[0])
        self.state = [self.delta[0], self.delta[1], self.delta[2], self.tank.rotation_y, self.tank.speed]
        # Terrain
        vis_rect_terrain(10, 10)
    
    def step(self, action):
        self.frame += 1
        self.tank.look_at(blocks[0], axis="back")
        # Action
        if action == 0:
            self.tank.turn(1)
        elif action == 1:
            self.tank.turn(-1)
        elif action == 2:
            self.tank.go()
        elif action == 3:
            self.tank.fire()

        if len(blocks) > 0:
            self.delta = self.tank.get_position(relative_to=blocks[0])
            self.state = [self.delta[0], self.delta[1], self.delta[2], self.tank.rotation_y, self.tank.speed]
            
        terminate = False
        if self.frame > 1000:
            terminate = True

        reward = 0
        if len(blocks) == 0:
            print("traiiiiiin")
            self.state = [0, 0, 0, self.tank.rotation_y, self.tank.speed]
            reward = 1
            terminate = True

        if self.tank.x < 0 or self.tank.z > 10:
            reward = -.1
            terminate = True
        if self.tank.z < 0 or self.tank.z > 10:
            reward = -.1
            terminate = True

        app.step()
        return self.state, reward, terminate, {}

    def render(self):
        pass

    def reset(self):
        self.frame = 0

        destroy(self.tank)
        if len(blocks) > 0:
            destroy(blocks[0])

        blocks.clear()

        # Agent
        self.tank = Tank()
        self.tank.x, self.tank.y, self.tank.z = random.randint(0, 9), 1.5, random.randint(0, 9)
        
        # Target
        vis_target([random.randint(0, 9), 1, random.randint(0, 9)])

        self.delta = self.tank.get_position(relative_to=blocks[0])
        self.state = [self.delta[0], self.delta[1], self.delta[2], self.tank.rotation_y, self.tank.speed]

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


train()
app.run()