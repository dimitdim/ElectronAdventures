import smu

s = smu.smu()

s.set_current(1, 0.)
s.set_autorange(1,1)

while True:
	print s.get_voltage(1)