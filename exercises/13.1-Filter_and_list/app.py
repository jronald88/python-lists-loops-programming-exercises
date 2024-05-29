all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here
def R_names(list):
    return list[0].lower() == "r"

resulting_names = list(filter(R_names, all_names))

print(resulting_names)




