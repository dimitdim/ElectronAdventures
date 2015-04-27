clf;
hold on;
sampleRate = 4;

v225x = V1forV20v5 - V2forV20v5;
v225Minus= I2forV20v5 - I1forV20v5;
v225Plus = I1forV20v5 + I2forV20v5;

plot(v225x(1:sampleRate:end), I1forV20v5(1:sampleRate:end), 'bo')
plot(v225x(1:sampleRate:end), I2forV20v5(1:sampleRate:end), 'b+')
plot(v225x(1:sampleRate:end), v225Minus(1:sampleRate:end), 'b*')
plot(v225x(1:sampleRate:end), v225Plus(1:sampleRate:end), 'bd')


v235x = V1forV21v5 - V2forV21v5;
v235Minus= I1forV21v5 - I2forV21v5;
v235Plus = I1forV21v5 + I2forV21v5;

plot(v235x(1:sampleRate:end), I1forV21v5(1:sampleRate:end), 'ro')
plot(v235x(1:sampleRate:end), I2forV21v5(1:sampleRate:end), 'r+')
plot(v235x(1:sampleRate:end), v235Minus(1:sampleRate:end), 'r*')
plot(v235x(1:sampleRate:end), v235Plus(1:sampleRate:end), 'rd')


v245x = V1forV22v5-V2forV22v5;
v245Minus= I2forV22v5 - I1forV22v5;
v245Plus = I1forV22v5+ I2forV22v5;

plot(v245x(1:sampleRate:end), I1forV22v5(1:sampleRate:end), 'go')
plot(v245x(1:sampleRate:end), I2forV22v5(1:sampleRate:end), 'g+')
plot(v245x(1:sampleRate:end), v245Minus(1:sampleRate:end), 'g*')
plot(v245x(1:sampleRate:end), v245Plus(1:sampleRate:end), 'gd')


xlabel('V1-V2 (V)');
ylabel('I1, I2, I1-I2, I1+I2 (A)');
title('Current-Voltage Characteristics for 3 values of V2');
legend('I1 for V2=0.5V', 'I2 for V2=0.5V', 'I1-I2 for V2=0.5V', 'I1+I2 for V2=0.5V','I1 for V2=1.5V', 'I2 for V2=1.5V', 'I1-I2 for V2=1.5V', 'I1+I2 for V2=1.5V', 'I1 for V2=2.5V', 'I2 for V2=2.5V', 'I1-I2 for V2=2.5V', 'I1+I2 for V2=2.5V');

