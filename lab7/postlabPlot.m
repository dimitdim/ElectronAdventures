clf;
hold on;
sampleRate = 1;

v225x = v11- 1.5;
v225Minus= I11 - I21;
v225Plus = I11 + I21;

plot(v225x(1:sampleRate:end), -1.*I11(1:sampleRate:end), 'bo')
plot(v225x(1:sampleRate:end), -1.*I21(1:sampleRate:end), 'b+')
plot(v225x(1:sampleRate:end), -1.*v225Minus(1:sampleRate:end), 'b*')
plot(v225x(1:sampleRate:end), -1.*v225Plus(1:sampleRate:end), 'bd')


v235x = v12 - 2.5;
v235Minus= I12 - I22;
v235Plus = I12 + I22;

plot(v235x(1:sampleRate:end), I12(1:sampleRate:end), 'ro')
plot(v235x(1:sampleRate:end), I22(1:sampleRate:end), 'r+')
plot(v235x(1:sampleRate:end), v235Minus(1:sampleRate:end), 'r*')
plot(v235x(1:sampleRate:end), v235Plus(1:sampleRate:end), 'rd')


v245x = v14 - 3.5;
v245Minus= I14 - I24;
v245Plus = I14 + I24;

plot(v245x(1:sampleRate:end), -1.*I14(1:sampleRate:end), 'go')
plot(v245x(1:sampleRate:end), -1.*I24(1:sampleRate:end), 'g+')
plot(v245x(1:sampleRate:end), -1.*v245Minus(1:sampleRate:end), 'g*')
plot(v245x(1:sampleRate:end), -1.*v245Plus(1:sampleRate:end), 'gd')


xlabel('V1-V2 (V)');
ylabel('I1, I2, I1-I2, I1+I2 (A)');
title('Current-Voltage Characteristics for 3 values of V2');
legend('I1 for V2=1.5V', 'I2 for V2=1.5V', 'I1-I2 for V2=1.5V', 'I1+I2 for V2=1.5V','I1 for V2=2.5V', 'I2 for V2=2.5V', 'I1-I2 for V2=2.5V', 'I1+I2 for V2=2.5V', 'I1 for V2=3.5V', 'I2 for V2=3.5V', 'I1-I2 for V2=3.5V', 'I1+I2 for V2=3.5V');

