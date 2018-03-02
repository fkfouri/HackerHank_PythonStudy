'''
Formatos de dados permitidos no Json
Number, string, Null, true/false, Object, Array

que podem ser transformado nos seguintes tipo de dados no Python respectivamente
int/float, str, None, True/False, dict, list

Biblioteca chamada json
json.load(<str>): converte um string JSON em um objeto python (Deserializacao)

json.dumps(<python_object>): converte um objeto python em uma string JSON (Serializacao)
'''

import json
data_string = '[{"b": [2, 4], "c": 3.0, "a": "A"}]'
python_data = json.loads(data_string)
print(python_data)