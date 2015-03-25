%% Experiment 1 A
clf;
semilogy(VA, IinA,'bd','LineWidth',1);
hold on;
semilogy(VinB, IB, 'ro','LineWidth',1);
plot(linspace(.3, .7, 100), 5E-14*(exp(35.465*linspace(.34, .71, 100))), 'go','LineWidth',1)
% y = 5E-14*e^35.465x
% R = .99165
xlabel('Volage (volts)');
ylabel('Current (Amps)');
legend('voltage-current characteristic', 'current-voltage characteristic', 'theoretical fit of current-voltage characteristic');

%% Experiment 1 B
clf;
loglog(IinA(5: 64), diff(VA(5:65)) ./ diff(IinA(5: 65)), 'bd');
hold on;
loglog(IinA(5: 64), 0.0282 ./ IinA(5: 64), 'ro');
xlabel('Current (Amps)');
ylabel('Incremental resistance (Ohms)');
title('Incremental Resistance of Diode');
legend('Experimental Incremental Resistance', 'Theoretical Incremental Resistance');
