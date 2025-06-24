from langchain_community.document_loaders import TextLoader
import os,sys
sys.path.append(os.path.abspath(".."))
from load_model import *
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model = Mistral_llm()

prompt = PromptTemplate(
    template='Write a summary for the following report.\n {report}',
    input_variables=['report']
)

parser = StrOutputParser()

loader = TextLoader('Rohit Sharma_report.txt')

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({'report':docs[0].page_content})

print(result)

# print(docs)

# print(type(docs))

# print(len(docs))

# print(type(docs[0]))

# print(docs[0])