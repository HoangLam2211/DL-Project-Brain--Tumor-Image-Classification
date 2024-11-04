import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Giả định bạn đã lưu mô hình VGG19 và trọng số của nó
model = load_model('model\\vgg19_model_03.keras')  # Tải mô hình đã được lưu
# model.load_weights('model_weights/vgg19_model_0.weights.h5')  # Tải trọng số

# Hàm phân loại ảnh
def classify_image(image):
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

# Giao diện chính
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
