import objectpath
import json

def lambda_handler(event, context):
    with open('/opt/data/aws-regions.json', 'r') as f:
        regionsObject = json.load(f)
    
    obTree = objectpath.Tree(regionsObject)

    sydneyObject = obTree.execute('$.sydney')

    return sydneyObject