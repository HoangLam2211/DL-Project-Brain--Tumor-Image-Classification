# import streamlit as st
# import tensorflow as tf
# import matplotlib.pyplot as plt
# import numpy as np
# from tensorflow.keras.models import load_model
# from tensorflow.keras.utils import to_categorical
# import os

# # Define model paths
# model_paths = {
#     "VGG19 Model 01": 'model\\vgg19_model_01.keras',
#     "VGG19 Model 02": 'model\\vgg19_model_02.keras',
#     "VGG19 Model 03": 'model\\vgg19_model_03.keras',
#     "CNN Model": 'model\\vgg19_model_cnn.keras',
#     "ResNet Model": 'model\\vgg19_model_resnet.keras'
# }

# # Check if model files exist
# for name, path in model_paths.items():
#     if not os.path.exists(path):
#         print(f"Model file not found: {path}")

# # Load models and evaluate performance
# def evaluate_models(models, test_data, test_labels):
#     results = {}
#     for name, path in models.items():
#         try:
#             model = load_model(path)
#             loss, accuracy = model.evaluate(test_data, test_labels, verbose=0)
#             results[name] = {"accuracy": accuracy, "loss": loss}
#         except Exception as e:
#             st.error(f"Error loading model '{name}' from path '{path}': {e}")
#             results[name] = {"accuracy": None, "loss": None}  # Handle loading errors
#     return results

# # Generate random test data (replace with actual test set)
# def generate_test_data():
#     test_data = np.random.rand(100, 240, 240, 3)  # Simulate test data
#     test_labels = np.random.randint(2, size=(100,))
#     test_labels = to_categorical(test_labels, num_classes=2)  # Convert to one-hot encoded
#     return test_data, test_labels

# # Display results as a bar chart
# def plot_results(results, metric="accuracy"):
#     fig, ax = plt.subplots()
#     models = list(results.keys())
#     values = [results[model][metric] for model in models]
#     ax.bar(models, values, color=['skyblue', 'salmon', 'orange', 'green', 'purple'])
#     ax.set_xlabel("Models")
#     ax.set_ylabel(metric.capitalize())
#     ax.set_title(f"{metric.capitalize()} Comparison Across Models")
#     return fig

# # Main Streamlit app wrapped in a function
# def show():
#     st.title("So sánh hiệu suất các mô hình")

#     # Generate or load test data
#     test_data, test_labels = generate_test_data()

#     # Evaluate each model and collect results
#     st.write("Đang đánh giá các mô hình trên tập dữ liệu kiểm tra...")
#     results = evaluate_models(model_paths, test_data, test_labels)

#     # Display results in a table
#     st.write("### Kết quả hiệu suất:")
#     st.write("Dưới đây là bảng kết quả về độ chính xác và mất mát của từng mô hình:")
#     st.table({model: [metrics['accuracy'], metrics['loss']] for model, metrics in results.items()})

#     # Choose metric to plot
#     metric = st.radio("Chọn một chỉ số để hiển thị biểu đồ:", ["accuracy", "loss"])

#     # Plot the selected metric for comparison
#     fig = plot_results(results, metric)
#     st.pyplot(fig)


import streamlit as st
import pandas as pd
import os
from PIL import Image

# Load model evaluation data from CSV
def load_model_data(csv_path):
    if os.path.exists(csv_path):
        return pd.read_csv(csv_path)
    else:
        st.error(f"CSV file not found: {csv_path}")
        return None

# Load and show image
def load_and_show_image(image_path):
    # Check if the image file exists
    if os.path.exists(image_path):
        # Read the image
        image = Image.open(image_path)
        # Display the image
        st.image(image, caption='Biểu đồ so sánh hiệu suất các mô hình', use_column_width=True)


# Main Streamlit app wrapped in a function
def show():
    st.title("So sánh hiệu suất các mô hình")

    # Load model evaluation data from CSV
    csv_path = 'model\model.csv'  # Specify the correct path to your CSV file
    results = load_model_data(csv_path)

    if results is not None:
        # Display results in a table
        st.write("### Kết quả hiệu suất:")
        st.write("Dưới đây là bảng kết quả về độ chính xác và mất mát của từng mô hình:")
        st.table(results)

        # Create buttons for selecting metrics
        if st.button("Hiển thị Accuracy"):
            # Load and display the accuracy comparison images
            accuracy_image_1 = 'performance\\accuracies.png'  # Path to the first accuracy comparison image
            accuracy_image_2 = 'performance\\cnn_resnet.png'  # Path to the second accuracy comparison image
            
            load_and_show_image(accuracy_image_1)
            load_and_show_image(accuracy_image_2)

        if st.button("Hiển thị Loss"):
            # Load and display the loss comparison image
            loss_image = 'performance\\loss.png'  # Path to the loss comparison image
            
            load_and_show_image(loss_image)

# Run the application
if __name__ == "__main__":
    show()

