import extract_key
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")

result = model.invoke("How many countries in Africa")

print(result.content)