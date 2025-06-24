from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from typing import TypedDict,Annotated,Optional,Literal
from dotenv import load_dotenv
from pydantic import BaseModel,Field
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

#schema
json_schema = {
    "title":"Review",
    "type":"object",
    "properties":{
        "key_name":{
            "type":"array",
            "item":{
                "type":"string"
            },
            "description":"Write down all key theme discuss in the review"
        },
        "summary":{
            "type":"string",
            "enum":["pos","neg"],
            "description":"Return sentiment of the review either positive, negative or neutral"
        },
        "pros":{
            "type":["array","null"],
            "items":{
                "type":"string"
            },
            "description":"Write down all the pros inside a list"
        },
        "cons":{
            "type":["array","null"],
            "items":{
                "type":"string"
            },
            "description":"Write down all the cons inside a list"
        },
        "name":{
            "type":["string","null"],
            "description":"Write the name of the reviewer" 
        }
    },
    "required":["key_themes","summary","sentiment"]
}

structured_model = llm.with_structured_output(json_schema)

result = structured_model.invoke("""The hardware is great,but the software feeels bloated. There are too many pre-installed app that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for software update to fix this.""")

print(result)
print(result.summary)
print(result.sentiment)
print(result.name)