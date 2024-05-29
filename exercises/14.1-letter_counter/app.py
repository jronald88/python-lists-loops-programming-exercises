par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

# Your code here
lower_par = par.lower()
for letter in lower_par:
    if letter != " ": #ignore spaces
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1 #this starts the count
print(counts)
