# import smu

# def linspace(initial, final, n = 100):
#     if n>=2:
#         increment = (float(final) - float(initial))/(n - 1)
#         return [float(initial) + i*increment for i in range(n)]
#     else:
#         return []

# s = smu.smu()

# # v2 = 2.5
# v1 = linspace(0, 5, 1001)
# f = open('experiment2DataB.csv', 'w')
# f.write('"Vout","Iout"\n')

# measurements = [[],[],[]]

# s.set_current(2, 0.)
# #s.set_autorange(1, 1)
# #s.set_autorange(2, 1)

# for val in v1:
#     s.set_voltage(1, val)
#     s.autorange(1)
#     f.write('{!s},{!s}\n'.format(val, s.get_current(1)))

# s.set_voltage(1, 0.)
# s.set_voltage(2, 0.)
# f.close()

# #Part A:
# #Vb = .545v
# #V1 1 = 3.5v
# #V2 1 = 3.5v

import smu

def linspace(initial, final, n = 100):
    if n>=2:
        increment = (float(final) - float(initial))/(n - 1)
        return [float(initial) + i*increment for i in range(n)]
    else:
        return []

s = smu.smu()

v1 = linspace(-1, 1, 1001)
f = open('experiment2DataC.csv', 'w')
f.write('"Vdm","Iout"\n')

measurements = [[],[],[]]

s.set_voltage(2, 1.73)
#s.set_autorange(1, 1)
#s.set_autorange(2, 1)

for val in v1:
    s.set_voltage(1, val)
    s.autorange(1)
    s.autorange(2)
    f.write('{!s},{!s}\n'.format(val, s.get_current(2)))

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()

#Part A:
#Vb = .545v
#V1 1 = 3.5v
#V2 1 = 3.5v

