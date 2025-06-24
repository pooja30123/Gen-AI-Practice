import os,sys
sys.path.append(os.path.abspath( '..'))
from load_model import Tiny_llm
from typing import TypedDict,Annotated,Optional,Literal
from langchain_openai import ChatOpenAI

model = Tiny_llm()

class Review(TypedDict):

    key_themes : Annotated[list[str],"Write down all the key themes discuss in th review in the list"]
    summary : Annotated[str,"A brief summary of review"]
    sentiment : Annotated[Literal["pos","neg"],"Return sentiment of the review either negative,positive or neutral"]
    pros : Annotated[Optional[list[str]],"Write down all the pros inside a list"]
    cons : Annotated[Optional[list[str]],"Write down all the cons inside a list"]


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great,but the software feeels bloated. There are too many pre-installed app that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for software update to fix this.""")

print(result)
print(result['summary'])
print(result['sentiment'])