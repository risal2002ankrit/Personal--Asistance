from config import apikey

# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
client = OpenAI(
    api_key=apikey
)

response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="note on COW",
    temperature=1,
    max_tokens=10,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
print(response["choices"][0]["text"])
