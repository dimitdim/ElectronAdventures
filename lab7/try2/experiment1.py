import smu

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()

v2 = 2.5
v1 = linspace(v2-0.5, v2+0.5, 501)
f = open('experiment1DataV2=2v5.csv', 'w')
f.write('"V1","V2","I1","I2","V"\n')

measurements = [[],[],[]]

#First two current measurements
s.set_voltage(2, 0.)
for i in range(0, 2):
    raw_input("Press enter when ready to measure " + str(i + 1))
    for val in v1:
        s.set_voltage(1, val)
        s.autorange(1)
        s.autorange(2)
        measurements[i] += [-s.get_current(2)]

#Measure V
raw_input("Press enter when ready to measure " + str(2 + 1))
s.set_current(2, 0.)
for val in v1:
    s.set_voltage(1, val)
    s.autorange(1)
    s.autorange(2)
    measurements[2] += [s.get_voltage(2)]

for val in v1:
    f.write('{!s},{!s},{!s},{!s},{!s}\n'.format(val, v2, measurements[0].pop(0), measurements[1].pop(0), measurements[2].pop(0)))

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()

#Vb = .65
