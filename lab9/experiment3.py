import smu

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()

# v2 = 2.5
v1 = linspace(0, 5.0, 501)
f = open('experiment3DataB.csv', 'w')
f.write('"Vin","Vout"\n')

s.set_current(2, 0.)
s.set_autorange(1, 1)
s.set_autorange(2, 1)

for val in v1:
    s.set_voltage(1, val)
    f.write('{!s},{!s}\n'.format(val, ))


s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()

