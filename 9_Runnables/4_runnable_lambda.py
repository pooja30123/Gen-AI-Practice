# Generate a joke also write how many words in joke

import sys,os
sys.path.append(os.path.abspath(".."))
from load_model import *
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda

def word_counter(text):
    return len(text.split())

# runnable_word_counter = RunnableLambda(word_counter)

# print(runnable_word_counter.invoke("Hi there how are you?"))

prompt = PromptTemplate(
    template='write a one line joke about {topic}',
    input_variables=['topic']
)

model = Tiny_llm()

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt,model,parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count' : RunnableLambda(word_counter)
})

chain = RunnableSequence(joke_gen_chain,parallel_chain)

print(chain.invoke({'topic':'AI'}))

