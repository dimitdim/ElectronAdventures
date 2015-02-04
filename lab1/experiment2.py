import smu

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()
v = linspace(-5, 5, 101)
f = open('experiment2Data.csv', 'w')
f.write('"Vin","Vout"\n')

s.set_current(2, 0.)
for val in v:
    s.set_voltage(1, val)
    s.autorange(1)
    s.autorange(2)
    f.write('{!s},{!s}\n'.format(val, s.get_voltage(2)))

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()
