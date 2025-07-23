import requests
from llama_index.llms.custom import CustomLLM
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex,ServiceContext

class LMStudioLLM(CustomLLM):
    def complete(self,prompt:str, **kwargs) -> str:
        response = requests.post(
            "http://127.0.0.1:1234/v1/completions",
            headers={"Content-Type":"application/json"},
            json={
                "model": "phi-2", 
                "prompt": prompt,
                "max_tokens": 500,
                "temperature": 0.7
            }
        )
        return response.json()["choices"][0]["text"]


def main():
    url = "https://joinseven.medium.com/blog-series-genai-a-brief-introduction-in-generative-ai-4e11154df3f2"

    llm = LMStudioLLM()
    Service_context = ServiceContext.from_defaults(llm=llm)

    document = SimpleWebPageReader(html_to_text = True).load_data([url])
    index = VectorStoreIndex.from_documents(document,Service_context)

    query_engine = index.as_query_engine()
    response = query_engine.query("What is the History of Generative AI?")
    print(response)

if __name__ == "__main__":
    main()