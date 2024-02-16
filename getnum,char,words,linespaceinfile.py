def count(mca2):
    nw=0
    nch=0
    nl=0
    with open(mca2,'r') as mca2:
        for line in mca2:
            wl=line.split()
            nl+=1
            nw+=len(wl)
            nch+=len(line)
    print("words:",nw)
    print("lines:",nl)
    print("character:",nch)
        
