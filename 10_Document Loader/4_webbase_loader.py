import sys,os
sys.path.append(os.path.abspath(".."))
from load_model import *
from langchain_community.document_loaders import WebBaseLoader
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = Mistral_llm()

prompt = PromptTemplate(
    template='Answer in one line of the following Question \n {question} \n from the following text.\n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.flipkart.com/apple-iphone-16-teal-256-gb/p/itm2b7be11cfadef?pid=MOBH4DQFYKJHESFG&lid=LSTMOBH4DQFYKJHESFGP6ZE0Z&marketplace=FLIPKART&q=iphone&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=4700512c-3a36-4391-919e-e7b0d902420e.MOBH4DQFYKJHESFG.SEARCH&ppt=hp&ppn=homepage&ssid=1a3dg8g0tc0000001750343547926&qH=0b3f45b266a97d70'

loader = WebBaseLoader(url)

docs = loader.load()

ques = input("Ask Your Query: ")

chain = prompt | model | parser

result = chain.invoke({'question':ques,'text':docs[0].page_content[1000:7000]})

print(result)

# print(docs[0].page_content)

# print(len(docs))

