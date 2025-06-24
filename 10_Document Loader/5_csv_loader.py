from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Churn_Modelling.csv')

data = loader.load()

print(data[1])
print(len(data))