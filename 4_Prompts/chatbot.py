import os,sys
sys.path.append(os.path.abspath( '..'))
from load_model import Tiny_llm,Mistral_llm
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage


model = Mistral_llm()

chat_history = [
    SystemMessage(content = "You are a helpful AI assistant")
]

while True: 
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI: ',result.content)

print(chat_history)