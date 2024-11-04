

---

# Brain Tumor Classification using the VGG19 Model

This project uses the VGG19 model to classify brain tumor images from an image dataset. The application is built using Streamlit, allowing users to upload images and receive predictions about the presence of a tumor.

## Project Overview

- **Model**: VGG19 fine-tuned for image classification tasks.
- **Libraries**: Utilizes TensorFlow and Streamlit.
- **Dataset**: Brain tumor images are categorized into two classes: 'yes' (tumor present) and 'no' (tumor absent).

## Installation

### Requirements

- Python 3.x
- TensorFlow
- OpenCV
- Streamlit

### Install Libraries

```bash
pip install tensorflow opencv-python streamlit
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

   ```bash
   streamlit run brain_tumor_classification.py
   ```

3. **Upload Images**: Use the Streamlit user interface to upload images and receive predictions.

## Contact

If you have any questions about this project, please contact me via email: [vohoanglam2211@gmail.com](mailto:vohoanglam2211@gmail.com).

--- 
