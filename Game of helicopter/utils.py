from random import randint as rand

def randboll(r, mxr):
    t  = rand(0, mxr)
    return (t <= r )

def randcell(w, h):
    tw = rand(0, w-1)
    th = rand(0, h-1)
    return th, tw

def randneibre(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1), (1, 1), (-1,-1)]
    t = rand (0, 5)
    dx, dy = moves[t][0], moves[t][1]
    return (x+dx, y+dy)