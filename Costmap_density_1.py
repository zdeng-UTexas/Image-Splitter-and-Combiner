import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_cost_values(csv_path, x, y):
    # Reading the cost values from the CSV file
    df = pd.read_csv(csv_path, header=None)
    cost_values = df[0].values
    # Reshaping the cost values into the specified matrix
    return cost_values.reshape((x, y))

def calculate_neighborhood_average(matrix):
    # Padding the original matrix to handle the edges
    padded_matrix = np.pad(matrix, pad_width=1, mode='constant', constant_values=0)
    averaged_matrix = np.zeros(matrix.shape)
    
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Extracting the 3x3 block surrounding the current cell including itself
            block = padded_matrix[i:i+3, j:j+3]
            # Calculating the average and assigning it to the corresponding cell
            averaged_matrix[i, j] = block.mean()
            
    return averaged_matrix

def create_density_map(matrix, title='Density Map', save_path='density_map.png'):
    plt.figure(figsize=(5, 5))
    # Displaying the matrix as a density map
    plt.imshow(matrix, cmap='viridis', interpolation='nearest')
    plt.title(title)
    plt.colorbar(label='Density Value')
    plt.savefig(save_path)

# Example usage
csv_path = '/home/zhiyundeng/AEROPlan/experiment/20240302/testing/predicted_cost_of_patch_64.csv' # Replace with your actual CSV file path
x, y = 57, 85 # Replace with your actual dimensions

cost_matrix = read_cost_values(csv_path, x, y)
averaged_cost_matrix = calculate_neighborhood_average(cost_matrix)
create_density_map(averaged_cost_matrix, save_path='density_map.png')