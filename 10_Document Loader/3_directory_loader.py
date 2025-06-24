from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path='pdfs',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

# print(len(docs))   # no of pages in all pdfs

# print(docs[6].page_content)
# print(docs[6].metadata)


for document in docs:
    print(document.metadata)