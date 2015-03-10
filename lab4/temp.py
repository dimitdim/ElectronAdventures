import smu

s = smu.smu()
f = open('temp.csv', 'w')
f.write('"Iin"\n')

s.set_voltage(1, 0)

while True:
    print s.get_current(1)

s.set_voltage(1, 0.)
f.close()