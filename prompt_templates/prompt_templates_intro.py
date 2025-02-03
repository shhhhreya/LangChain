from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

template = "Write a {tone} email to {company} expressing interest in the {position}, mentioning {skill} as a key strength. Keep it upto 4 lines only"

prompt_template = ChatPromptTemplate.from_template(template)
prompt = prompt_template.invoke({
    "tone":"energetic",
    "company":"samsung",
    "position":"AI engineer",
    "skill":"AI"
})

messages = [
    ("system", "You are a young comedians who is joking about {topic}"),
    ("human", "tell me {joke_count} jokes")
]

prompt_template_ = ChatPromptTemplate(messages)
prompt_ = prompt_template_.invoke({
    "topic":"engineers",
    "joke_count": 3
})

result_ = llm.invoke(prompt_)

print(result_.content)