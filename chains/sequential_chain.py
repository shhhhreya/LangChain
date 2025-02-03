from langchain_core.runnables import RunnableLambda

def addOne(x:int) -> int:
    return x+1

def multiplyTwo(x:int)-> int:
    return x*2

runnable1 = RunnableLambda(addOne)
runnable2 = RunnableLambda(multiplyTwo)

chain = runnable1 | runnable2

print(chain.invoke(2))
print(chain.batch_as_completed([5,1,4]))
print(chain.batch([5,1,3]))