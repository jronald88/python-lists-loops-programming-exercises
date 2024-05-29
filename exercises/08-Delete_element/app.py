people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    # Your code here
    new_list = list(people) #duplicates people into new_list
    if person_name in new_list:
        new_list.remove(person_name) #checks the new list for person_name and removes if necessary
    return new_list

    
# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))
