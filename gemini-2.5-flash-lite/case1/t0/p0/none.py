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
                types.Part.from_text(text="""愛媛大学附属図書館は、2026年1月27日に「図書館の未来を考えるシンポジウム」を開催します。

このシンポジウムでは、図書館の現状と課題を共有し、未来の図書館のあり方について参加者と共に考えます。

主な内容は以下の通りです。

*   **基調講演:** 図書館の専門家による、図書館の未来に関する最新の動向や展望についての講演。
*   **パネルディスカッション:** 図書館関係者や利用者代表などが登壇し、図書館のサービス向上や新たな役割について活発な議論を行います。
*   **ワークショップ:** 参加者がグループに分かれ、具体的な図書館の未来像や実現に向けたアイデアを出し合います。

このシンポジウムは、図書館の利用者、図書館関係者、教育関係者、地域住民など、図書館の未来に関心のあるすべての方々を対象としています。

参加費は無料ですが、事前申し込みが必要です。詳細は愛媛大学附属図書館のウェブサイトでご確認ください。"""),
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
