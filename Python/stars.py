def draw_stars(arr) :
    for obj in arr :
        if isinstance(obj, int) :
            print "*" * obj
        else :
            print obj[0].lower() * len(obj)


x = [4, 6, 1, 3, 5, 7, 25]
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(x)