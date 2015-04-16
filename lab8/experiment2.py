import smu

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

# s = smu.smu()

# #For a single value of V2, sweep V1 around V2 in fine increments while measuring Vout. 
# v2 = 3.5
# v1 = linspace(-.3, .3, 501)
# f = open('experiment2DataA.csv', 'w')
# f.write('"V1","Vout"\n')

# s.set_current(2, 0.)
# s.set_autorange(1, 1)
# s.set_autorange(2, 1)

# for val in v1:
#     s.set_voltage(1, val)
#     f.write('{!s},{!s}\n'.format(val, s.get_voltage(2)))

# s.set_voltage(1, 0.)
# s.set_voltage(2, 0.)
# f.close()

#V2 = 3.5



####B 
# s = smu.smu()

# #For a single value of V2, sweep V1 around V2 in fine increments while measuring Vout. 
# v1 = linspace(0, 5, 501)
# f = open('experiment2DataB.csv', 'w')
# f.write('"V1","Vout"\n')

# s.set_autorange(1, 1)

# for val in v1:
#     s.set_voltage(1, val)
#     f.write('{!s},{!s}\n'.format(val, s.get_current(1)))

# s.set_voltage(1, 0.)
# s.set_voltage(2, 0.)
# f.close()

#V2 = V1 = 3.5


####C (finally)
s = smu.smu()

v1 = linspace(-.1, .1, 501)
f = open('experiment2DataC.csv', 'w')
f.write('"V1","Vout"\n')

s.set_voltage(2, 3.5)
s.set_current(1, 0.)
s.set_autorange(1, 1)
s.set_autorange(2, 1)

for val in v1:
    s.set_voltage(1, val)
    f.write('{!s},{!s}\n'.format(val, s.get_current(2)))

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()

