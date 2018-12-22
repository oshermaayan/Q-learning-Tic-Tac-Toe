import numpy as np
import tkinter as tk
import copy
import pickle
from Q_Learning_Tic_Tac_Toe import Game, QPlayer, RandomPlayer     # Classes used for Tic Tac Toe

root = tk.Tk()
epsilon = 0.9
player1 = QPlayer(mark="X",epsilon = epsilon)### add parameters!
player2 = RandomPlayer(mark="O")
game = Game(root, player1, player2)#,board_size=5,streak_size=4)

N_episodes = 100
for episodes in range(N_episodes):
    game.play()
    game.reset()

Q = game.Q

filename = "Q_epsilon_09_Nepisodes_{}.p".format(N_episodes)
pickle.dump(Q, open(filename, "wb"))
