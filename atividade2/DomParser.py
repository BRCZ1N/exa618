from xml.dom.minidom import parse
import time

beginTime = time.perf_counter()
mapDocument = parse('map.xml')
#Formato CSV
print("Starting DOM Parser...")
isAmenity = False
currentName = ""
currentType = ""
file = open("estabelecimentosDOM.csv", "w", encoding="utf-8")
file.write("lat,lon,tipo,nome\n")
cont = 1
for currentNode in mapDocument.getElementsByTagName("node"):
    
	tagNode = currentNode.getElementsByTagName("tag")
	isAmenity = False
	currentName = ""
	currentType = ""
 
	for tag in tagNode:
     
		if tag.getAttribute("k") == "amenity":
      
			currentType = tag.getAttribute("v")
			isAmenity = True

		if isAmenity and tag.getAttribute("k") == "name":
       
				currentName = tag.getAttribute("v") 
    
	if(currentType and currentName):
     
		print("Latitude:", currentNode.getAttribute("lat"))	
		print("Longitude:", currentNode.getAttribute("lon"))
		print("Nome:", currentName)
		print("Tipo:", currentType)
		file.write(f"{currentNode.getAttribute("lat")},{currentNode.getAttribute("lon")},{currentName},{currentType}\n")
endTime = time.perf_counter()
timeCount = endTime - beginTime
print("Tempo de execução: {:.2f} s" .format(timeCount))


     