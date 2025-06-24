import sys, os
sys.path.append(os.path.abspath(".."))
from load_model import *
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Fixed: input_variable -> input_variables (plural)
prompt1 = PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=['topic']  # Fixed: was input_variable
)

prompt2 = PromptTemplate(
    template="Generate a 5 pointer summary from the following text:\n\n{text}",
    input_variables=['text']  # Fixed: was input_variable
)

model = Tiny_llm()
parser = StrOutputParser()

# Create the chain
chain = prompt1 | model | parser | prompt2 | model | parser

try:
    print("Starting chain execution...")
    result = chain.invoke({'topic': 'unemployment in India'})
    print("Result:")
    print(result)
except Exception as e:
    print(f"Error occurred: {e}")
    print("Make sure LM Studio server is running and model is loaded.")