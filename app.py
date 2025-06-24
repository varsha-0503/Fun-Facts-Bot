import streamlit as st
from gradio_client import Client

st.set_page_config(page_title="🤖 Fun Facts Bot", page_icon="📚")
st.title("🤖 Fun Facts Chat Assistant")
st.write("Ask me for a fun fact about anything — like 'space', 'animals', or 'technology'!")

user_input = st.text_input("You:")

if user_input:
    with st.spinner("Thinking of a fun fact..."):
        try:
            client = Client("varshaa2005/Fun-Facts-Bot", hf_token=st.secrets["HUGGINGFACE_TOKEN"])
            result = client.predict(
                user_input,     # 👈 your text input
                api_name="/predict"
            )
            st.success("🤓 " + result)
        except Exception as e:
            st.error(f"Error: {str(e)}")