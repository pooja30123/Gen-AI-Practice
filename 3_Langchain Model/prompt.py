from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id = 'meta-llama/Meta-Llama-3-70B-Instruct',
    task = 'text-generation'
)
model = ChatHuggingFace(llm=llm)

st.header('Research Tool')

user_input = st.text_input("Enter your Prompt")

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)








