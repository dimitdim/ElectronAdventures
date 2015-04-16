%% nMOS
clf;
% hold on;
loglog(IcN(2:end), diff(IcN) ./ diff(VgN), 'bo')
hold on;
loglog(IcN(2:35), 0.40639 .* (IcN(2:35)./.025), 'r-')
loglog(IcN(35: end), .40639*sqrt(IcN(35: end).*7.1652e-06)./.026, 'g-')
legend('incremental transconductance gain', 'weak inversion fit', 'strong inversion fit')
title('Incremental Transconductance Gain')
xlabel('Channel Current (I)')
ylabel('incremental transconductance gain (1/ohms)')

%% pMOS
clf;
% hold on;
loglog(IcP(2:end), -1*diff(IcP) ./ diff(VgP), 'bo')
hold on;
loglog(IcP(55:end), 0.7974 .* (IcP(55:end)./.025), 'r-')
loglog(IcP(1:55), 0.7974*sqrt(IcP(1: 55).*6.1023e-07)./.025, 'g-')
legend('incremental transconductance gain', 'weak inversion fit', 'strong inversion fit')
title('Incremental Transconductance Gain')
xlabel('Channel Current (I)')
ylabel('incremental transconductance gain (1/ohms)')
