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
import numpy as np
grid = np.ones((11, 11), dtype=int)
print(grid)


