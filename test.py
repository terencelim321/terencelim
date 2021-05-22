import json

with open("app.php","rb") as f:
    jsonData = json.loads(f.read())

for key,value in jsonData['numbers'].items():
    if key == 'number1':
        x = value
    else:
        y = value
        
print( x + y)