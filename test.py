def calculate_match(person1: dict, person2: dict) -> bool:
    
    #artist compatability
    art1 = person1["top 5 artists"]
    art2 = person2["top 5 artists"]
    art  = 0.4 * len(set(art1) & set(art2))

    #genre compatability
    gen1 = person1["top 5 genres"]
    gen2 = person2["top 5 genres"]
    gen = 0.3 * len(set(gen2) & set(gen2))

    #song preferences
    song1 = person1["top 10 songs"]
    song2 = person2["top 10 songs"]
    song = 0.2 * 0.5 * len(set(song1) & set(song2))

    #album preferences
    alb1 = person1["top 5 albums"]
    alb2 = person2["top 5 albums"]
    alb = 0.1 * len(set(alb1) & alb(2))

    #calculate score
    score = art + gen + song + alb

    returnValue = False

    if score >= 1:
        returnValue = True

    return returnValue








