import smu

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()
v = linspace(0, 1, 101)
f = open('experiment1Data.csv', 'w')
f.write('"Vbase","IbaseT1","IemitterT1","IbaseT2","IemitterT2","IbaseT3","IemitterT3","IbaseT4","IemitterT4",\n')

s.set_voltage(2, 0.)

measuredBase = [[],[],[], []]
measuredEmitter = [[],[],[], []]
for i in range(0, 4):
    raw_input("Press enter when ready to measure " + str(i + 1))
    for val in v:
        s.set_voltage(1, val)
        s.autorange(1)
        s.autorange(2)
        measuredBase[i] += [s.get_current(1)]
        measuredEmitter[i] += [s.get_current(2)]

for val in v:
    f.write('{!s},{!s},{!s},{!s},{!s},{!s},{!s},{!s},{!s}\n'.format(val, measuredBase[0].pop(0), measuredEmitter[0].pop(0), measuredBase[1].pop(0), measuredEmitter[1].pop(0), measuredBase[2].pop(0), measuredEmitter[2].pop(0), measuredBase[3].pop(0), measuredEmitter[3].pop(0)))

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()