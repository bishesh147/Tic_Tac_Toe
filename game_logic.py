def determine_winner(game): # Returning [a, b] a = 1 means x wins, b is the type of win
    if game[0][0] == "X":
        if game[0][1] == "X" and game[0][2] == "X":
            return [1, 1]
        if game[1][0] == "X" and game[2][0] == "X":
            return [1, 2]
        if game[1][1] == "X" and game[2][2] == "X":
            return [1, 3]
    elif game[0][1] == "X" and game[1][1] == "X" and game[2][1] == "X":
        return [1, 4]
    elif game[0][2] == "X" and game[1][2] == "X" and game[2][2] == "X":
        return [1, 5]
    elif game[1][0] == "X" and game[1][1] == "X" and game[1][2] == "X":
        return [1, 6]
    elif game[2][0] == "X" and game[2][1] == "X" and game[2][2] == "X":
        return [1, 7]
    
    if game[0][0] == "O":
        if game[0][1] == "O" and game[0][2] == "O":
            return [2, 1]
        if game[1][0] == "O" and game[2][0] == "O":
            return [2, 2]
        if game[1][1] == "O" and game[2][2] == "O":
            return [2, 3]
    elif game[0][1] == "O" and game[1][1] == "O" and game[2][1] == "O":
        return [2, 4]
    elif game[0][2] == "O" and game[1][2] == "O" and game[2][2] == "O":
        return [2, 5]
    elif game[1][0] == "O" and game[1][1] == "O" and game[1][2] == "O":
        return [2, 6]
    elif game[2][0] == "O" and game[2][1] == "O" and game[2][2] == "O":
        return [2, 7]
    
    for i in range(3):
        for j in range(3):
            if game[i][j] == ".":
                return [3, 8]
    
    return [0, 0]
    