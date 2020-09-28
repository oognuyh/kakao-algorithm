RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, -1)
DOWN = (0, 1)

def solution(board) -> int:
    return navigate(board)

def navigate(board) -> int:
    q, visited = [[[0, 0], [1, 0]]], [[[0, 0], [1, 0]]]
    count = 0
    
    while q:
        print(q)
        for _ in range(len(q)):
            robot = q.pop(0)
            if is_end(board, robot): return count 

            for direction in [RIGHT, LEFT, UP, DOWN]:
                if is_valid(board, robot, direction):
                    to = [add(coord, direction) for coord in robot]
                    if not to in visited:
                        visited.append(to)
                        q.append(to)

            # rotate
            if is_vertical(robot): # |
                if is_valid(board, robot, RIGHT):
                    to = sorted([robot[0], add(robot[1], add(RIGHT, UP))])
                    if not to in visited:
                        visited.append(to); q.append(to)

                    to = sorted([add(robot[0], add(RIGHT, DOWN)), robot[1]])
                    if not to in visited:
                        visited.append(to); q.append(to)

                if is_valid(board, robot, LEFT):
                    to = sorted([robot[0], add(robot[1], add(LEFT, UP))])
                    if not to in visited:
                        visited.append(to); q.append(to)
                        
                    to = sorted([add(robot[0], add(LEFT, DOWN)), robot[1]])
                    if not to in visited:
                        visited.append(to); q.append(to)
            else: # --
                if is_valid(board, robot, UP):
                    to = sorted([robot[0], add(robot[1], add(LEFT, UP))])
                    if not to in visited:
                        visited.append(to); q.append(to)
                        
                    to = sorted([add(robot[0], add(RIGHT, UP)), robot[1]])
                    if not to in visited:
                        visited.append(to); q.append(to)

                if is_valid(board, robot, DOWN):
                    to = sorted([robot[0], add(robot[1], add(LEFT, DOWN))])
                    if not to in visited:
                        visited.append(to); q.append(to)
                        
                    to = sorted([add(robot[0], add(RIGHT, DOWN)), robot[1]])
                    if not to in visited:
                        visited.append(to); q.append(to)
        
        count += 1

def add(coord, to) -> list:
    return [coord[0] + to[0], coord[1] + to[1]]

def is_valid(board, robot, to) -> bool: # coord is in range and not wall
    for coord in robot:
        x, y = add(coord, to)
        if -1 < x and x < len(board) and -1 < y and y < len(board):
            if board[y][x] == 0:
                continue
        return False
    return True

def is_end(board, robot) -> bool: # coord is goal
    return True if [len(board) - 1, len(board) - 1] in robot else False
    
def is_vertical(robot) -> bool: 
    x1, x2 = robot[0][0], robot[1][0]
    return True if x1 == x2 else False
