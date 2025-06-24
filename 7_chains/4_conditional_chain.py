import sys,os
sys.path.append(os.path.abspath(".."))
from load_model import *
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel , RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal


model = Thebloke_llm()

parser = StrOutputParser()

class Feedback(BaseModel):

    sentiment:Literal['positive','negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object = Feedback)

prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following feedback text into positive or negative return a single word either positive or negative \n {feedback} \n {format_instruction}',
    input_variables = ['feedback'],
    partial_variables = {'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

# result = classifier_chain.invoke({'feedback':'This is a good smartphone'})

# print(result)

prompt2 = PromptTemplate(
    template = 'Write an appropriate response of the following positive feedback \n {feedback}',
    input_variables = ['feedback']
)

prompt3 = PromptTemplate(
    template = 'Write an appropriate response of the following negative feedback \n {feedback}',
    input_variables = ['feedback']
)

branch_chain = RunnableBranch(
    (lambda x : x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x : x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x : "Could not find Sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback':'The product was waste of money ,It broken on next day'})

print(result)

chain.get_graph().print_ascii()