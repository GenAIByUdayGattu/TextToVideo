import streamlit as st
import requests

# Streamlit app title
st.title("🎥 Video Generation Chatbot")

# Generate Video Tab
st.header("Generate Video")
user_input = st.text_input("Enter your video description:")
if st.button("Generate Video"):
    if not user_input:
        st.error("Please provide a description!")
    else:
        with st.spinner("Generating video..."):
            try:
                # Send user input to backend
                response = requests.post(
                    "http://127.0.0.1:8000/generate_video",
                    json={"user_input": user_input},
                )
                if response.status_code == 200:
                    video_path = response.json().get("video_path")
                    st.video(video_path)
                    st.success("Video generated successfully!")
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
