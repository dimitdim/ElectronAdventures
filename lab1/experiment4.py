import smu

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()
v = linspace(-5, 5, 101)
f = open('experiment4Data.csv', 'w')
f.write('"Vin","V1","V2","V3","V4"\n')
s.set_current(2, 0.)

measuredVoltage = [[],[],[],[]];
for i in range(0, 4):
    raw_input("Press enter when ready to measure " + str(i + 1))
    for val in v:
        s.set_voltage(1, val)
        s.autorange(1)
        s.autorange(2)
        measuredVoltage[i] += [s.get_voltage(2)]

for val in v:
    f.write('{!s},{!s},{!s},{!s},{!s}\n'.format(val, measuredVoltage[0].pop(0), measuredVoltage[1].pop(0), measuredVoltage[2].pop(0), measuredVoltage[3].pop(0)))

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()