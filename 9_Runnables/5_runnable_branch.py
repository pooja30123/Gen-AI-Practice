# take a topic from user generate a report from the llm apply the runnable branch and check whether the report is less 500 words or not and if not then summarie the report

import sys,os
sys.path.append(os.path.abspath(".."))
from load_model import *
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

model = Tiny_llm()

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1,model,parser)

# sub = input("Enter Topic: ")

# result = report_gen_chain.invoke({'topic':sub})

# print(result)

# with open(f"{sub}_report.txt", "w", encoding="utf-8") as file:
#     file.write(result)

branch_chain = RunnableBranch(
    (lambda x:len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough() 
)

final_chain = RunnableSequence(report_gen_chain,branch_chain)

result = final_chain.invoke({'topic':'India Vs Pakistan Match 2025'})

print(result)

