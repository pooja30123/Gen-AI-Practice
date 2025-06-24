from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('GenAI-and-Prompt-Engineering.pdf')

text = loader.load()

# text = "Rohit Sharma is an Indian cricketer who has been playing for the country since 2013. He is one of the most successful batsmen in the country's history with over 6,500 test runs and more than 2,800 ODI runs. This report will explore Rohit Sharma's career highlights, performance statistics, and analysis of his contributions to India's success in cricket.Rohit was born on December 24th, 1985, in Mumbai, Maharashtra, India. He started playing cricket at a young age and joined the Delhi Cricket Academy at the age of 10. Rohit made his first-class debut for the Mumbai Cricket Association XI in 2003 and went on to play for them until 2007. In 2008, he was selected for India's Under-19 team, which he represented until 2011. Rohit made his international debut for the India A side against South Africa in January 2007. He went on to represent India in numerous Test matches and ODIs from 2013. Rohit's most notable achievement as a batsman is his 49-ball century against England in October 2016, which helped India win the series."

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator = ''
)

# result =splitter.split_text(text)
result =splitter.split_documents(text)

print(result[0].page_content)
print(result[0].metadata)
