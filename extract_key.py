import os
import key

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = key.OPENAI_API_KEY
