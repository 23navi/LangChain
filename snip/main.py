import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import argparse

parser= argparse.ArgumentParser()
parser.add_argument("--task",default="Print number from 1 to 100")
parser.add_argument("--language",default="js")
args= parser.parse_args()

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
      prompt=code_prompt,
      output_key="code"
)

test_prompt = PromptTemplate(
      template="Write test in {language} for the code:\n{code}",
      input_variables=["code","language"]
)

test_chain = LLMChain(
      llm=llm,
      prompt=test_prompt,
      output_key="test_code"
)


# result = llm("Write a very short poem")
# print(result)

seq_result_chain= SequentialChain(
      chains=[code_chain,test_chain],
      input_variables=["task","language"],
      output_variables=["test_code","code"]
)

# result = code_chain({
#       "language":args.language,
#       "task":args.task
# })

result = seq_result_chain({
      "language":args.language,
      "task":args.task
})

print(result["code"])
print("\n----------\n")
print(result["test_code"])