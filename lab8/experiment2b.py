import smu

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()

v2 = 2.5
v1 = linspace(v2-.2, v2+.2, 501)
f = open('experiment2DataA.csv', 'w')
f.write('"Vout",""\n')

s.set_current(2, 0.)
for val in v1:
    s.set_voltage(1, val)
    s.autorange(1)
    s.autorange(2)
    f.write('{!s},{!s}\n'.format(val, -1*measurements[0].pop(0)))
    measurements[0] += [s.get_voltage(2)]

for val in v1:
    

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()
