import xml.sax
import time

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.currentData = ""
    self.currentLat = ""
    self.currentLong = ""
    self.currentType = ""
    self.currentName = ""

  def startElement(self, tag, attributes):    
    self.currentData = ""
    if tag =="node":  
      self.currentLat = attributes.get("lat")
      self.currentLong = attributes.get("lon") 
      self.currentType = ""
      self.currentName = ""
    if tag =="tag":
      if attributes.get("k") == "amenity":
        self.currentType = attributes.get("v")  
      if attributes.get("k") == "name":  
        self.currentName = attributes.get("v")
      

  def endElement(self, tag):    
    if tag =="node" and self.currentType and self.currentName and self.currentLat and self.currentLong:
      print(self.currentLat)
      print(self.currentLong)
      print(self.currentType)
      print(self.currentName)
      file.write(f"{self.currentLat},{self.currentLong},{self.currentType},{self.currentName}\n")

  def characters(self, content):	
    self.currentData += content

parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

beginTime = time.perf_counter()
print("Starting SAX Parser...")
file = open("estabelecimentosSAX.csv", "w", encoding="utf-8")
file.write("lat,lon,tipo,nome\n")
parser.parse("map.xml")
endTime = time.perf_counter()
timeCount = endTime - beginTime
print("Tempo de execução: {:.2f} s" .format(timeCount))