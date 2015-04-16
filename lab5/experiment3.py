import smu

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()
v = linspace(-5, 0, 101)
f = open('experiment3pMOSData-5V.csv', 'w')
f.write('"Vd","Ic"\n')

s.set_voltage(2, -5)
s.autorange(2)
for val in v:
    s.set_voltage(1, val)
    s.autorange(1)
    f.write('{!s},{!s}\n'.format(val, s.get_current(1)))

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()

#nMOS
#Weak inversion: .45V
#Moderate inversion: .6V
#Strong inversion: gate voltage set to 5V


#pMOS
#weak inversion: -.5V
#moderate inversion: -.65V
#strong inversion: -5V