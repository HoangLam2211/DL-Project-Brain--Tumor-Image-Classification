import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image

# Giả định bạn đã lưu mô hình VGG19 và trọng số của nó
try:
    model = load_model('model\\vgg19_model_resnet.keras')  # Tải mô hình đã được lưu
except ValueError as e:
    st.error(f"Error loading model: {e}")
    model = None  # Set model to None if loading fails

# Hàm phân loại ảnh
def classify_image(image):
    if model is None:
        return "Model is not loaded.", 0

    # Tiền xử lý ảnh nếu cần thiết
    image = image.resize((240, 240))  # Điều chỉnh kích thước nếu cần
    image = np.array(image) / 255.0  # Chuẩn hóa
    image = image.reshape(1, 240, 240, 3)  # Thay đổi kích thước để phù hợp với đầu vào của mô hình
    prediction = model.predict(image)
    
    # Xác định lớp dự đoán
    if prediction[0][0] > 0.5:
        result = "Có u não"
        confidence = prediction[0][0]
    else:
        result = "Không có u não"
        confidence = 1 - prediction[0][0]
    
    return result, confidence

# Hàm hiển thị giao diện chính của ứng dụng
def show():
    st.title("Phân loại ảnh với VGG19")

    # Thêm sidebar để chọn trang
    options = st.sidebar.radio("Chọn một trang:", ["Phân loại ảnh"])

    if options == "Phân loại ảnh":
        st.title("Phân loại ảnh")
        uploaded_file = st.file_uploader("Tải ảnh lên", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Ảnh đã tải lên.', use_column_width=True)
            if st.button("Dự đoán"):
                result, confidence = classify_image(image)
                st.write(f"Kết quả phân loại: {result} với độ chính xác: {confidence:.2f}")
