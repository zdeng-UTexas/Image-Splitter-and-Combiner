import pandas as pd
import numpy as np
import heapq
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


# Load the CSV file into a DataFrame
# values_csv_path = '/home/zhiyundeng/AEROPlan/experiment/20240302/testing/predicted_cost_of_patch_64.csv'
values_csv_path = '/home/zhiyundeng/AEROPlan/experiment/20240302/testing/smoothed_predicted_cost_of_patch_64.csv'


save_directory = '/home/zhiyundeng/AEROPlan/experiment/20240302/'
filename = 'global_planning_costmap.png'
save_path = save_directory + filename

df = pd.read_csv(values_csv_path, header=None)

# Dynamically determine the grid dimensions based on the CSV data
total_elements = df.size
grid_rows = 57  # Adjust this based on your actual data
grid_columns = total_elements // grid_rows
grid = df.values.reshape((grid_rows, grid_columns))

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def heuristic(a, b):
    # Manhattan distance on a square grid
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(grid, node):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Four directions: right, down, left, up
    result = []
    for direction in directions:
        neighbor = (node[0] + direction[0], node[1] + direction[1])
        if 0 <= neighbor[0] < grid.shape[0] and 0 <= neighbor[1] < grid.shape[1]:
            result.append(neighbor)
    return result

def a_star_search(grid, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in get_neighbors(grid, current):
            new_cost = cost_so_far[current] + grid[next[0]][next[1]]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:  # Traverse backwards from goal to start
        path.append(current)
        current = came_from[current]
    path.append(start)  # Add the start position
    path.reverse()  # Reverse the path to start->goal
    return path

# def visualize_path(grid, path, start, goal):
#     # Create a color map for the grid
#     cmap = mcolors.ListedColormap(['black', 'gray', 'lightgray', 'white', 'red'])
#     bounds = [-0.5, 0.5, 1.5, 2.5, 3.5, 4.5]
#     norm = mcolors.BoundaryNorm(bounds, cmap.N)

#     # Convert the grid to a color map where each value corresponds to a different color
#     grid_vis = np.copy(grid).astype(float)
#     for y in range(grid.shape[0]):
#         for x in range(grid.shape[1]):
#             if (y, x) == start:
#                 grid_vis[y, x] = 4  # Start point color
#             elif (y, x) == goal:
#                 grid_vis[y, x] = 4  # Goal point color
#             elif (y, x) in path:
#                 grid_vis[y, x] = 4  # Path color

#     fig, ax = plt.subplots()
#     ax.imshow(grid_vis, cmap=cmap, norm=norm)

#     # Draw gridlines
#     ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
#     ax.set_xticks(np.arange(-.5, grid.shape[1], 1))
#     ax.set_yticks(np.arange(-.5, grid.shape[0], 1))

#     # Hide the tick labels
#     ax.set_xticklabels([])
#     ax.set_yticklabels([])

#     # Set aspect of the plot to equal to ensure the grid is square-shaped
#     ax.set_aspect('equal')

#     plt.show()

# def visualize_path_with_labels(grid, path, start, goal):
#     # Plot the grid with original colors
#     plt.figure(figsize=(10, 10))
#     plt.imshow(grid, cmap='viridis', origin='upper')  # Use 'viridis' or another colormap that suits your grid values

#     # Extract x and y coordinates from the path
#     x_coords, y_coords = zip(*path)

#     # Overlay the path on the grid
#     plt.plot(y_coords, x_coords, color="red", linewidth=2, marker='o', markersize=5, markerfacecolor="blue", markeredgecolor="blue")

#     # Highlight the start and goal positions
#     plt.plot(start[1], start[0], 'go', markersize=10)  # Start in green
#     plt.plot(goal[1], goal[0], 'ro', markersize=10)  # Goal in red

#     # Setting the ticks to label x and y axes
#     plt.xticks(range(grid.shape[1]), range(grid.shape[1]))
#     plt.yticks(range(grid.shape[0]), range(grid.shape[0]))

#     # Adding gridlines for clarity
#     plt.grid(which='both', color='lightgray', linewidth=0.5)
#     plt.title('Grid with Path from Start to Goal')
#     plt.xlabel('X-axis')
#     plt.ylabel('Y-axis')
    
#     # Show the plot
#     plt.show()


def visualize_path_with_custom_background(grid, path, start, goal):
    # Define a custom colormap for the grid values
    cmap = mcolors.ListedColormap(['black', 'gray', 'lightgray', 'white'])
    bounds = [-0.5, 0.5, 1.5, 2.5, 3.5]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    # Plot the grid with the custom colormap
    plt.figure(figsize=(25, 18))
    plt.imshow(grid, cmap=cmap, norm=norm, origin='upper')

    # Extract x and y coordinates from the path
    x_coords, y_coords = zip(*path)

    # Overlay the path on the grid
    plt.plot(y_coords, x_coords, color="blue", linewidth=4, marker='o', markersize=4, markerfacecolor="blue")

    # Highlight the start and goal positions
    plt.plot(goal[1], goal[0], 'r*', markersize=20)  # Goal in red
    plt.plot(start[1], start[0], 'ro', markersize=10)  # Start in green

    # Setting the ticks to label x and y axes
    plt.xticks(range(grid.shape[1]), range(grid.shape[1]))
    plt.yticks(range(grid.shape[0]), range(grid.shape[0]))

    # Adding gridlines for clarity
    plt.grid(which='both', color='lightgray', linewidth=0.5)
    # plt.title('Grid with Path from Start to Goal')
    plt.xlabel('Y-axis')
    plt.ylabel('X-axis')

    # Show the plot
    plt.show()
    plt.savefig(save_path)
    print('saved')
    plt.close()

# Example usage
start, goal = (13,0), (56,31)  # Adjust these points based on your grid and requirements
came_from, cost_so_far = a_star_search(grid, start, goal)
path = reconstruct_path(came_from, start, goal)

path = reconstruct_path(came_from, start, goal)
# visualize_path(grid, path, start, goal)
# visualize_path_with_labels(grid, path, start, goal)
visualize_path_with_custom_background(grid, path, start, goal)

print("Path from start to goal:", path)
