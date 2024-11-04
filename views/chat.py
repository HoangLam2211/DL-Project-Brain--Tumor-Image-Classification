import streamlit as st
import google.generativeai as genai

def chatbot_response(chat, message, history):
    # Define specific responses based on user input
    if "cách tải ảnh lên" in message.lower():
        chatbot_reply = (
            "Vui lòng click vào phần Upload and Predict để tải ảnh bạn muốn dự đoán có u não hay không, "
            "sau khi tải ảnh lên, xin vui lòng chờ kết quả trong giây lát."
        )
        history.append((message, chatbot_reply))
        return history

    if "lưu ý khi sử dụng ứng dụng" in message.lower():
        chatbot_reply = (
            "Mọi kết quả của chatbot chỉ là dự đoán, vui lòng gặp bác sĩ chuyên khoa để có thể có kết quả rõ ràng hơn về chẩn đoán của mình."
        )
        history.append((message, chatbot_reply))
        return history

    # Default response using the chatbot model
    history.append((message, ""))

    system_message = (
        "Bạn là một chatbot chuyên nghiệp trong lĩnh vực y tế, đặc biệt về chủ đề u não. "
        "Ngoài việc trả lời các câu hỏi liên quan đến các loại u não, triệu chứng, chẩn đoán, điều trị, và phương pháp phục hồi, "
        "bạn cũng có thể giải thích kết quả phân loại, cung cấp hướng dẫn sử dụng ứng dụng, và các lưu ý quan trọng khi sử dụng. "
        "Nếu người dùng cần, hãy hướng dẫn cách tải ảnh lên, đọc hiểu kết quả dự đoán, và đưa ra các gợi ý tương tác khác. "
        "Hãy trả lời ngắn gọn, rõ ràng, và có thể cung cấp thông tin chi tiết nếu cần thiết. "
        "Nếu câu hỏi chưa rõ, yêu cầu người dùng cung cấp thêm thông tin cụ thể hơn."
    )

    context = ""
    for user_message, bot_reply in history:
        context += f"{user_message}\n {bot_reply}\n"

    response = chat.send_message(system_message + "\n\n" + context + "Người dùng: " + message, stream=True)
    chatbot_reply = ""
    for chunk in response:
        if chunk.text:
            chatbot_reply += chunk.text + " "

    history[-1] = (message, chatbot_reply.strip())
    return history  

def show():
    genai.configure(api_key='AIzaSyBqHLvnvATwKlnQEhmJQxM_BSAQolc0hg4')  # Replace with your actual API key
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[])

    st.title("Chatbot Hỗ trợ Y tế - U Não")
    st.write("Xin chào! Tôi có thể giúp gì cho bạn?")

    if 'history' not in st.session_state:
        st.session_state.history = []

    chat_area = st.container()
    with chat_area:
        if st.session_state.history:
            for user_message, bot_reply in st.session_state.history:
                st.chat_message("user").markdown(user_message)
                st.chat_message("assistant").markdown(bot_reply)

    user_input = st.text_input("Câu hỏi của bạn...", "")

    # Interaction tips
    st.write("💡 Mẹo: Bạn có thể hỏi cách tải ảnh lên, cách đọc hiểu kết quả phân loại, "
             "hoặc lưu ý khi sử dụng ứng dụng.")

    if st.button("Gửi"):
        if user_input:
            st.session_state.history = chatbot_response(chat, user_input, st.session_state.history)

            # Clear input field
            st.text_input("Câu hỏi của bạn...", "", key="new_input")
            st.rerun()

            with chat_area:
                for user_message, bot_reply in st.session_state.history:
                    st.chat_message("user").markdown(user_message)
                    st.chat_message("assistant").markdown(bot_reply)
