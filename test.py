



v = [1, 2, 3, 4, 5, 6,0, ]
s = [-33.44, 24.3, 1234.44, 234.5, 444.333, -1.0, -33.55, ]
def comp(a, b):
    vala = s[a]
    valb = s[b]
    print "val a, b", vala, valb    
    return cmp(vala, valb)
    # if vala > valb: return 1
    # elif vala == valb : return 0
    # else : return -1




# v.sort(cmp = comp)
# sorted( v, cmp = comp)

v = sorted(v, comp)
print v