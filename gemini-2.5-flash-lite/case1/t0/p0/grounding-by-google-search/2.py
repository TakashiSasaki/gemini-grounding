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
                types.Part.from_text(text="""愛媛大学附属図書館は、2026年2月9日（月）と10日（火）に「除籍図書等リユースセール」を開催します。このセールでは、重複や改版等により利用予定のない図書や、保存期間が過ぎた雑誌が低価格で販売されます。売上金は図書館の蔵書充実や学修環境整備に活用されます。セールは城北キャンパスのE.U. Regional Commons 1階 NP地域交流ルームにて行われ、図書は100円、雑誌は10円で購入できます。来場者にはマイバッグの持参が推奨されており、転売目的での購入はご遠慮ください。また、電子マネーは利用できず、小銭の用意が必要です。"""),
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
