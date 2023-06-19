import os
try:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
except:
    OPENAI_API_KEY = None