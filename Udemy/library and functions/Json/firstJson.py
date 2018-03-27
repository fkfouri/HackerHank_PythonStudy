import json

data = {}
data['key'] = 'value'
json_data = json.dumps(data)

print(data)
print('-' * 50)
print(json_data)