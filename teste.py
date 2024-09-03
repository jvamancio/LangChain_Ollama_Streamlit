from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM


def generate_response(question):
    template = """Question: {question}

    Answer: Let's think step by step."""

    prompt = ChatPromptTemplate.from_template(template)

    model = OllamaLLM(model="qwen2:0.5b", api_base="http://localhost:11434/")

    chain = prompt | model

    response = chain.invoke({"question": question})

    return response