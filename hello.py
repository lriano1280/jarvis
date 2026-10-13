import json
import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()  # lee ANTHROPIC_API_KEY del archivo .env

resp = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=200,
    messages=[
        {
            "role": "user",
            "content": "Preséntate en 2 frases como J.A.R.V.I.S., el asistente de Leo.",
        }
    ],
)

texto = "".join(b.text for b in resp.content if b.type == "text")

salida = {
    "texto": texto,
    "tokens_entrada": resp.usage.input_tokens,
    "tokens_salida": resp.usage.output_tokens,
}

os.makedirs("out", exist_ok=True)
with open("out/hoy.json", "w", encoding="utf-8") as f:
    json.dump(salida, f, ensure_ascii=False, indent=2)

print(salida)