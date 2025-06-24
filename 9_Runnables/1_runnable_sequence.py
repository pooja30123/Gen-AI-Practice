import sys,os
sys.path.append(os.path.abspath(".."))
from load_model import *
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

# prompt = PromptTemplate(
#     template='wrtie a one line joke about {topic}',
#     input_variables=['topic']
# )

prompt1 = PromptTemplate(
    template='wrtie a one line joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

model = Tiny_llm()

parser = StrOutputParser()

# chain = RunnableSequence(prompt,model,parser)

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

print(chain.invoke({'topic':'AI'}))

