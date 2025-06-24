import sys,os
sys.path.append(os.path.abspath(".."))
from load_model import *
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = Thebloke_llm()

prompt = PromptTemplate(
    template = "Generate 5 intersting facts about {topic}",
    input_variable = ['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()