import smu

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()

# v2 = 2.5
v1 = linspace(0, 5.0, 501)
f = open('experiment1DataV2=4v5.csv', 'w')
f.write('"V1","Vout1"\n')

measurements = [[],[],[]]

s.set_current(2, 0.)
s.set_autorange(1, 1)
s.set_autorange(2, 1)

for val in v1:
    s.set_voltage(1, val)
    measurements[0] += [s.get_voltage(2)]

for val in v1:
    f.write('{!s},{!s}\n'.format(val, measurements[0].pop(0)))

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()


#Vb = .545v
#V2 1 = 2.5v
#V2 2 = 3.5v
#V2 3 = 4.5v

