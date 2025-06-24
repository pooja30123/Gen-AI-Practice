from langchain_community.document_loaders import PyPDFLoader,Py

loader = PyPDFLoader("GenAI-and-Prompt-Engineering.pdf")

docs = loader.load()

# print(docs)

print(len(docs))

print(docs[1].page_content)

print(docs[1].metadata)