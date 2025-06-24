import os,sys
sys.path.append(os.path.abspath( '..'))
from load_model import Tiny_llm
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

model = Tiny_llm()

messages = [
    SystemMessage(content = "You are a helpful assistant"),
    HumanMessage(content = "Tell me about Langchain")
]

result = model.invoke(messages)

messages.append(AIMessage(content = result.content))

print(messages)