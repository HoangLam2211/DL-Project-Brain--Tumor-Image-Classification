
# Phân loại khối u não bằng mô hình VGG19

Dự án này sử dụng mô hình VGG19 để phân loại hình ảnh khối u não từ một tập dữ liệu hình ảnh. Ứng dụng được xây dựng bằng Streamlit, cho phép người dùng tải lên hình ảnh và nhận dự đoán về việc có khối u hay không.

## Nội dung dự án

- **Mô hình**: VGG19 được tinh chỉnh cho bài toán phân loại hình ảnh.
- **Thư viện**: Sử dụng TensorFlow và Streamlit.
- **Tập dữ liệu**: Các hình ảnh khối u não được chia thành hai lớp: 'yes' (có khối u) và 'no' (không có khối u).

## Cài đặt

### Yêu cầu

- Python 3.x
- TensorFlow
- OpenCV
- Streamlit

### Cài đặt thư viện

```bash
pip install tensorflow opencv-python streamlit
```

## Cách sử dụng

1. **Chuẩn bị tập dữ liệu**: Tạo một thư mục `data` với cấu trúc như sau:

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

2. **Chạy ứng dụng Streamlit**:

   ```bash
   streamlit run brain_tumor_classification.py
   ```

3. **Tải lên hình ảnh**: Sử dụng giao diện người dùng của Streamlit để tải lên hình ảnh và nhận dự đoán.

## Liên hệ

Nếu bạn có bất kỳ câu hỏi nào về dự án này, hãy liên hệ với tôi qua email: [vohoanglam2211@gmail.com](mailto:vohoanglam2211@gmail.com).
```
