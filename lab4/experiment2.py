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
f = open('experiment2DataB.csv', 'w')
f.write('"Ix","Iz1","Iz2","Iz3"\n')

s.set_voltage(2, 0.)

measuredIz = [[],[],[]]
for i in range(0, 3):
    raw_input("Press enter when ready to measure " + str(i + 1))
    for val in Ixy:
        s.set_current(1, val*-1)
        s.autorange(1)
        s.autorange(2)
        measuredIz[i] += [s.get_current(2)]

for val in Ixy:
    f.write('{!s},{!s},{!s},{!s}\n'.format(val*-1, measuredIz[0].pop(0),measuredIz[1].pop(0),measuredIz[2].pop(0)))

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()

#Exp 2
# 1 Iy: .0025 A
# 2.04E-02