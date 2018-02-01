
def replace(test_string, replace_string):
    cursor = test_string.find(replace_string)
    size = len(replace_string)

    #transform string to list
    transformed_string = list(test_string)

    #remove part from string
    for i in range(cursor, cursor + size):
        transformed_string.pop(cursor)

    changeString = list('bodega')
    for i in range(0, len(changeString)):
        transformed_string.insert(cursor + i, changeString[i])


    return ''.join(transformed_string)

print(replace('Hi how are you?','how'))