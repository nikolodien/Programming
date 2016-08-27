#!/usr/bin/python

# Instead of comparing strings, we can assign an integer to each color as follows
# black     1
# blue      2
# red       3
# green     4
# yellow    5
# orange    6

def colorMapper(string):
    if string=="black":
        return 1
    elif string=="blue":
        return 2
    elif string=="red":
        return 3
    elif string=="green":
        return 4
    elif string=="yellow":
        return 5
    else: # string=="orange"
        return 6

T=input()

for i in range(1,T+1):
    colors=map(colorMapper,raw_input().split(" "))
    # The answer will be true if two of front,back,left, and right have the same color
    # and one of top or bottom have that color too
    count,bother={},False
    for color in colors:
        if color in count:
            count[color] = count[color]+1
        else:
            count[color] = 1
        if count[color]==3:
            bother= not bother
            break
    if not bother:
        print "NO"
    else:
        match = lambda x: x==color
        mappedColors = map(match,colors)
        hr0 = mappedColors[0]+mappedColors[2]
        hr1 = mappedColors[0]+mappedColors[3]
        hr2 = mappedColors[1]+mappedColors[2]
        hr3 = mappedColors[1]+mappedColors[3]
        vr = mappedColors[4]+mappedColors[5]
        if (hr0==2 or hr1==2 or hr2==2 or hr3==2) and vr>=1:
            print "YES"
        else:
            print "NO"
