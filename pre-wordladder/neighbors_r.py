#!/usr/bin/python
import sys
from datetime import datetime

def neighbors (in_f, out_f):
    try:
        i_file = open(in_f,"r")
        input_f = [line.rstrip() for line in i_file]
        i_file.close()

        lngth = len(input_f[0])
        ln = range(lngth)

        fin = open("dictall.txt","r")
        d_file = [i for i in fin.read().split("\n") if i != "" and len(i) == lngth]
        fin.close()

        d = dict([])
        for word in d_file:
            for i in ln:
                s = word[:i] + "_" + word[i+1:]
                d[s] = d.get(s, []) + [word]

        dct = dict([])
        for word in d_file:
            s = word[:i] + "_" + word[i+1:]
            dct[word] = list(set.union(*[set(d[s]) for i in ln]) - set([word]))

        s = ""
        for i in input_f:
            s += i + "," + str(len(dct[i])) + "\n"

        o_file = open(out_f, "w+")
        o_file.write(s)
        o_file.close()

    except FileNotFoundError:
        print("so uh, " + in_f + " don't exist broski")

if __name__ == "__main__":
    start = datetime.now()
    neighbors(sys.argv[1], sys.argv[2])
    print((datetime.now()-start).microseconds / 1000000)


    #python3 neighbors_d.py  harry.txt  answers.txt
