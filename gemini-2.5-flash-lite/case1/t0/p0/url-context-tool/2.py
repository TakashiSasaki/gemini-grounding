# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""要約して下さい。 https://www.ehime-u.ac.jp/data_event/ev_20260127_lib/"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""
愛媛大学図書館は、重複や改版、保存期間経過などにより利用予定がなくなった図書や雑誌を低価格で販売する「除籍図書等リユースセール」を2026年2月9日（月）と10日（火）に城北キャンパスで開催します。売上金は図書館の蔵書充実や学修環境整備に活用されます。図書は100円、雑誌は10円で販売され、マイバッグ持参と公共交通機関での来場が推奨されています。"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    tools = [
        types.Tool(url_context=types.UrlContext()),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,
        ),
        tools=tools,
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
