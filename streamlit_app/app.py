import json
import requests
import streamlit as st
from typing import Optional

# Base URL and identifiers for the flow
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "8f7cca58-a7f2-43f9-9ed1-449933025472"
FLOW_ID = "4108084b-4b9f-4655-aa40-b0d9b02a85d1"
APPLICATION_TOKEN = "AstraCS:inSJNFvIjuJvGgQfRBhTBNsU:81e6fce7b7a385b5c33365260fd6c19b3bafa945e6ca5ac1c12a96b674c41949"
ENDPOINT = "" # You can set a specific endpoint name in the flow settings

# Default tweaks dictionary to modify flow behavior
DEFAULT_TWEAKS = {
    "ChatOutput-xTViY": {},
    "TextInput-eCRx5": {},
    "Prompt-JfODg": {},
    "Memory-CeBFr": {},
    "ChatInput-v1uLB": {},
    "AstraDBChatMemory-qizKA": {},
    "OpenAIModel-U0Hkq": {}
}

# Function to run the flow with the provided message
def run_flow(message: str,
             endpoint: str = ENDPOINT,
             output_type: str = "chat",
             input_type: str = "chat",
             tweaks: Optional[dict] = None,
             application_token: Optional[str] = APPLICATION_TOKEN) -> dict:
    """
    Run a flow with a given message and optional tweaks.
    :param message: The message to send to the flow
    :param endpoint: The endpoint name of the flow
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{FLOW_ID}?stream=false"
    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    if tweaks:
        payload["tweaks"] = tweaks
    headers = {
        "Authorization": "Bearer " + application_token,
        "Content-Type": "application/json"
    }
    
    # Send the request to the flow
    response = requests.post(api_url, json=payload, headers=headers)
    
    # Check if the response is valid
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch response", "details": response.text}

# Streamlit app for UI using chat UI
def main():
    st.title("Social Media Performance Analysis")

    # Initialize session state for messages
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Input form for user message
    message = st.chat_input("Enter your message:")

    # Add an option for tweaking the flow
    tweaks_option = st.checkbox("Customize Flow Tweaks")
    tweaks = DEFAULT_TWEAKS
    if tweaks_option:
        tweak_json_input = st.text_area("Enter custom tweaks (JSON format):", value=json.dumps(DEFAULT_TWEAKS, indent=2))
        try:
            tweaks = json.loads(tweak_json_input)
        except json.JSONDecodeError:
            st.error("Invalid JSON format for tweaks.")

    # When the user sends a message
    if message:
        if message.strip() == "":
            st.error("Please enter a message.")
        else:
            # Run the flow
            try:
                with st.spinner("Running flow..."):
                    response = run_flow(message, tweaks=tweaks)
                    
                    if "error" in response:
                        st.error(response["details"])
                    else:
                        response_text = response.get("outputs", [{}])[0].get("outputs", [{}])[0].get("results", {}).get("message", {}).get("text", "No response from flow.")
                        
                        # Save the chat history in the session state
                        st.session_state["messages"].append({"user": message, "bot": response_text})

            except Exception as e:
                st.error(f"Error: {e}")

    # Display the chat history
    for chat in st.session_state["messages"]:
        with st.chat_message("user"):
            st.markdown(chat['user'])
        with st.chat_message("bot"):
            st.markdown(chat['bot'])

# Run the Streamlit app
if __name__ == "__main__":
    main()