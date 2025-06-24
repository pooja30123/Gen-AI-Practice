import os,sys
sys.path.append(os.path.abspath( '..'))
from load_model import Tiny_llm
import streamlit as st
from langchain.prompts import PromptTemplate,load_prompt


model = Tiny_llm()

st.header('Research Tool')

paper_input = st.selectbox("Select Research Paper Name",["Select....","Attention Is All You Need","BERT: Pre-training of Deep Bidirectional Transformers","GPT-3: Language Models are Few-Short Learners","Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explaination Style",["Beginner-Friendly" ,"Technical","Code-Oriented","Mathematical"])

length_input = st.selectbox("Select Explaination Length",["Short (1-2 paragraph)", "Medium (3-5 paragraph)", "Long (detailed explaination)"])

template = load_prompt('tamplate.json')



if st.button('Summarize'):
    chain = template|model
    result = chain.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
    })
    st.write(result.content)








