from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize local model (LM Studio as OpenAI API)
llm = ChatOpenAI(
    model="mistral",  # or exact name shown in LM Studio if different
    temperature=0.7,
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    openai_api_key=os.getenv("OPENAI_API_KEY")  # 'lmstudio'
)

# Ask a question
response = llm.invoke([HumanMessage(content="What is the capital of India?")])

print("LLM Response:", response.content)
