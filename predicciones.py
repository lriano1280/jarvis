import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
pares = [
    ("Soy el Iron Man de la IA", "I am the Iron Man of AI"),
    ("Quiero aprender inteligencia artificial", "I want to learn artificial intelligence"),
    ("El gato duerme en el sofá", "The cat sleeps on the sofa"),
]
print(f"{'ES':>5} {'EN':>5}  frase")
for es, en in pares:
    print(f"{len(enc.encode(es)):>5} {len(enc.encode(en)):>5}  {es}")