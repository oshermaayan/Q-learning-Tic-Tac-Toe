def compute_open_paths_data_interaction_new(row, col, board, exp=1, player='X', player_turn=True, interaction=True):
    other_player = 'O'
    if player == 'O':
        other_player = 'X'

    max_length_path = 0
    threshold = 0
    # if len(board)==10:
    #     threshold +=1

    streak_size = 4  # how many Xs in a row you need to win
    if len(board) == 10:  # if it's a 10X10 board you need 5.
        streak_size = 5

    open_paths_data = []  # this list will hold information on all the potential paths, each path will be represented by a pair (length and empty squares, which will be used to check overlap)
    paths = []
    # check right-down diagonal (there is a more efficient way to look at all the paths, but it was easier for me to debug when separating them :)
    for i in range(streak_size):
        r = row - i
        c = col - i
        if (r > len(board)-1) | (r < 0) | (c > len(board)-1) | (c < 0):
            continue
        blocked = False
        path_length = 0
        path_x_count = 0
        empty_squares = []
        path = []
        square_row = r
        square_col = c
        while (not blocked) & (path_length < streak_size) & (square_row < len(board)) & (square_row >= 0) & (square_col < len(board)) & (square_col >= 0):
            if board[square_row][square_col] == other_player:
                blocked = True
            elif board[square_row][square_col] == player:
                path_x_count += 1
            elif ((square_col != col) | (square_row != row)):
				# Square is empty, add it to empty_squares only only if it's NOT the current square in play
                empty_squares.append([square_row,square_col])
            path.append([square_row,square_col])
            square_row += 1
            square_col += 1
            path_length += 1

        if (path_length == streak_size) & (not blocked) & ((path_x_count>threshold) | ((player_turn) & (path_x_count+1)>threshold)):
            # If a path is blocked by the opponent, we disregard it
			# add the path if it's not blocked and if there is already at least one X on it
            if player_turn:
				# The player draw X in the current square, therefore the path has 1 more X in it
                open_paths_data.append((path_x_count+1, empty_squares, path))
                if (path_x_count+1) > max_length_path:
					# update longest path of Xs
                    max_length_path = path_x_count+1
            elif path_x_count > threshold:
				# Opponent's turn - places an O in the current square.
				# ## Question: why isn't this case symmetrical to the one with Xs? why do we use path_x_count
				# ##			and not path_current_player_count ?
                open_paths_data.append((path_x_count,empty_squares, path))

    # check left-down diagonal
    for i in range(streak_size):
        r = row - i
        c = col + i
        if (r > len(board)-1) | (r < 0) | (c > len(board)-1) | (c < 0):
            continue
        blocked = False
        path_length = 0
        path_x_count = 0
        empty_squares = []
        path = []
        square_row = r
        square_col = c
        while (not blocked) & (path_length < streak_size) & (square_row < len(board)) & (square_row >= 0) & (square_col < len(board)) & (square_col >= 0):
            if board[square_row][square_col] == other_player:
                blocked = True
            elif board[square_row][square_col] == player:
                path_x_count += 1
            elif ((square_col != col) | (square_row != row)):
                empty_squares.append([square_row,square_col])
            path.append([square_row,square_col])
            square_row += 1
            square_col -= 1
            path_length += 1

        if (path_length == streak_size) & (not blocked) & ((path_x_count>threshold) | ((player_turn) & path_x_count+1>threshold)): # add the path if it's not blocked and if there is already at least one X on it
            if player_turn:
                open_paths_data.append((path_x_count+1,empty_squares, path))
                if (path_x_count+1) > max_length_path:
                    max_length_path = path_x_count+1
            elif (path_x_count>threshold):
                open_paths_data.append((path_x_count,empty_squares, path))

    # check vertical
    for i in range(streak_size):
        r = row - i
        c = col
        if (r > len(board)-1) | (r < 0) | (c > len(board)-1) | (c < 0):
            continue
        blocked = False
        path_length = 0
        path_x_count = 0
        empty_squares = []
        path = []
        square_row = r
        square_col = c
        while (not blocked) & (path_length < streak_size) & (square_row < len(board)) & (square_row >= 0) & (square_col < len(board)) & (square_col >= 0):
            if board[square_row][square_col] == other_player:
                blocked = True
            elif board[square_row][square_col] == player:
                path_x_count += 1
            elif ((square_col != col) | (square_row != row)):
                empty_squares.append([square_row,square_col])

            path.append([square_row,square_col])
            square_row += 1
            path_length += 1



        if (path_length == streak_size) & (not blocked) & ((path_x_count>threshold) | ((player_turn) & path_x_count+1>threshold)): # add the path if it's not blocked and if there is already at least one X on it
            if player_turn:
                open_paths_data.append((path_x_count+1,empty_squares, path))
                if (path_x_count+1) > max_length_path:
                    max_length_path = path_x_count+1
            elif (path_x_count>threshold):
                open_paths_data.append((path_x_count,empty_squares, path))

    # check horizontal
    for i in range(streak_size):
        r = row
        c = col - i
        if (r > len(board)-1) | (r < 0) | (c > len(board)-1) | (c < 0):
            continue
        blocked = False
        path_length = 0
        path_x_count = 0
        empty_squares = []
        path = []
        square_row = r
        square_col = c
        while (not blocked) & (path_length < streak_size) & (square_row < len(board)) & (square_row >= 0) & (square_col < len(board)) & (square_col >= 0):
            if board[square_row][square_col] == other_player:
                blocked = True
            elif board[square_row][square_col] == player:
                path_x_count += 1
            elif ((square_col != col) | (square_row != row)):
                empty_squares.append([square_row, square_col])

            path.append([square_row, square_col])
            square_col += 1
            path_length += 1

        if (path_length == streak_size) & (not blocked) & ((path_x_count>threshold) | ((player_turn) & path_x_count+1>threshold)):  # add the path if it's not blocked and if there is already at least one X on it
            if player_turn:
                open_paths_data.append((path_x_count+1,empty_squares, path))
                if (path_x_count+1) > max_length_path:
                    max_length_path = path_x_count+1
            elif (path_x_count>threshold):
                open_paths_data.append((path_x_count,empty_squares, path))


    score = 0.0
    # compute the score for the cell based on the potential paths
    for i in range(len(open_paths_data)):
        p1 = open_paths_data[i]

        if streak_size == p1[0]:
            score = WIN_SCORE
        else:
			if lineaer:
				score += p1[0]
			else:
				score += 1.0/math.pow((streak_size-p1[0]), exp)  # score for individual path
        if interaction:
            for j in range(i+1, len(open_paths_data)):
                p2 = open_paths_data[j]
                if check_path_overlap(p2[2],p1[2]): #pi[2] = an array describing the open path
                    if (not(check_path_overlap(p1[1],p2[1]))):  # interaction score if the paths don't overlap
						# pi[1] = array of empty positions in paths
						# Questions: What is the meaning of the inner if statement?
						# where do we check that the interacting paths (but that cannot be
						# blocked simultaneously by a single ‘O’ move)
						# ok!
                        top = 0.0 +p1[0]*p2[0]
                        bottom = ((streak_size-1)*(streak_size-1))-(p1[0]*p2[0]) ### This isn't the exact same formula from the paper
                        if bottom == 0:
                            score = WIN_SCORE
                        else:
                            score += math.pow(top/bottom, exp)

    return (score, open_paths_data, max_length_path)


'''
checks if the two paths can be blocked by a shared cell
'''
def check_path_overlap(empty1, empty2):
    for square in empty1:
        if square in empty2:
            return True
    return False

'''
	Ideas:
		1. For each square:
			2. For each of its surroundings (in streak size)
				3. "create" an array of the current surroundings
				4. Count the number of Xs, 0s and Nans if #Os >0 - the way is blocked
				5. used similar calcuations as the ones in the code above
		2. Weight X's score and O's score (something similar happens in Ofra's code)
	
	Questions:
		1. Linear feature - ask for details about "The square receives an additional
												score for blocking potential opponent winning paths (similar
												computation for path score, but not counting the currently
												examined square as it is not the opponent’s turn)."
		2. Where is the Blocking score calculated?
			Blocking: This scoring is similar to interaction, but includes
			an additional component: if placing an ‘X’ in the square
			results in an immediate threat (a path that contains n−1 X
			markers), the score of the square is augmented by a large
			constant (10 points) since by forcing ‘O’ to a particular
			move, ‘X’ essentially blocked all other paths for ‘O’.
			
			An idea for implentation:
				1. look for open paths with length==streak_size-2 (then, if we play X, length = streak_size-1 
					and an immediate threat is created)
				2. 
		
		3. How about "penalties", e.g. when we place an X in a square that forces the opponent to block more than 1 path?
	
	
	
	compute_paths_score_for_matrix
	
	add matrices for tests (e.g. calc features)
'''