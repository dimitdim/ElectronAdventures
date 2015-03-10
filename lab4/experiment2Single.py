import smu
import numpy

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()
Ixy = numpy.logspace(-8, -2, 200)
f = open('experiment2DataA5.csv', 'w')
f.write('"Ix","Iz"\n')

s.set_voltage(2, 5.)

for val in Ixy:
    s.set_current(1, val)
    s.autorange(1)
    s.autorange(2)
    f.write('{!s},{!s}\n'.format(val, s.get_current(2)))


s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()

#Exp 2
# 1 Iy: .0025 A
# 2 .04E-02
# Vin: .205 V 