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
        translated_text = completion.choices[0].message.content
        print("翻译结束,翻译结果为：" + translated_text)
        return translated_text

    return ""
