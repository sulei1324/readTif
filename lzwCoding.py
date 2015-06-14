__author__ = 'Su Lei'

# d = {'1': '1', '2':  '2', '3': '3', '4':  '4'}
d = ['A', 'B', 'C', 'D']
r = 'AAAAAAAAAAAAA'

o = []

for i in xrange(len(r)):
    if i is 0:
        pre = ''
        suf = r[0]
    else:
        suf = r[i]
    print pre, suf
    if pre + suf in d:
        if i is len(r) - 1:
            o.append(d.index(pre + suf))
        else:
            pre += suf
    else:
        d.append(pre + suf)
        if i is len(r) - 1:
            o.append(d.index(pre))
            o.append(d.index(suf))
        else:
            o.append(d.index(pre))
            pre = suf


print o
print d

