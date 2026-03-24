from html.parser import HTMLParser
import urllib.request

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.currentData = ""
        self.title = ""
        self.image = ""
    def handle_starttag(self, tag, attrs): 
        self.currentData = ""
        if tag =="img":
            for k, v in attrs:
                if k == "src":
                    self.image = v
    def handle_endtag(self, tag):
        if tag =="title":
            self.title = self.currentData
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
    parser = MyHTMLParser()
    parser.feed(str(page.read().decode('utf-8')))
    pages.append((parser.title,parser.image))
    
    with open("agregador.html", "w", encoding="utf-8") as file:

        file.write("""<!DOCTYPE html>
        <html>
            <head>
                <title>Agregador de Alunos - EXA618</title>
            </head>
            <body>
                <h1>Agregado de páginas de alunos - EXA618 Atividade 4</h1>
            <ul>
        """)

        for title,image in pages:

            file.write(f"""
            <li>
                <h2>{title}</h2>
                <img src="{image}">
            </li>
            """)

        file.write("""
             </ul>
            </body>
        </html>
            """)
    
    
