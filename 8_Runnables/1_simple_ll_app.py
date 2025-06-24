import sys,os
sys.path.append(os.path.abspath(".."))
from load_model import *
from langchain_core.prompts import PromptTemplate

model = Tiny_llm()

prompt = PromptTemplate(
    template = 'Suggest a catchy blog title about {topic}.',
    input_variables = ['topic']
)

topic = input('Enter a topic: ')

formatted_prompt = prompt.format(topic = topic)

blog_title = model.predict(formatted_prompt)

print('Generated Blog Title',blog_title)