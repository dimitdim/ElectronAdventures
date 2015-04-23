import smu
from subprocess import call

name='experiment3Data.csv'
run=2
neg=1

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()
v = linspace(0, .02, 501)
f = open(name, 'w')
f.write('"Iin","I1","I2"\n')

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)

measuredChannelCurrents = [[] for x in xrange(run+1)]
for i in range(0, run):
    raw_input("Press enter when ready to measure " + str(i + 1))
    for val in v:
        s.set_current(1, val)
        s.autorange(1)
        s.autorange(2)
        measuredChannelCurrents[i] += [((-1)**neg)*s.get_current(2)]

unf='{!s},'*(run)+'{!s}\n'
for val in v:
    f.write(unf.format(val, measuredChannelCurrents[0].pop(0), measuredChannelCurrents[1].pop(0)))

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()

call(['open',name])
