# Import necessary modules from the Streamlit library and LangChain library
import streamlit as st
from langchain.llms import OpenAI

# Set the title of the Streamlit app
st.title('🦜🔗 Quickstart App')

# Create a sidebar input where the user can enter their OpenAI API Key
openai_api_key = st.sidebar.text_input('OpenAI API Key')

# Define a function to generate a response using the OpenAI model from LangChain
def generate_response(input_text):
  # Initialize the OpenAI model with the provided API key and a temperature of 0.7
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  # Display the model's response in an info box on the app
  st.info(llm(input_text))

# Create a form named 'my_form' in the Streamlit app
with st.form('my_form'):
  # Create a text area inside the form where the user can enter text, with a default prompt
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    # Create a submit button inside the form
  submitted = st.form_submit_button('Submit')
  # Display a warning if the entered OpenAI API key is not valid
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  # If the form is submitted and the OpenAI API key is valid, call the generate_response function with the entered text
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)