#!/usr/bin/python3
import sys

genre = dict()
inp_name = sys.argv[1]
out_name = sys.argv[2]

with open(inp_name,'r') as f:
    for line in f:
        nline = line.rstrip('\n')
        full = nline.rfind('::')
        full2  = nline[full + 2:]
        gen = full2.split('|')
        for i in gen:
            if i not in genre:
                genre[i] = 1
            else:
                genre[i] += 1

with open(out_name,'w') as out:
    for i, j in genre.items():
        out.write("{} {}\n".format(i,j))
            
