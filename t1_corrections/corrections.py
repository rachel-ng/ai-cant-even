# 1 -- committee_sort.py

#!/usr/bin/python3
import sys

def committee (in_f, out_f):
    c_f = open(in_f,"r")
    c =[[a for a in i.strip("\n").split(",") if a != ""] for i in c_f.readlines()]
    c.sort(key = lambda x: x[0])
    com = ""
    for i in c:
        if len(i) > 1:
            s = "" + i[0]
            n = i[1:]
            n.sort()
            for x in n:
                s += ", " + x
            com += s + "\n"

    o_f = open(out_f,"w+")
    o_f.write(com)
if __name__ == "__main__":
    committee(sys.argv[1], sys.argv[2])
