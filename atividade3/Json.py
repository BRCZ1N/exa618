import json
import csv

with open('estabelecimentosSAX.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    id = 0
    featureList = []
    for row in reader:
        
        geometry = dict()
        geometry["type"] = "Point"
        geometry["coordinates"] = [
            float(row["lon"]),
            float(row["lat"])
        ]

        properties = dict()
        properties["nome"] = row["nome"]
        properties["tipo"] = row["tipo"]
        
        
        features = dict()
        features["type"] = "Feature"
        features["geometry"] = geometry
        features["properties"] = properties
        features["id"] = id
        id += 1
        featureList.append(features)
    
    dim = dict()
    dim["type"] = "FeatureCollection"
    dim["features"] = featureList
    jsonStr = json.dumps(dim, indent=4, ensure_ascii=False)
    objJson = json.loads(jsonStr)


with open('estabelecimentos.geojson', 'w', encoding='utf-8') as f:
    json.dump(objJson, f, indent=4, ensure_ascii=False)