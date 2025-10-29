import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
api_key= os.getenv('DEEKSEEK_API_KEY')   
base_url = os.getenv('DEEKSEEK_API_BASE')

# 初始化 OpenAI 客户端
client = OpenAI(
    base_url=base_url,
    api_key=api_key
)

# 1. 为模型定义可调用工具列表
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_horoscope",
            "description": "获取指定星座的今日运势",
            "parameters": {
                "type": "object",
                "properties": {
                    "sign": {
                        "type": "string",
                        "description": "星座名称，如金牛座或水瓶座",
                    },
                },
                "required": ["sign"],
            },
        }
    },
]

# 创建一个消息列表，随着时间推移会不断添加内容
messages = [
    {"role": "user", "content": "我的运势如何？我是水瓶座。"}
]

# 2. 使用定义的工具提示模型
response = client.chat.completions.create(
    model="deepseek-chat",
    tools=tools,
    messages=messages,
)

print("response:")
print(response)

print("response_model_dump:")
print(response.model_dump())

print("模型初始输出:")
print(json.dumps(response.model_dump(), indent=2, ensure_ascii=False))

# 保存函数调用输出以供后续请求使用
function_call = None
function_call_arguments = None
messages.append(response.choices[0].message)

print("messages:")
print(messages)

# 检查模型是否想要调用函数
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    function_call = tool_call
    function_call_arguments = json.loads(tool_call.function.arguments)


def get_horoscope(sign):
    return f"{sign}: 下周二你将结识一只小水獭。"


# 3. 执行 get_horoscope 函数逻辑
result = {"horoscope": get_horoscope(function_call_arguments["sign"])}

print("result:")
print(result)

print("result_json_dump:")
print(json.dumps(result))

# 4. 向模型提供函数调用结果
messages.append({
    "tool_call_id": function_call.id,
    "role": "tool",
    "name": "get_horoscope",
    "content": json.dumps(result),
})
print("messages:")
print(messages)

print("消息流程:")
for i, message in enumerate(messages):
    if isinstance(message, dict):
        role = message.get('role', 'unknown')
        if role == 'user':
            print(f"{i+1}. 用户输入: {message.get('content', '')}")
        elif role == 'tool':
            content = json.loads(message.get('content', '{}'))
            print(f"{i+1}. 工具返回: {content}")
    else:
        print(f"{i+1}. 助手: 调用工具 {message.tool_calls[0].function.name if message.tool_calls else '无工具调用'}")


response = client.chat.completions.create(
    model="deepseek-chat",
    tools=tools,
    messages=messages,
)

# 5. 模型应该能够给出响应！
print("最终输出:")
print(json.dumps(response.model_dump(), indent=2))
print('response:')
print(response)
print("response content:")
print("\n" + response.choices[0].message.content)
