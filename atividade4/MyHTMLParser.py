from html.parser import HTMLParser
import urllib.request
import urllib.parse

class MyHTMLParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.currentData = ""
        self.title = ""
        self.image = ""
        self.base_url = base_url

    def handle_starttag(self, tag, attrs):
        self.currentData = ""
        if tag == "img" and not self.image:
            for k, v in attrs:
                if k == "src":
                    self.image = urllib.parse.urljoin(self.base_url, v)

    def handle_endtag(self, tag):
        if tag == "title":
            self.title = self.currentData.strip()

    def handle_data(self, data):
        self.currentData += data


listURLS = []

with open("seeds.txt", "r", encoding="utf-8") as file:
    for linha in file:
        url = linha.strip()
        if url:
            listURLS.append(url)

pages = []

for url in listURLS:
    page = urllib.request.urlopen(url)
    html = page.read().decode("utf-8")
    parser = MyHTMLParser(url)
    parser.feed(html)
    pages.append((parser.title, parser.image))

with open("agregador.html", "w", encoding="utf-8") as file:
    file.write("""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Agregador de Alunos - EXA618</title>
<style>
body { font-family: Arial; padding: 40px; background:#f4f4f4; }
.grid { display:grid; grid-template-columns: repeat(auto-fill,minmax(250px,1fr)); gap:20px; }
.card { background:white; padding:15px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.1); text-align:center; }
img { max-width:100%; height:auto; border-radius:8px; }
</style>
</head>
<body>
<h1>Agregado de páginas de alunos - EXA618 Atividade 4</h1>
<div class="grid">
""")

    for title, image in pages:
        file.write(f"""
<div class="card">
<h2>{title}</h2>
<img src="{image}">
</div>
""")

    file.write("""
</div>
</body>
</html>
""")