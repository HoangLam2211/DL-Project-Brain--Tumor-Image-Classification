import streamlit as st
from views import home

def main():
    st.set_page_config(
    page_title="Chatbot Brain Tumor",
    page_icon="🤖",
    layout="wide"
)
    home.show()  
if __name__ == "__main__":
    main()