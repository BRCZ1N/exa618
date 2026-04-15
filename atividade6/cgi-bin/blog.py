#!/usr/bin/env python3

import os
from datetime import datetime
from urllib.parse import parse_qs

ARQUIVO = "../posts.txt"

print("Content-type: text/html\n")

method = os.environ.get("REQUEST_METHOD", "")

autor = None
mensagem = None

if method == "POST":
    tamanho = int(os.environ.get("CONTENT_LENGTH", 0))
    dados = os.read(0, tamanho).decode("utf-8")
    form = parse_qs(dados)

    autor = form.get("autor", [""])[0]
    mensagem = form.get("mensagem", [""])[0]

    if autor and mensagem:
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open(ARQUIVO, "a", encoding="utf-8") as f:
            f.write(f"{data}|{autor}|{mensagem}\n")

posts = []
try:
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        for linha in f:
            data, autor, mensagem = linha.strip().split("|")
            posts.append((data, autor, mensagem))
except:
    pass

posts.reverse()

print("""
<html>
<head>
<meta charset="UTF-8">
<title>Postagens</title>
</head>
<body>

<h1>Postagens</h1>
<a href="/index.html">Voltar</a>
<hr>
""")

for data, autor, mensagem in posts:
    print(f"""
    <p>
        <b>{autor}</b><br>
        <i>{data}</i><br>
        {mensagem}
    </p>
    <hr>
    """)

print("""
</body>
</html>
""")