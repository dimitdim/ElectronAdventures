import smu

s = smu.smu()
f = open('temp.csv', 'w')
f.write('"Iin"\n')

s.set_voltage(1, 0)
# s.set_current(1, 0)

while True:
    # s.set_current(1, .001)
    s.autorange(1)
    s.autorange(2)

    print s.get_current(1)
    # print s.get_voltage(1)

s.set_voltage(1, 0.)
f.close()