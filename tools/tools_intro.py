from langchain_core.tools import tool

@tool
def multiply(a:int, b:int) -> int:
    """Multiply two numbers."""
    return a*b

res = multiply.invoke({'a':2, 'b':3})
print(res)

print(multiply.name) # multiply
print(multiply.description) # Multiply two numbers.
print(multiply.args) 

