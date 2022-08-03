import serial
from datetime import datetime
import time
from time import sleep

# `$ python -m serial.tools.list_ports`


def open_port():
    # set port
    tcs_port = "/dev/cu.usbmodem14401"
    tcs = serial.Serial(tcs_port, baudrate=115200, timeout=1)
    sleep(0.001)
    tcs.write(b"F")
    return tcs


def port_status(tcs):
    if tcs.is_open:
        sleep(0.001)
        tcs.write(b"B")
        battery = tcs.read_until().decode()
        if len(battery) > 0:
            print("\ntcs port open:", datetime.now().strftime("%H:%M %m/%d/%y"))
            print(battery)
        else:
            print("\nturn tcs power ON")
            raise KeyboardInterrupt
    else:
        print("\ntcs port closed:", datetime.now().strftime("%H:%M %m/%d/%y"))


def set_parameters(tcs, parameters):
    for i in parameters:
        sleep(0.001)
        tcs.write(i.encode())


def replace(var, st):
    for i in st:
        var = var.replace(i, "")
    return var


def print_parameters(tcs):
    sleep(0.001)
    tcs.write(b"F")
    sleep(0.001)
    tcs.write(b"P")
    par = tcs.read_until().decode().replace("\r", "")
    print("\nparameters: ")
    print("global:", par[:28])
    print("zone 1:", par[28:51])
    print("zone 2:", par[51:74])
    print("zone 3:", par[74:97])
    print("zone 4:", par[97:120])
    print("zone 5:", par[120:], "\n")


def start_stim(tcs):
    sleep(0.001)
    tcs.write(b"O")
    tcs.reset_output_buffer()
    tcs.reset_input_buffer()
    sleep(0.001)
    tcs.write(b"L")


def stim(tcs, start):

    # plot.txt is read by plot_live.py
    open("plot.txt", "w").close()  # clear file

    start_stim(tcs)

    # the tcs will return the current temperatures of the five zones at 100Hz
    for _ in range(
        1000
    ):  # range dependent on parameter Y9999, writes 9.99sec of temp data
        temp = tcs.read_until().decode().strip()
        temp = replace(temp, "+.")

        x = time.time() - start
        y = temp[:3]

        if len(temp) > 1:
            with open("plot.txt", "a") as file_out:
                print("%s %s" % (x, y), file=file_out)


def main():

    tcs = open_port()

    try:
        port_status(tcs)

        # define stim parameters
        set_parameters(tcs, parameters="N350 C0480 S11111 D006000 Y9999")
        print_parameters(tcs)

        input("[enter]: ")

        # start stim, run 10x
        start = time.time()
        for counter in range(1, 11):

            print("heat%d" % counter)
            stim(tcs, start)

            print("neutral%d" % counter)
            sleep(6)

    except KeyboardInterrupt:
        sleep(0.001)
        tcs.write(b"A")

    tcs.close()
    port_status(tcs)


main()
