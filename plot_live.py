import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
open('plot.txt', 'w').close()  # clear file


def animate(i):
    data = open('plot.txt', 'r').read()
    data_list = data.split('\n')
    xs = []
    ys = []
    for line in data_list:
        if len(line) > 0:
            x, y = line.split(' ')
            xs.append(float(x))
            ys.append(float(y)/10)
    plt.cla()
    plt.plot(xs, ys, 'k', lw=.5)
    plt.xlabel('time (sec)')
    plt.ylabel('temperature')


def main():
    ani = animation.FuncAnimation(fig, animate, interval=100)
    plt.show()


main()
