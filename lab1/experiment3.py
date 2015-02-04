import smu

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()
i = linspace(-.0001, .0001, 101)
f = open('experiment3Data.csv', 'w')
f.write('"Iin","Iout"\n')

s.set_voltage(2, 0.)
for val in i:
    s.set_current(1, val)
    s.autorange(1)
    s.autorange(2)
    f.write('{!s},{!s}\n'.format(val, s.get_current(2)))

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()