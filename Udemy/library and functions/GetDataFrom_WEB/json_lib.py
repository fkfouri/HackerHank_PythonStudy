'''
Formatos de dados permitidos no Json
Number, string, Null, true/false, Object, Array

que podem ser transformado nos seguintes tipo de dados no Python respectivamente
int/float, str, None, True/False, dict, list

Biblioteca chamada json
json.load(<str>): converte um string JSON em um objeto python (Deserializacao)

json.dumps(<python_object>): converte um objeto python em uma string JSON (Serializacao)
'''

import json, requests
data_string = '[{"b": [2, 4], "c": 3.0, "a": "A"}]'
#dir(json)
python_data = json.loads(data_string)
print(python_data, python_data[0]['c'], '=> Convert a string em Objeto Python (DESERIALIZACAO)')

return_strign = json.dumps(python_data)
print(return_strign, '=> Convert objeto Python em String (SERIALIZACAO)')





#Obtendo json via request
address="Columbia University, New York, NY"
url="https://maps.googleapis.com/maps/api/geocode/json?address=%s" % (address)
response = requests.get(url).json()
print(requests.get(url))
print(40 * '*')
print(type(response), response)


print(40 * '*')
y=json.loads('[[{"equity":[{"ticker":"AAPL", "value":139.78, "change": "+0.59%"}],"option":[{"ticker":"AAPLOCT17120","value":21.22,"change":"-2.4%"}]}]]')

print(y[0][0]['option'][0]['value'])