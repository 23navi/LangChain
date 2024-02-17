import os
from langchain.llms import OpenAI

api_key= os.environ.get("OPENAI_API_KEY","default")
print(f"OpenAI API key {api_key}")

llm = OpenAI(
      openai_api_key= api_key
)

result = llm("Write a very short poem")

print(result)