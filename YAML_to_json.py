import yaml
import json
with open("file.json",'r') as yaml_in, open("file.json",'w') as json_out:
    yaml_data = yaml.safe_load(yaml_in)
    json.dump(yaml_data, json_out, indent=4)