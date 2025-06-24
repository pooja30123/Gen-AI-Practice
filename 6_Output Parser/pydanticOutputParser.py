from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = 'google/gemma-2-2b-it',
    task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):

    name : str = Field(description="Name of the Person")
    age : int = Field(gt=18,description="age of the person")
    city : str = Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object = Person)

template = PromptTemplate(
    template = "Generate the name,age and city of the frictional {place} person \n {format_instruction}",
    input_variables = ['place'],
    partial_variables = {'formate_instruction':parser.get_format_instructions()}
)

# prompt = template.invoke({'place':'Indian'})

# print(prompt )

# result = model.invoke(prompt)

# final_result = parser.parser(result.content)

# print(result)

chain = template | model | parser

result = chain.invoke({'place':'sri lanka'})

print(result)