import smu

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()
v = linspace(0, 5, 101)
f = open('experiment2Data.csv', 'w')
f.write('"Vbase","IbaseR1","IemitterR1","IbaseR2","IemitterR2","IbaseR3","IemitterR3"\n')

s.set_voltage(2, 0.)

measuredBaseCurrents = [[],[],[]]
measuredEmitterCurrents = [[],[],[]]
for i in range(0, 3):
    raw_input("Press enter when ready to measure " + str(i + 1))
    for val in v:
        s.set_voltage(1, val)
        s.autorange(1)
        s.autorange(2)
        measuredBaseCurrents[i] += [s.get_current(1)]
        measuredEmitterCurrents[i] += [s.get_current(2)]

for val in v:
    f.write('{!s},{!s},{!s},{!s},{!s},{!s},{!s}\n'.format(val, measuredBaseCurrents[0].pop(0),measuredEmitterCurrents[0].pop(0), measuredBaseCurrents[1].pop(0),measuredEmitterCurrents[1].pop(0), measuredBaseCurrents[2].pop(0), measuredEmitterCurrents[2].pop(0)))

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()