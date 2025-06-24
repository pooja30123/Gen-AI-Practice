import sys,os
sys.path.append(os.path.abspath(".."))
from load_model import *
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough


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


joke_gen_chain = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explaination' : RunnableSequence(prompt2,model,parser)
})

chain = RunnableSequence(joke_gen_chain,parallel_chain)

print(chain.invoke({'topic':'AI'}))

