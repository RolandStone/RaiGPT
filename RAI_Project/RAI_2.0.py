import os
os.environ["OPENAI_API_KEY"] = "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"

from langchain.llms import OpenAI
llm = OpenAI(temperature=0.9)
text = input("input: ")
print(llm(text))
