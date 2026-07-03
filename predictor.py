import os
import json

from groq import Groq
from dotenv import load_dotenv

from prompt import SYSTEM_PROMPT

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def predict(text):

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },

            {
                "role":"user",
                "content":text
            }
        ],

        temperature=0

    )

    result = response.choices[0].message.content

    return json.loads(result)