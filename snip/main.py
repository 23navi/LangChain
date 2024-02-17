import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

api_key= os.environ.get("OPENAI_API_KEY","default")
print(f"OpenAI API key {api_key}")

llm = OpenAI(
      openai_api_key= api_key
)

code_prompt = PromptTemplate(
      template="Write a very short {language} function that will {task}",
      input_variables=["language","task"]
)

code_chain = LLMChain(
      llm=llm,
      prompt=code_prompt
)

# result = llm("Write a very short poem")
# print(result)

result = code_chain({
      "language":"js",
      "task":"Print number from 1 to 100"
})

print(result)