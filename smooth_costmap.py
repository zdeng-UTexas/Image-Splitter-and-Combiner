import cv2
import numpy as np

def apply_gaussian_blur(image, kernel_size=(5, 5)):
    """Applies Gaussian Blur to an image."""
    return cv2.GaussianBlur(image, kernel_size, 0)

def smooth_transitions(costmap_path, kernel_size=(5, 5)):
    # Load the image
    costmap = cv2.imread(costmap_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply Gaussian blur to the entire image
    blurred_costmap = apply_gaussian_blur(costmap, kernel_size)
    
    # Find the contours of the regions in the costmap
    contours, _ = cv2.findContours(costmap, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Create an empty mask to draw the contours
    mask = np.zeros_like(costmap)
    
    # Draw the contours on the mask with thickness = -1, which fills the contour
    cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)
    
    # Erode the mask to shrink the regions slightly
    kernel = np.ones((3,3), np.uint8)
    eroded_mask = cv2.erode(mask, kernel, iterations=5)
    
    # Where mask is not eroded, keep the original regions, else use the blurred image
    smoothed_costmap = np.where(eroded_mask == 255, costmap, blurred_costmap)
    
    # Save the smoothed costmap
    smoothed_costmap_path = '/home/dengzy/AEROPlan_Dataset/Costmap/Combined_Images/Smoothed_Combined_Costmap_256.jpg'
    cv2.imwrite(smoothed_costmap_path, smoothed_costmap)
    
    return smoothed_costmap_path

# Use the function on the uploaded costmap image
smoothed_costmap_path = smooth_transitions('/home/dengzy/AEROPlan_Dataset/Costmap/Combined_Images/Combined_Costmap_256.jpg')
print(smoothed_costmap_path)
