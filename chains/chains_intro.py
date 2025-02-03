from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

prompt_template = ChatPromptTemplate([
    ("system", "you are a facts expert who knows facts about {animal}."),
    ("human", "Tell mde {fact_count} facts.")
])

chain = prompt_template | model | StrOutputParser()


result = chain.invoke({"animal":"cat", "fact_count":2})

print(result)
