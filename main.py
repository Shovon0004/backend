import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "b813fde7-815c-419a-b02f-c3983c6e2d4f"
FLOW_ID = "fc69aa7e-9ae9-4ff7-8570-23546e8c9983"
APPLICATION_TOKEN = os.environ.get('APP_TOKEN')
ENDPOINT = FLOW_ID  

def run_flow(text: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"
    payload = {
        "input_value": text,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("Social Media Engagement Analysis")
    text = st.text_input("Enter your post type here:", placeholder="e.g. reels, static post, carousel, etc.")
    if st.button("Run"):
        if not text:
            st.write("Please enter a post type.")
            return
        try:
            with st.spinner("Running the model..."):
                response = run_flow(text)

            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))

if __name__ == "__main__":
    main()