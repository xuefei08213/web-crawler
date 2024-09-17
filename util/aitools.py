import os

from dotenv import load_dotenv
from volcenginesdkarkruntime import Ark

load_dotenv()

print(os.environ.get("ARK_API_KEY"))

client = Ark(
    api_key=os.environ.get("ARK_API_KEY"),
    timeout=120,
    max_retries=2
)

def translate(text):
    if text != "":
        print("开始翻译" + text)
        translate_system_message = f"""
        你是一个翻译助手，将输入的段落从英文翻译为中文，并输出翻译后的中文结果。
        """
        translate_completion = client.chat.completions.create(
            model="ep-20240819124512-f4mqn",
            messages=[
                {'role': 'system', 'content': translate_system_message},
                {'role': 'user', 'content': f"{text}"},
            ]
        )
        translated_text = translate_completion.choices[0].message.content
        print("翻译结束,翻译结果为：" + translated_text)
        return translated_text

    return ""

def extract_code_from_pre(preinnerhtml):
    if preinnerhtml != "":
        print("开始从html中提取代码" + preinnerhtml)
        extract_code_system_message = f"""
        将上面这段html中的代码提取出来。注意以下几点
        1、返回内容中只包含代码
        2、注意代码换行
        3、返回内容以markdown格式
        """
        extract_code_completion = client.chat.completions.create(
            model="ep-20240819124512-f4mqn",
            messages=[
                {'role': 'system', 'content': extract_code_system_message},
                {'role': 'user', 'content': f"{preinnerhtml}"},
            ]
        )
        code = extract_code_completion.choices[0].message.content
        print("提取的代码为：" + code)
        return code
