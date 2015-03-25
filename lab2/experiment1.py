import smu
import numpy

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()
i = numpy.logspace(-8, -2, 71)
f = open('experiment1DataA.csv', 'w')
f.write('"Iin","V"\n')

for val in i:
    s.set_current(1, val)
    s.autorange(1)
    f.write('{!s},{!s}\n'.format(val, s.get_voltage(1)))

s.set_voltage(1, 0.)
f.close()

raw_input("Press enter when ready to start next part")

v = linspace(0, 1, 101)
f = open('experiment1DataB.csv', 'w')
f.write('"Vin","I"\n')

for val in v:
    s.set_voltage(1, val)
    s.autorange(1)
    f.write('{!s},{!s}\n'.format(val, s.get_current(1)))

s.set_voltage(1, 0.)
f.close()
