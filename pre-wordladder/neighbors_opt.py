#!/usr/bin/python
import sys
from datetime import datetime

def neighbors (in_f, out_f):
    try:
        i_file = open(in_f,"r")
        input_f = [line.rstrip() for line in i_file]
        i_file.close()
        lngth = len(input_f[0])

        fin = open("dictall.txt","r")
        d_file = [i for i in fin.read().split("\n") if i != "" and len(i) == lngth]
        fin.close()
        place = [dict([[i, set([])] for i in "abcdefghijklmnopqrstuvwxyz"]) for x in range(lngth)]
        dct = dict([[i, []] for i in d_file])

        for i in d_file:
            n = 0
            for p in i:
                place[n][p].add(i)
                n += 1

        avg = 0
        avg2 = 0
        for i in d_file:
            start = datetime.now()
            places = [place[n][p] for n,p in enumerate(i,0)]
            end = (datetime.now()-start).microseconds
            avg += end

            start = datetime.now()
            dct[i] = set.union(*[set.intersection(*[k for k in places if k != j]) for j in places]) - set([i])
            end = (datetime.now()-start).microseconds
            avg2 += end

        print((avg + avg2)/1000000)
        print(avg/len(dct))
        print(avg2/len(dct))

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


    #python3 neighbors.py  harry.txt  answers.txt
