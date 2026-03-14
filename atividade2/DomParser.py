from xml.dom.minidom import parse

mapDocument = parse('./atividade2/map.xml')
#Formato CSV
print("Starting DOM Parser...")
isAmenity = False
currentName = ""
currentType = ""
for currentNode in mapDocument.getElementsByTagName("node"):
    
	tagNode = currentNode.getElementsByTagName("tag")
	isAmenity = False
	currentName = ""
	currentType = ""
 
	for tag in tagNode:
     
		if tag.getAttribute("k") == "amenity":
      
			currentType = tag.getAttribute("v")
			isAmenity = True
   
		if(isAmenity):
      
			if tag.getAttribute("k") == "name":
       
				currentName = tag.getAttribute("v")
    
			elif tag.getAttribute("k") == "type":
       
				currentType = tag.getAttribute("v")
				print("type:", currentType)
    
	if(isAmenity):
     
		print("Latitude:", currentNode.getAttribute("lat"))	
		print("Longitude:", currentNode.getAttribute("lon"))
		print("Nome:", currentName)
		print("Tipo:", currentType)

     