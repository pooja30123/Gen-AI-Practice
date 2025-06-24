from langchain.prompts import PromptTemplate

#Template
template = PromptTemplate(
    template = """
    Please Summarize the Research Paper Title 
    "{paper_input}" with the following specification: 
    Explaination Style : {style_input}
    Explaination length : {length_input}
    1.Mathematical Details:
        -include relevent mathematical equation if present in paper.
        -Explain th mathematical concept using simple intitive code     snippets where aplicable.
    2. Analogies:
        -Use relatable analogies to simplify complex ideas. If certain information is not available in the paper response with:"Insufficient information available" instead of guessing.
        -Ensure the summary in clear, accurate and aligned with the provided style and length.
    """,
    input_variables = ['paper_input','style_input','length_input'],
    validate_template = True
)

template.save("tamplate.json")