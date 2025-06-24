import os,sys
sys.path.append(os.path.abspath( '..'))
from load_model import Tiny_llm
import streamlit as st

model = Tiny_llm()

st.header('Research Tool')

user_input = st.text_input("Enter your Prompt")

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)


# st.header('Research Tool')
# user_input = st.text_input("Enter your Prompt")

# if st.button('Summarize'):
#     st.write("Sending prompt to model... Please wait ⏳")
#     try:
#         result = llm.invoke(user_input)
#         st.write("✅ Response received!")
#         st.write(result)  # Log entire result object
#         st.write(result.content)  # Main content
#     except Exception as e:
#         st.error(f"❌ Error: {e}")








