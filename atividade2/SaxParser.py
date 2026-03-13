import xml.sax

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.currentData = ""
    self.clientId = ""

  def startElement(self, tag, attributes):    
    self.currentData = ""
    
    if tag =="Cliente":  
      self.clientId = attributes.get("id")  

  def endElement(self, tag):    
    if tag =="nome":	
      print("Nome:", self.currentData) 
      print("id:", self.clientId) 

  def characters(self, content):	
    self.currentData += content

parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("Banco.xml")