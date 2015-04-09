import smu

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()
v = linspace(0, 5, 101)
f = open('experiment2DataA.csv', 'w')
f.write('"Vs","Ic"\n')

for val in v:
    s.set_voltage(1, val)
    s.autorange(1)
    f.write('{!s},{!s}\n'.format(val, -1*s.get_current(1)))

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()           
