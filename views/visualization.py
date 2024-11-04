import streamlit as st
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Đường dẫn đến thư mục chứa ảnh
path_u_nao = "archive/brain_tumor_dataset/yes"  
path_khong_u_nao = "archive/brain_tumor_dataset/no"  

# Hàm để lấy thông tin số lượng ảnh theo từng loại
def load_image_data(path_u_nao, path_khong_u_nao):
    class_counts = {
        "u não": len(os.listdir(path_u_nao)) if os.path.exists(path_u_nao) else 0,
        "không có u não": len(os.listdir(path_khong_u_nao)) if os.path.exists(path_khong_u_nao) else 0
    }
    
    class_images = {
        "u não": [os.path.join(path_u_nao, img) for img in os.listdir(path_u_nao)] if os.path.exists(path_u_nao) else [],
        "không có u não": [os.path.join(path_khong_u_nao, img) for img in os.listdir(path_khong_u_nao)] if os.path.exists(path_khong_u_nao) else []
    }
    
    return class_counts, class_images

# Hàm để vẽ histogram cường độ pixel
def plot_pixel_intensity(image_path):
    image = Image.open(image_path)
    image_array = np.array(image)
    if image_array.ndim == 3:  # Nếu là ảnh màu
        image_array = image_array.mean(axis=2)  # Chuyển đổi sang ảnh xám

    # Tạo figure và ax cho biểu đồ
    fig, ax = plt.subplots()
    ax.hist(image_array.flatten(), bins=256, color='gray', alpha=0.7)
    ax.set_xlim([0, 255])
    ax.set_xlabel('Cường độ Pixel')
    ax.set_ylabel('Tần suất')
    ax.set_title('Biểu đồ Cường độ Pixel')
    
    return fig  # Trả về figure

# Hàm để vẽ biểu đồ pie cho tỷ lệ ảnh
def plot_pie_chart(class_counts):
    labels = class_counts.keys()
    sizes = class_counts.values()
    colors = ['lightcoral', 'lightskyblue']
    
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Đảm bảo biểu đồ là hình tròn
    ax.set_title('Tỷ lệ số lượng ảnh theo loại')
    
    return fig  # Trả về figure

# Hàm để vẽ boxplot cường độ pixel
def plot_boxplot(class_images):
    pixel_values = {}
    for class_name, images in class_images.items():
        for img_path in images:
            image = Image.open(img_path)
            image_array = np.array(image)
            if image_array.ndim == 3:  # Nếu là ảnh màu
                image_array = image_array.mean(axis=2)  # Chuyển đổi sang ảnh xám
            pixel_values[class_name] = pixel_values.get(class_name, []) + image_array.flatten().tolist()
    
    fig, ax = plt.subplots()
    ax.boxplot(pixel_values.values(), labels=pixel_values.keys())
    ax.set_title('Phân bố cường độ pixel theo loại')
    ax.set_ylabel('Cường độ Pixel')

    return fig  # Trả về figure

# Hàm chính để hiển thị trên Streamlit
def show():
    st.title("Phân tích dữ liệu khám phá (EDA)")

    # Tải dữ liệu ảnh
    class_counts, class_images = load_image_data(path_u_nao, path_khong_u_nao)

    # Hiển thị số lượng ảnh theo từng loại
    st.write("### Số lượng ảnh theo từng loại:")
    st.bar_chart(class_counts)

    # Hiển thị biểu đồ pie cho tỷ lệ số lượng ảnh
    st.write("### Tỷ lệ số lượng ảnh theo loại:")
    pie_chart = plot_pie_chart(class_counts)
    st.pyplot(pie_chart)

    # Hiển thị mẫu ảnh
    st.write("### Mẫu ảnh từ từng loại:")
    for class_name, images in class_images.items():
        if images:  # Kiểm tra xem có ảnh trong loại đó không
            st.write(f"#### Loại: {class_name}")
            cols = st.columns(3)  # Hiển thị 3 ảnh trên một hàng
            for i, img_path in enumerate(images[:3]):  # Hiển thị 3 ảnh mẫu
                cols[i % 3].image(img_path, caption=class_name, use_column_width=True)
            
            # Expander để hiển thị tất cả ảnh của loại này
            with st.expander(f"Xem tất cả ảnh của loại '{class_name}'"):
                for img_path in images:
                    st.image(img_path, caption=class_name, use_column_width=True)

    # Phân tích cường độ pixel
    st.write("### Biểu đồ cường độ pixel:")
    selected_class = st.selectbox("Chọn loại ảnh để xem biểu đồ cường độ pixel:", list(class_images.keys()))
    if selected_class and class_images[selected_class]:  # Kiểm tra xem có ảnh để chọn không
        st.write(f"Biểu đồ cường độ pixel cho loại: {selected_class}")
        sample_image_path = class_images[selected_class][0]  # Chọn ảnh mẫu để vẽ histogram
        fig = plot_pixel_intensity(sample_image_path)  # Nhận figure từ hàm vẽ
        st.pyplot(fig)  # Hiển thị biểu đồ trong Streamlit

    # Vẽ boxplot cho cường độ pixel
    st.write("### Boxplot cường độ pixel cho các loại:")
    boxplot_fig = plot_boxplot(class_images)
    st.pyplot(boxplot_fig)  # Hiển thị boxplot trong Streamlit

