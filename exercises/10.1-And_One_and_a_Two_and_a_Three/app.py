contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}

# Your code here
for item in contact.keys():
    print(item + ": " + contact.get(item))
    #print(f"{item}: {contact[item]}")