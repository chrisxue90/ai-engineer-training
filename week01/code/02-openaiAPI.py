import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('DEEKSEEK_API_KEY')
base_url = os.getenv('DEEKSEEK_API_BASE')
print(f"-- debug -- deepseek api key is {api_key[0:10]}******")

client = OpenAI(
    base_url=base_url,
    api_key=api_key
)


response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "Hello world!"}
    ]
)

print(response.choices[0].message.content)


# 正常会输出结果：Hello! It's great to see you. How can I assist you today?