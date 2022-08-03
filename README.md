## run_tcs
> script to run [thermal cutaneous stimulator](https://www.qst-lab.eu/)

control of the system using [serial commands](https://pyserial.readthedocs.io/en/latest/pyserial.html) sent over USB connection

**to run**:
- check connections: TCS to thermal probe, TCS to computer
- set computer port: on OSX it will be /dev/cu.usbmodemNNN, where NNN is some number
- to find ports run: `$ python -m serial.tools.list_ports`
- to run: `$ python run-tcs.py`
- to run with live plotting: `$ python plot-live.py &; python run-tcs.py`