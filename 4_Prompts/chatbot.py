import os,sys
sys.path.append(os.path.abspath( '..'))
# from load_model import Tiny_llm,Mistral_llm
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
import google.generativeai as genai
from dotenv import load_dotenv
from IPython.display import Markdown, display

load_dotenv()
api_key = os.getenv("GOOGLE_GENAI_API_KEY")

genai.configure(api_key=api_key)


# model = Mistral_llm()

model = genai.GenerativeModel('gemini-2.5-flash')


# chat_history = [
#     SystemMessage(content = "You are a helpful AI assistant")
# ]

# while True: 
#     user_input = input('You: ')
#     chat_history.append(HumanMessage(content=user_input))
#     if user_input == 'exit':
#         break
#     result = model.invoke(chat_history)
#     chat_history.append(AIMessage(content=result.content))
#     print('AI: ',result.content)

# print(chat_history)



# response = model.generate_content("What is the GenAI?")

# print(response.text)

chat_history= model.start_chat(history=
                               [{
                                   "role" : "user", "parts" : ["You are Helpful Assistant."]
                               }])
while True: 
    user_input = input('You: ')
    # chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        break
    # result = model.generate_content(chat_history)
    # chat_history.append(AIMessage(content=result.text))
    result = chat_history.send_message(user_input)
    print('AI: ',result.text)

print(chat_history)