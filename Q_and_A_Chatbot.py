### Q & A ChatBot App

from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv() # takes the environmwnt variables from the .env file
import os
import streamlit as st

# Function to load OPENAI model and get responses
os.getenv("OPEN_API_KEY")
def get_openai_response(question):
    llm = OpenAI(model_name ="gpt-3.5-turbo-instruct", temperature= 0.5)
    response=llm(question)
    return response
 
## initialize our streamlit app
    
st.set_page_config(page_title="SAMPLE Q&A ChatBot")

st.header("Karthik's Q&A ChatBot Developed Using Langchain")

input = st.text_input("Input : ", key = "input")
response = get_openai_response(input)

submit = st.button("Ask the Question")

## if ask button is clicked 
if submit:
    st.subheader("The Response is: ")
    st.write(response)
