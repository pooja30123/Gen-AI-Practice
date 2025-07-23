# from load_model import *

# llm = Tiny_llm()

# response = llm.invoke("What is LangChain?")
# print(response.content)






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



from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load variables from .env file
load_dotenv()

# Get the API key from environment
api_key = os.getenv("GOOGLE_GENAI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)
