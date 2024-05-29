chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
    # Your code here
    merged_list = []
    for i in list1:
        merged_list.append(i)
    for j in list2:
        merged_list.append(j)
    return merged_list
    
print(merge_list(chunk_one, chunk_two))
