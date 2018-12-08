import numpy as np
from copy import deepcopy
from Q_Learning_Tic_Tac_Toe import Board
from FeatureExtractor import import FeatureExtractor

featExt = FeatureExtractor()
board = Board()

# Test: zero matrix
board.grid.fill(0)
'''
#res = featExt.densityFeature(board,1,0,board.board_size)
# Works

board.grid = ([["O", "O", "X"],
               ["O", "X", "O"],
               ["O", "X", "O"]])
#assert(featExt.densityFeature(board,1,1)==3*1/8)
#assert(featExt.densityFeature(board,2,1)==2/8+1/16)
#assert(featExt.densityFeature(board,2,2)==2/8+1/16)
# Works :)


# Test non-density features
board.grid = ([["O", np.nan, "X"],
               ["O", np.nan, "O"],
               ["O", "X", "O"]])
paths_data = np.array(board.grid)
#linear, nonlinear, interaction, blocking = featExt.calcNotDensityFeats(board,paths_data,1,1,False,True,"O")

board.grid = ([["O", np.nan, "X"],
               ["O", np.nan, "O"],
               [np.nan, "X", "O"]])
paths_data = np.array(board.grid)
#linear, nonlinear, interaction, blocking = featExt.calcNotDensityFeats(board,paths_data, 1,1,False,True,"O")


#Test interaction
board.grid = ([["O", np.nan, "X"],
               ["O", np.nan, "O"],
               [np.nan, "X", "O"]])
paths_data = np.array(board.grid)
#linear, nonlinear, interaction, blocking = featExt.calcNotDensityFeats(board,paths_data, 1,1,False,True,"O")

#Test blocking
board.grid = ([["O", np.nan, np.nan],
               ["X", np.nan, "O"],
               [np.nan, "X", "O"]])
#paths_data = np.array(board.grid)
#linear, nonlinear, interaction, blocking = featExt.calcNotDensityFeats(board,paths_data,
#                                                                       2,0,x_turn=True,o_turn=False,player="X")

#res = featExt.extractFeatures(board,player="X")
'''

board = Board(board_size=5)

# Test: zero matrix
board.grid = ([[1, 0, 0, 0, 1],
               [1, 1, 1, 0 ,1],
               [0, 0, 1, 1, 0],
               [1, 1, 0, 0, 0],
               [0, 0, 1, 1, 0]])
rows,cols,diag,cross_diag = board.get_rows_cols_streaks()
print(rows)
print(cols)
print(diag)
print(cross_diag)

print("Done")

