import smu
from subprocess import call

name='experiment2Data.csv'
run=6
neg=0

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()
v = linspace(0, 5, 501)
f = open(name, 'w')
f.write('"VGate","I_10_Single","I_dd_Single","I_10_Series","I_dd_Series","I_10_Paralle","I_dd_Parallel"\n')

s.set_voltage(2, 0.)

measuredChannelCurrents = [[] for x in xrange(run+1)]
for i in range(0, 3):
    raw_input("Press enter when ready to measure " + str(i + 1))
    s.set_voltage(2, 0.010)
    for val in v:
        s.set_voltage(1, val)
        s.autorange(1)
        s.autorange(2)
        measuredChannelCurrents[2*i] += [((-1)**neg)*s.get_current(2)]
    s.set_voltage(2, 5.)
    for val in v:
        s.set_voltage(1, val)
        s.autorange(1)
        s.autorange(2)
        measuredChannelCurrents[2*i+1] += [((-1)**neg)*s.get_current(2)]

unf='{!s},'*(run)+'{!s}\n'
for val in v:
    f.write(unf.format(val, measuredChannelCurrents[0].pop(0), measuredChannelCurrents[1].pop(0), measuredChannelCurrents[2].pop(0), measuredChannelCurrents[3].pop(0), measuredChannelCurrents[4].pop(0), measuredChannelCurrents[5].pop(0)))

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()

call(['open',name])
