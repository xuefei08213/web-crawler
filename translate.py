# from openai import OpenAI
#
# client = OpenAI()

import os
from volcenginesdkarkruntime import Ark

print(os.environ.get("ARK_API_KEY"))

client = Ark(
    api_key=os.environ.get("ARK_API_KEY"),
    timeout=120,
    max_retries=2
)


def translate(text):
    if text != "":
        print("开始翻译"+text)
        system_message = f"""
        你是一个翻译助手，将输入的段落从英文翻译为中文，并输出翻译后的中文结果。
        """
        completion = client.chat.completions.create(
            model="ep-20240819124512-f4mqn",
            messages=[
                {'role': 'system', 'content': system_message},
                {'role': 'user', 'content': f"{text}"},
            ]
        )
        # print(completion.choices[0].message.content)
        translated_text = completion.choices[0].message.content
        print("翻译结束,翻译结果为："+translated_text)
        return translated_text

    return ""


graph = """
In the traditional session-based authentication mindset, the server maintains the state of the user's session,
typically using a session ID stored in a cookie. While functional for simpler, monolithic applications,
 this model shows its limitations in the face of modern, distributed applications. These limitations manifest in several ways:
"""

translate(graph)
