import sys,os
sys.path.append(os.path.abspath('..'))
from load_model import *
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = Tiny_llm()

prompt = PromptTemplate(
    template='Suggest a catchy blog title about {topic}.',
    input_variables=['topic']
)

chain = LLMChain(llm=llm,prompt=prompt)

topic = input("Enter Topic: ")
output = chain.invoke(topic)

print("Generated Blog Title: ",output)
