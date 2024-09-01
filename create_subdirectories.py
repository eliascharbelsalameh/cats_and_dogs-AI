import os
import shutil
import random

# Define the source directory containing the classes "Cat" and "Dog"
source_directory = "dataset/"

# Define the destination directory where the split data will be stored
destination_directory = "split_dataset/"

# Define the ratio for splitting (80% training, 20% testing)
split_ratio = 0.8

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Function to count the number of files in a directory
def count_files(directory):
    return sum(len(files) for _, _, files in os.walk(directory))

# Iterate through each class directory ("Cat" and "Dog") in the source directory
for class_name in os.listdir(source_directory):
    class_directory = os.path.join(source_directory, class_name)
    
    # Create subdirectories for training and testing
    train_directory = os.path.join(destination_directory, "train", class_name)
    test_directory = os.path.join(destination_directory, "test", class_name)
    os.makedirs(train_directory, exist_ok=True)
    os.makedirs(test_directory, exist_ok=True)
    
    # Get a list of image files in the class directory
    image_files = [f for f in os.listdir(class_directory) if os.path.isfile(os.path.join(class_directory, f))]
    
    # Shuffle the list of image files randomly
    random.shuffle(image_files)
    
    # Calculate the number of images for training and testing based on the split ratio
    num_train_images = int(len(image_files) * split_ratio)
    num_test_images = len(image_files) - num_train_images
    
    # Split the image files into training and testing sets
    train_images = image_files[:num_train_images]
    test_images = image_files[num_train_images:]
    
    # Move training images to the training directory
    for image in train_images:
        source_path = os.path.join(class_directory, image)
        destination_path = os.path.join(train_directory, image)
        shutil.copy(source_path, destination_path)
    
    # Move testing images to the testing directory
    for image in test_images:
        source_path = os.path.join(class_directory, image)
        destination_path = os.path.join(test_directory, image)
        shutil.copy(source_path, destination_path)

# Display the length of each directory
print("Number of images in training directory (Cat):", count_files(os.path.join(destination_directory, "train", "Cat")))
print("Number of images in training directory (Dog):", count_files(os.path.join(destination_directory, "train", "Dog")))
print("Number of images in testing directory (Cat):", count_files(os.path.join(destination_directory, "test", "Cat")))
print("Number of images in testing directory (Dog):", count_files(os.path.join(destination_directory, "test", "Dog")))
