import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
api_key = os.getenv('DOUBAO_API_KEY')
base_url = os.getenv('DOUBAO_API_BASE')

# 初始化 DeepSeek 客户端
client = OpenAI(
    base_url=base_url,
    api_key=api_key
)

def query(user_prompt):
    """
    发送用户提示到 DeepSeek API 并返回响应内容
    
    参数:
        user_prompt (str): 用户输入的提示内容
        
    返回:
        str: AI 的响应内容
    """
    try:
        response = client.chat.completions.create(
            model="doubao-seed-1-6-lite-251015",
            messages=[
                {"role": "user", "content": user_prompt}
            ],
            reasoning_effort="medium"
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"错误: {str(e)}"

if __name__ == "__main__":
    print(query("早上好，今天想聊点什么呢?"))
