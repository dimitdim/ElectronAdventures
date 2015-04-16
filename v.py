import smu

s=smu.smu()

s.set_current(1,0.)
s.set_current(2,0.)
s.set_autorange(1,1)
s.set_autorange(2,1)
while True:
    print str(s.get_voltage(1))+' : '+str(s.get_voltage(2))
