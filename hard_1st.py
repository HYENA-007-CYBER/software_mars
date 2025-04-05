# Function to read the file and store contents as a nested list
def read_obstacle_file(file_path):
    nested_list = []  # Initialize empty list

    with open(file_path, 'r') as file:
        for line in file:
            coordinates = list(map(int, line.strip().split()))  # Convert line to list of integers
            nested_list.append(coordinates)  # Append to nested list

    return nested_list  # Return final nested list

# Example usage
file_path = "sample.txt"  # Update with the actual file location
obstacle_list = read_obstacle_file(file_path)

# Print the nested list
print(obstacle_list)
import numpy as np#USING NUMPY TO CREATE GRID
grid = np.ones((11, 11), dtype=int) # SINCE THE FINAL DESTINATION IS (10,10) A  ARENA GRID OF 11*11 IS CREATED
print(grid)
# FUNCTION TO MAKE ZEROS AT OBSTACLE POSITION
def moves_from_origin(origin, moves):
    x, y = origin
    x -= moves[0]  # NORTH
    y += moves[1]  # EAST
    x += moves[2]  # SOUTH
    y -= moves[3]  # WEST
    return x, y

# SINCE SOME OBSTACLES ARE OUT OF RANGE FROM (0,0) I AM SHIFTING THE ORIGIN
origin = (5, 5)#SHIFTING THE ORIGIN TO CENTER OF THE GRID FOR PLACING EVERY OBSTACLE

# Place obstacles on the grid AS ZEROS
for moves in obstacle_list:
    x, y = moves_from_origin(origin, moves)
    grid[x][y] = 0

# Print updated grid
print(grid)
from collections import deque

# DIRECTIONS FOR MOVEMENT
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  #MOVEMENT IN FOUR DIRECTIONS RESPECTIVELY

# BFS FUNCTION
def bfs(grid, start, end):
    n = len(grid)
    visited = set()#TO STORE THE VISTED LOCATIONS
    queue = deque()# HOLD LOCATIONS TO EXPLORE NEXT AND THE PATH TAKEN SO FAR
    queue.append((start, [start]))#ADDING STARTING POSITION
    visited.add(start)#ADIING START TO VISTED LIST

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path  # Return the shortest path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy#TRYING TO MOVE IN ALL FOUR DIRECTIONS

            # CHECK IF THE POSITION DOESNOT CONTAIN OBSTACLE AND DOESNOT EXCEED GRID
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    

# Start and end points
start = (0, 0)
end = (10, 10)

# DO BFS ONLY IF  START AND END ARE NOT OBSTACLES
if grid[start[0]][start[1]] == 1 and grid[end[0]][end[1]] == 1:
    path = bfs(grid, start, end)
    print("Shortest path:")
    print(path)

