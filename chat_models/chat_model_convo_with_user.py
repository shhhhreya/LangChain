#import extract_key
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

chat_history = []

sys_message = SystemMessage(content="You are helpful AI assistant")
chat_history.append(sys_message)

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content

    chat_history.append(AIMessage(content=response))

    print(f"AI: {response}")

print("---------Message History----------")
print(chat_history)

