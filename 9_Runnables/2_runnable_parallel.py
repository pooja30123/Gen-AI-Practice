import sys,os
sys.path.append(os.path.abspath(".."))
from load_model import *
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a LinkedIn post about {topic}',
    input_variables=['topic']
)

model = Tiny_llm()

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweret':RunnableSequence(prompt1,model,parser),
    'linkedIn':RunnableSequence(prompt2,model,parser)
})

result = parallel_chain.invoke({'topic':'AI'})

print(result)