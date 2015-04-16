clf;
hold on;
sampleRate = 4;

v225x = V1forv225-V2forV225;
v225Minus= I1forV225V - I2forV225;
v225Plus = I1forV225V + I2forV225;

plot(v225x(1:sampleRate:end), I2forV225(1:sampleRate:end), 'bo')
plot(v225x(1:sampleRate:end), I1forV225V(1:sampleRate:end), 'b+')
plot(v225x(1:sampleRate:end), v225Minus(1:sampleRate:end), 'b*')
plot(v225x(1:sampleRate:end), v225Plus(1:sampleRate:end), 'bd')


v235x = V1forv235-V2forV235;
v235Minus= I1forV235 - I2forV235;
v235Plus = I1forV235 + I2forV235;

plot(v235x(1:sampleRate:end), I2forV235(1:sampleRate:end), 'ro')
plot(v235x(1:sampleRate:end), I1forV235(1:sampleRate:end), 'r+')
plot(v235x(1:sampleRate:end), v235Minus(1:sampleRate:end), 'r*')
plot(v235x(1:sampleRate:end), v235Plus(1:sampleRate:end), 'rd')


v245x = V1forv245-V2forV245;
v245Minus= I1forV245 - I2forV245;
v245Plus = I1forV245 + I2forV245;

plot(v245x(1:sampleRate:end), I2forV245(1:sampleRate:end), 'go')
plot(v245x(1:sampleRate:end), I1forV245(1:sampleRate:end), 'g+')
plot(v245x(1:sampleRate:end), v245Minus(1:sampleRate:end), 'g*')
plot(v245x(1:sampleRate:end), v245Plus(1:sampleRate:end), 'gd')


xlabel('V1-V2 (V)')
ylabel('I1, I2, I1-I2, I1+I2 (A)')
title('Current-Voltage Characteristics for 3 values of V2')
legend('I1 for V2=2.5V', 'I2 for V2=2.5V', 'I1-I2 for V2=2.5V', 'I1+I2 for V2=2.5V','I1 for V2=3.5V', 'I2 for V2=3.5V', 'I1-I2 for V2=3.5V', 'I1+I2 for V2=3.5V','I1 for V2=4.5V', 'I2 for V2=4.5V', 'I1-I2 for V2=4.5V', 'I1+I2 for V2=4.5V')


