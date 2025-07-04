from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = 'google/gemma-2-2b-it',
    task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me  the name ,age and city of a frictional person \n {format_instruction}',
    input_variable = [],
    partial_variable = {'format_instruction':parser.get_format_instructions()}
)

# prompt = template.format()

# #print(prompt)

# result = model.invoke(prompt)

# final_result = parser.parser(result.content)

# print(final_result)
# print(type(final_result))

chain = template | model | parser

result = chain.invoke({})

print(result)