inp = open('in.txt', 'w+')
out = open('out.txt', 'w+')

def input():
    return inp.readline()

def print(v):
    out.write(str(v))
