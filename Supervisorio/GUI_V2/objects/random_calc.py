Ku1 = 0.2
Ku2 = 0.2
Kx1 = -0.05
Kx2 = -.2
Td = 5

p1 = 1/(Ku1*Td)
i1 = -Kx1/(Ku1*Td)
p2 = 1/(Ku2*Td)
i2 = -Kx2/(Ku2*Td)

print('C1(s) = {:.3f} + {:.3f}/s'.format(p1, i1))
print('C2(s) = {:.3f} + {:.3f}/s'.format(p2, i2))
exit()





























Ea = 3361.5
ra = 0.05
aa = 0.09
ba = -30.1535
Eb = 1947.5357
rb = 0.05
ab = -0.09
bb = 31.2535

e = 2.7183
R = 8.314462

Cf = 0
Cn = 0
Ca0 = 10
T = 55+273
dt = 0.001
t = 0

print(-Ea*(aa*T+ba)/(R*T))

vca = []
vcn = []
vcf = []
vt = []
while t < 40:
	Ca = Ca0 - Cf - Cn
	Cf = Cf + (ra*pow(e,(-Ea*(aa*T+ba)/(R*T)))*Ca)*dt
	Cn = Cn + (rb*pow(e,(-Eb*(ab*T+bb)/(R*T)))*Ca)*dt

	vca.append(Ca)
	vcf.append(Cf)
	vcn.append(Cn)
	vt.append(t)

	print(Cf)

	t = t + dt

plt.plot(vt, vca, label='Ca(t)')
plt.plot(vt, vcf, label='Cf(t)')
plt.plot(vt, vcn, label='Cn(t)')
plt.legend()
plt.show()