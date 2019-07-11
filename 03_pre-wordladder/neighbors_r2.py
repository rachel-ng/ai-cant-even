#!/usr/bin/python
import sys

def neighbors (in_f, out_f):
    try:
        i_file = open(in_f,"r")
        input_f = [line.rstrip() for line in i_file]
        i_file.close()

        lngth = len(input_f[0])
        ln = range(lngth)

        fin = open("dictall.txt","r")
        d_file = [i for i in fin.read().split("\n") if i != "" and len(i) == lngth]
        #dct = dict([[i, []] for i in d_file])

        fin.close()

        d = dict([])
        for word in d_file:
            for i in ln:
                s = word[:i] + "_" + word[i+1:]
                d[s] = d.get(s, []) + [word]

        dct = dict([])
        for word in d_file:
            for i in ln:
                s = word[:i] + "_" + word[i+1:]
                dct[word] =  dct.get(word, []) + d[s]
            dct[word] = set(dct.get(word, []))

        s = ""
        for i in input_f:
            s += i + "," + str(len(dct[i] - set([i]))) + "\n"

        o_file = open(out_f, "w+")
        o_file.write(s)
        o_file.close()

    except FileNotFoundError:
        print("so uh, " + in_f + " don't exist broski")

if __name__ == "__main__":
    neighbors(sys.argv[1], sys.argv[2])


    #python3 neighbors_r2.py  harry.txt  answers.txt
