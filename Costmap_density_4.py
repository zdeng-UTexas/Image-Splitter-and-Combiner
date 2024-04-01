import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_cost_values(csv_path, x, y):
    # Reading the cost values from the CSV file, assuming no header
    df = pd.read_csv(csv_path, header=None)
    cost_values = df[0].values  # Assuming cost values are in the first column
    # Reshaping the cost values into the specified matrix
    return cost_values.reshape((x, y))

def calculate_neighborhood_average(matrix, neighborhood_size=1):
    # Calculate padding size based on neighborhood size (e.g., 1 for 3x3, 2 for 5x5)
    pad_size = neighborhood_size // 2
    padded_matrix = np.pad(matrix, pad_width=pad_size, mode='constant', constant_values=0)
    averaged_matrix = np.zeros(matrix.shape)
    
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Defining the block size based on the neighborhood size
            block = padded_matrix[i:i+neighborhood_size, j:j+neighborhood_size]
            averaged_matrix[i, j] = block.mean()
            
    return averaged_matrix

def create_density_map(matrix, title='Density Map', save_path='density_map_bw.png', colormap='Greys'):
    plt.figure(figsize=(10, 10))
    plt.imshow(matrix, cmap=colormap, interpolation='nearest')
    plt.title(title)
    plt.colorbar(label='Density Value')
    plt.savefig(save_path)  # Saving the figure to the current directory
    plt.show()

def save_averaged_cost_matrix_to_csv(matrix, save_path='averaged_cost_matrix.csv'):
    # Flatten the matrix to a single column
    flattened_matrix = matrix.flatten()
    # Convert the flattened array to a DataFrame
    df = pd.DataFrame(flattened_matrix)
    # Save the DataFrame to a CSV file, maintaining the single-column format
    df.to_csv(save_path, index=False, header=False)

# Example usage
csv_path = '/home/zhiyundeng/AEROPlan/experiment/20240320/testing/predicted_cost_of_patch_32.csv' # Replace with your actual CSV file path
x, y = 44, 57 # Replace with your actual dimensions
neighborhood_size = 3  # For a 24-neighborhood, use 5 (5x5 area)

cost_matrix = read_cost_values(csv_path, x, y)
averaged_cost_matrix = calculate_neighborhood_average(cost_matrix, neighborhood_size=neighborhood_size)
create_density_map(averaged_cost_matrix, save_path='density_map_with_neighborhood.png')
save_averaged_cost_matrix_to_csv(averaged_cost_matrix, save_path='/home/zhiyundeng/AEROPlan/experiment/20240320/testing/smoothed_predicted_cost_of_patch_32.csv')