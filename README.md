# Cats and Dogs Classification using Convolutional Neural Networks

## Project Overview
This project focuses on the binary classification of images into two categories: cats and dogs. The model is built using Convolutional Neural Networks (CNNs) and is implemented using TensorFlow and Keras. The project demonstrates data preprocessing, model training, evaluation, and visualization of the results.

## Table of Contents
- [Project Overview](#project-overview)
- [Data Preprocessing](#data-preprocessing)
- [Model Architecture](#model-architecture)
- [Training and Evaluation](#training-and-evaluation)
- [Results Visualization](#results-visualization)
- [Using the Best Model](#using-the-best-model)

## Data Preprocessing
The dataset is split into training and testing subsets and preprocessed using `ImageDataGenerator`:
- **Training Data Augmentation**: Includes rescaling, rotation, width/height shift, shearing, zooming, and horizontal flipping.
- **Testing Data**: Only rescaled for normalization.

Data generators are used to load and preprocess images on-the-fly.

## Model Architecture
The CNN model consists of several layers:
1. **Convolutional Layers**: Four convolutional layers with increasing filters (32, 64, 128, 256), each followed by a max-pooling layer.
2. **Flatten Layer**: Converts the 2D output of the last convolutional layer into a 1D feature vector.
3. **Dense Layers**: Two dense layers, with the final layer having 2 neurons for binary classification (using softmax activation).

### Model Compilation
- **Optimizer**: Adam
- **Loss Function**: Categorical Crossentropy
- **Metrics**: Accuracy

## Training and Evaluation
The model is trained using the augmented training data with early stopping, model checkpointing, and learning rate scheduling as callbacks.

### Callbacks:
- **Early Stopping**: Monitors accuracy to prevent overfitting.
- **Model Checkpoint**: Saves the best model during training.
- **Learning Rate Scheduler**: Adjusts learning rate periodically.

The model's performance is evaluated on the test data after training.

## Results Visualization
Training and validation loss/accuracy curves are plotted to visualize the model's performance over epochs. Additionally, a function `display_images_with_labels` is used to visualize predictions on a set of images, displaying true and predicted labels.

## Using the Best Model
After training, the best model is saved and can be loaded for further evaluation or predictions:
- **Loading and Evaluating**: The best model is loaded and evaluated on the test set.
- **Visualizing Results**: The same visualization function is applied to a new validation set to inspect the model's predictions.

## How to Run the Project
1. **Install Dependencies**: Ensure you have TensorFlow and Keras installed.
2. **Prepare Dataset**: Ensure your dataset is structured correctly in the `split_dataset/` and `outer_dataset/` directories.
3. **Run the Script**: Execute the provided Python script to train the model, visualize results, and evaluate the best model.
4. **Inspect Results**: Check the console output for accuracy and loss metrics, and view the plotted figures for training and validation performance.

## Conclusion
The model effectively classifies cats and dogs with a high degree of accuracy. This project serves as a foundation for further experimentation with more complex architectures or different datasets.
