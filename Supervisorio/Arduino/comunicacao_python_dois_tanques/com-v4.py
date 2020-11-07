import serial
from time import sleep, time

from matplotlib.pyplot import figure, close
from numpy import linspace, array, hstack

delta_time = []

ser = serial.Serial('/dev/ttyUSB0', 9600)  # Establish the connection on a specific port

nsim = 50

v1 = array([0.0]*10)
v1 = hstack((v1,[3]*40))
v2 = array([0.0]*10)
v2 = hstack((v2,[0]*40))

h1 = []
h2 = []
v1_ = []
v2_ = []

Ts = 1.056

tempo = linspace(0,nsim*Ts,nsim)
x = ser.readline()

#ser.write(bytearray('{:.5f}&{:.3f}&{:.3f}T'.format(14.5, 3.,Ts), 'ASCII'))

# while x!=1:
#     x = ser.readline()
print(x)

for it in range(nsim):
    ser.write(bytearray('{:.2f}&{:.2f}T'.format(v1[it],v2[it]),'ASCII'))
    start = time()
    x = ser.readline().decode("utf-8")
    end = time()
    print(x)
    data = x.split('&')
    h1.append(float(data[0]))
    h2.append(float(data[1]))
    v1_.append(float(data[2]))
    v2_.append(float(data[3]))
    delta_time.append(start-end)

    fig = figure(figsize=(4,8))
    ax = fig.add_subplot(2, 1, 1)
    ax.plot([0, 0, 0, 0], [0, 30. / 4, 2 * 30. / 4, 30], 'k-', [1, 1, 1, 1], [0, 30. / 4, 2 * 30. / 4, 30], 'k-')
    ax.plot([0, 1],[float(data[1]), float(data[1])],'b-')
    ax.set_ylabel('h2')
    ax.set_ylim(0,10)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(True)
    ax.tick_params(axis=u'y',length=0)
    ax = fig.add_subplot(2, 1, 2)
    ax.plot([0, 0, 0, 0], [0, 30. / 4, 2 * 30. / 4, 30], 'k-',[1, 1, 1, 1], [0, 30. / 4, 2 * 30. / 4, 30], 'k-')
    ax.plot([0, 1], [float(data[0]), float(data[0])], 'b-')
    ax.set_ylabel('h1')
    ax.set_ylim(0,10)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(True)
    fig.show()
    close()

ser.close()

fig = figure()
axes = fig.add_subplot(4,1,1)
axes.plot(tempo,h2,'.-')
axes.set_ylabel('h2')
axes = fig.add_subplot(4,1,2)
axes.plot(tempo,h1,'.-')
axes.set_ylabel('h1')
axes = fig.add_subplot(4,1,3)
axes.plot(tempo,v1_,'.-')
axes.set_ylabel('v1')
axes = fig.add_subplot(4,1,4)
axes.plot(tempo,v2_,'.-')
axes.set_ylabel('v2')
fig.show()



print(delta_time)

#print(delta_time)