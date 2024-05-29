incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

# Your code here
full_name = []
def data_transformer(list_data):
    return list(map(lambda element: f"{element['name']} {element['last_name']}", list_data))
#returns the list of mapping the lambda function to the list_data parameter
print(data_transformer(incoming_ajax_data))