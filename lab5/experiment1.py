import smu

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()
v = linspace(-5, 0, 201)
f = open('experiment1DataB3.csv', 'w')
f.write('"Vg","Ic"\n')

s.set_voltage(2, -2)
for val in v:
    s.set_voltage(1, val)
    s.autorange(1)
    s.autorange(2)
    f.write('{!s},{!s}\n'.format(val, -1*s.get_current(2)))

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()

# Notes
# Result for nMOS: EKV Fit: {\it I}_s = 7.1652e-06A, {\it V}_T = 0.58447V, \kappa = 0.40639
