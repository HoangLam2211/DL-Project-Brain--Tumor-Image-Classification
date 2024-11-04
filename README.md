
---

# Brain Tumor Classification using VGG19, CNN, and ResNet

This project leverages advanced deep learning models, including VGG19, Convolutional Neural Networks (CNN), and ResNet, to classify brain tumor images from a curated dataset. The application is built using Streamlit, providing an intuitive user interface for uploading images and receiving predictions about the presence of a tumor. Additionally, a chatbot feature is integrated to enhance user interaction and provide information related to brain tumors and health.

## Project Overview

- **Models**:
  - **VGG19**: Known for its deep architecture and effectiveness in image classification tasks, fine-tuned specifically for the detection of brain tumors in medical images.
  - **CNN**: A custom convolutional neural network tailored for image processing, enabling effective feature extraction and classification.
  - **ResNet**: Utilizing residual learning to facilitate the training of very deep networks, ResNet enhances classification accuracy while mitigating the vanishing gradient problem.

- **Libraries**: The application is developed using:
  - **TensorFlow**: For implementing the models (VGG19, CNN, ResNet) and handling image processing tasks.
  - **OpenCV**: For pre-processing images before feeding them into the models.
  - **Streamlit**: To create a user-friendly web interface for the application.
  - **Flask**: For implementing the chatbot functionality to assist users with questions related to brain tumors and health.

- **Dataset**: The dataset consists of brain tumor images organized into two categories:
  - **'yes'**: Images with tumors.
  - **'no'**: Images without tumors.

## Installation

### Requirements

- Python 3.x
- TensorFlow
- OpenCV
- Streamlit
- Flask

### Install Libraries

To install the required libraries, run the following command:

```bash
pip install tensorflow opencv-python streamlit flask
```

## Usage

1. **Prepare the Dataset**: Create a directory named `data` with the following structure:

   ```
   data/
       yes/
           image1.jpg
           image2.jpg
           ...
       no/
           image1.jpg
           image2.jpg
           ...
   ```

2. **Run the Streamlit Application**:

   Launch the Streamlit application with the following command:

   ```bash
   streamlit run main.py
   ```

3. **Upload Images**: Use the Streamlit user interface to upload images and receive predictions about the presence of a tumor.

4. **Interact with the Chatbot**:
   - The chatbot is integrated within the Streamlit application to assist users in understanding brain tumors, symptoms, treatment options, and general health advice.
   - Users can type in their questions, and the chatbot will provide predefined responses or direct them to relevant resources.

## Chatbot Features

- **Information Retrieval**: The chatbot can answer common questions regarding brain tumors, such as:
  - What are the symptoms of brain tumors?
  - What are the treatment options available?
  - How can I maintain a healthy lifestyle?

- **User Engagement**: The chatbot is designed to encourage users to ask questions and engage in a conversation about health topics related to brain tumors.

- **Feedback Loop**: Users can provide feedback on the responses received, which can be used to improve the chatbot's performance over time.

## Contact

If you have any questions about this project, please feel free to contact me via email: [vohoanglam2211@gmail.com](mailto:vohoanglam2211@gmail.com).

---

