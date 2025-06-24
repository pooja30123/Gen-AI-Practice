from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
import sys,os
sys.path.append(os.path.abspath(".."))
from load_model import *

loader = TextLoader('docs.txt')
document = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
docs = text_splitter.split_documents(document)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embeddings)

retriver = vectorstore.as_retriever()

llm = Thebloke_llm()

qa_chain = RetrievalQA.from_chain_type(llm=llm,retriver=retriver)

query = "What are the key takeaway from document?"
answer = qa_chain.run(query)

print("Answer",answer)

