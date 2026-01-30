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
                types.Part.from_text(text="""愛媛大学図書館は、2026年1月27日に「除籍図書等リユースセール」を開催します。このセールでは、重複や改版等により利用予定のない図書や、保存期間が過ぎた雑誌が低価格で販売されます。売上金は図書館の蔵書充実や学修環境整備に活用されます。セールは愛媛大学城北キャンパスのE.U. Regional Commons（ひめテラス）1階 NP地域交流ルームにて、2026年2月9日（月）10:00～16:00と2月10日（火）10:00～14:00に開催されます。図書は100円、雑誌は10円で購入できます。"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        top_p=0.001,
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,
        ),
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
