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
f.write('"Vin","R1I","R1V","R2I","R2V","R3I","R3V","R4I","R4V"\n')

s.set_current(2, 0.)

measuredCurrents = [[],[],[],[]]
measuredVoltages = [[],[],[],[]]
for i in range(0, 4):
    raw_input("Press enter when ready to measure " + str(i + 1) + " resistor")
    for val in v:
        s.set_voltage(1, val)
        s.autorange(1)
        s.autorange(2)
        measuredCurrents[i] += [s.get_current(1)]
        measuredVoltages[i] += [s.get_voltage(2)]

for val in v:
    f.write('{!s},{!s},{!s},{!s},{!s},{!s},{!s},{!s},{!s}\n'.format(val, measuredCurrents[0].pop(0), measuredVoltages[0].pop(0), measuredCurrents[1].pop(0), measuredVoltages[1].pop(0),measuredCurrents[2].pop(0), measuredVoltages[2].pop(0), measuredCurrents[3].pop(0), measuredVoltages[3].pop(0)))

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()