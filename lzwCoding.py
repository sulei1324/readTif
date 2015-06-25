__author__ = 'Su Lei'

# d = {'1': '1', '2':  '2', '3': '3', '4':  '4'}
d = [str(x) for x in xrange(258)]
r = ['255'] * 9
s = '256'
e = '257'

o = []

for i in xrange(len(r)):
    if i is 0:
        o.append(d.index(s))
        pre = ''
        suf = r[0]
    else:
        suf = r[i]
    if pre + suf in d:
        if i is len(r) - 1:
            o.append(d.index(pre + suf))
            o.append(d.index(e))
        else:
            pre += suf
    else:
        d.append(pre + suf)
        if i is len(r) - 1:
            o.append(d.index(pre))
            o.append(d.index(suf))
            o.append(d.index(e))
        else:
            o.append(d.index(pre))
            pre = suf


print o
obs = ''
for i in o:
    tmp = bin(i)[2::]
    if len(tmp) is not 9:
        nt = 9 - len(tmp)
        tmp += '0' * nt
    obs += tmp

if len(obs) % 8 is not 0:
    n = len(obs) / 8
    m = 8 * (n + 1) - len(obs)
    obs += '0' * m

y = [hex(int(obs[i: i + 8], 2)) for i in xrange(0, len(obs), 8)]
print [obs[i: i + 8] for i in xrange(0, len(obs), 8)]
print y

