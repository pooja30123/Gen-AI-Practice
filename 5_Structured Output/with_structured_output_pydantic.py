from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from typing import TypedDict,Annotated,Optional,Literal
from dotenv import load_dotenv
from pydantic import BaseModel,Field
import os

load_dotenv()

llm = ChatHuggingFace(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",  
    task="text-generation",                  
    model_kwargs={"temperature": 0.7}
)

#model = ChatHuggingFace(llm=llm)

class Review(BaseModel):

    key_themes:list[str] = Field(description="Write down all the key themes discuss in th review in the list")
    summary: str = Field(description="A brief summary of review")
    sentiment:Literal["pos","neg"] = Field(description="Return sentiment of the review either negative,positive or neutral")
    pros:Optional[list[str]] = Field(default=None,description="Write down all the pros inside a list")
    cons:Optional[list[str]] = Field(default=None,description="Write down all the cons inside a list")
    name:Optional[str] = Field(default=None,description="Write the name of the rviewer")

structured_model = llm.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great,but the software feeels bloated. There are too many pre-installed app that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for software update to fix this.""")

print(result)
print(result.summary)
print(result.sentiment)
print(result.name)