import numpy as np
from copy import deepcopy
from Q_Learning_Tic_Tac_Toe import FeatureExtractor, Board

featExt = FeatureExtractor()
board = Board()

# Test: zero matrix
board.grid.fill(0)
res = featExt.densityFeature(board,1,0)
# Works

board.grid = ([["O", "O", "X"],
               ["O", "X", "O"],
               ["O", "X", "O"]])
assert(featExt.densityFeature(board,1,1)==3*1/8)
assert(featExt.densityFeature(board,2,1)==2/8+1/16)
assert(featExt.densityFeature(board,2,2)==2/8+1/16)
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
board.grid = ([["O", "X", "X"],
               ["X", np.nan, "O"],
               [np.nan, "X", "O"]])
paths_data = np.array(board.grid)
linear, nonlinear, interaction, blocking = featExt.calcNotDensityFeats(board,paths_data,
                                                                       1,1,True,False,"X")
### Why is the interaction score zero?
print("Done")

