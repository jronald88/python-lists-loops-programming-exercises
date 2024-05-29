def lyrics_generator(lyrics):
    boom = "Boom "
    DtB = "Drop the bass "
    BtB = "!!!Break the bass!!! "
    beat = ""
    consecutive_count = 0
    for i in lyrics:
        if i == 0:
            beat += boom
            consecutive_count = 0
        elif i == 1:
            beat += DtB
            consecutive_count += 1
        else: 
            consecutive_count = 0
        if consecutive_count == 3:
            beat += BtB
    return beat

# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
