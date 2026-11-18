import os
from dotenv import load_dotenv

# Reads variables from the .env file and loads them into Python process's environment.
load_dotenv()

# os.getenv() retrieves the value of EVALKIT_MODEL/MODE/API_KEY from that environment.
model = os.getenv("EVALKIT_MODEL")
mode = os.getenv("EVALKIT_MODE")
api_key = os.getenv("EVALKIT_API_KEY")

print("Model:", model)
print("Mode:", mode)
print("API key configured:", bool(api_key))
