EMPTY = -1
COLUMN = 0
BEAM = 1
DELETE = 0
BUILD = 1

def solution(n, build_frame):
    columns, beams = make_frame(n), make_frame(n)
    
    for command in build_frame:
        print(command)
        do(command, columns, beams)
        if not is_possible_to_do(columns, beams): rollback(command, columns, beams)
    
    return merge(columns, beams)

def do(command, columns, beams):
    x, y, a, b = command

    if a == COLUMN:
        columns[y][x] = EMPTY if b == DELETE else COLUMN
    elif a == BEAM:
        beams[y][x] = EMPTY if b == DELETE else BEAM    

def make_frame(n):
    return [[EMPTY for _ in range(n + 1)] for _ in range(n + 1)]

def merge(columns, beams):
    # 기둥과 보 프레임을 합치고 정렬 후 반환
    merged = []

    for y in range(len(beams)):
        for x in range(len(beams)):
            if columns[y][x] == COLUMN: merged.append([x, y, COLUMN])
            if beams[y][x] == BEAM: merged.append([x, y, BEAM])

    return sorted(merged)

def is_possible_to_do(columns, beams):
    for y in range(len(beams)):
        for x in range(len(beams)):
            if beams[y][x] == BEAM:
                if not is_valid_beam(x, y, columns, beams): return False
            if columns[y][x] == COLUMN:
                if not is_valid_column(x, y, columns, beams): return False
    return True

def is_valid_beam(x, y, columns, beams):
    # 보의 끝이 기둥 위에 위치 또는 양쪽이 다른 보로 연결된 경우 가능
    if x == 0: # 왼쪽
        if columns[y - 1][x] == COLUMN or columns[y - 1][x + 1] == COLUMN:
            return True
    elif x == len(beams) - 1: # 오른쪽
        return False
    else:
        if columns[y - 1][x] == COLUMN or columns[y - 1][x + 1] == COLUMN:
            return True
        elif beams[y][x - 1] == BEAM and beams[y][x + 1] == BEAM:
            return True
    return False

def is_valid_column(x, y, columns, beams):
    # 다른 기둥 위에 위치 또는 보 위에 위치한 경우 가능
    if y == 0: return True # 바닥에 설치된 경우
    else:
        if x == 0:
            if columns[y - 1][x] == COLUMN or beams[y][x] == BEAM:
                return True
        elif x == len(beams) - 1:
            if columns[y - 1][x] == COLUMN or beams[y][x - 1] == BEAM:
                return True
        else:
            if columns[y - 1][x] == COLUMN or beams[y][x - 1] == BEAM or beams[y][x] == BEAM:
                return True
    return False

def rollback(command, columns, beams):
    x, y, a, b = command

    if a == COLUMN:
        columns[y][x] = COLUMN if b == DELETE else EMPTY 
    elif a == BEAM:
        beams[y][x] = BEAM if b == DELETE else EMPTY

# build_frame의 가로가 4인데 지어지는 공간의 가로가 4로 착각하여 오래걸림

if __name__ == "__main__":
    print('- ' * 30)
    print('\n'.join(map(str, solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))))
    print('- ' * 30)
    
    print('\n'.join(map(str, solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))))
    print('- ' * 30)