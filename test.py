from load_model import *

llm = Tiny_llm()

response = llm.invoke("What is LangChain?")
print(response.content)






# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

# # Test if server is reachable
# try:
#     response = requests.get(f"{os.getenv('OPENAI_API_BASE')}/models")
#     print("Available models:", response.json())
# except Exception as e:
#     print(f"Connection error: {e}")