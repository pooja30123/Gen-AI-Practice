from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
import sys,os
sys.path.append(os.path.abspath(".."))
from load_model import *

loader = TextLoader('docs.txt')
document = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
docs = text_splitter.split_documents(document)

vectorstore = FAISS.from_documents(docs,nomicEmbedding())

retriver = vectorstore.as_retriever()

query = "What are the key takeaway from document?"
retrieved_docs = retriver.get_retrievant_documents(query)

retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])

llm = Tiny_llm()

prompt = f"Based on the following text, answer the question : {query} \n\n {retrieved_text}"

answer  =llm.predict(prompt)

print("Answer",answer)

