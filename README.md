## run_tcs
> script to run [thermal cutaneous stimulator](https://www.qst-lab.eu/)

control of the system using [serial commands](https://pyserial.readthedocs.io/en/latest/pyserial.html) sent over USB connection

**to run**:
- check connections: TCS to thermal probe, TCS to computer
- set computer port: on OSX it will be /dev/cu.usbmodemNNN, where NNN is some number
- to find ports run: `$ python -m serial.tools.list_ports`
- to run: `$ python run_tcs.py`
- to run with live plotting: `$ python plot_live.py; python run_tcs.py`

below are some commands that can be passed to the TCS with the function run_tcs.set_parameters():

**global parameters**:
| command | action       | values for x       | default for x | unit  |
|:--------|:-------------|:-------------------|:--------------|:------|
| Nxxx    | neutral temp | 200-400            | 300           | 0.1 C |
| Sxxxxx  | active zones | 0 or 1 per surface | 00000         |       |
| Yxxxx   | temp display | 0001-9999          | 0200          | ms    |

**zone parameters**:
| command | action          | values for x | default for x | unit     |
|:--------|:----------------|:-------------|:--------------|:---------|
| Csxxx   | stim temp       | 000-600      | 100           | 0.1C     |
| Dsxxxxx | stim duration   | 00001-99999  | 000100        | ms       |
| Vsxxxx  | ramp-up speed   | 0001-1000    | 1000          | 0.1C/sec |
| Rsxxxx  | ramp-down speed | 0001-1000    | 1000          | 0.1C/sec |

**TCS control**:
| command | action                         | returns                 | unit  |
|:--------|:-------------------------------|:------------------------|:------|
| O       | enable regular display of temp | temp of each zone       | 100Hz |
| E       | displays current temps         | neutral, then each zone | 1Hz   |
| B       | battery charge                 | battery V and %         |       |
| P       | displays stim parameters       | global, then each zone  |       |
| H       | help                           | manual                  |       |
| F       | disble current display of temp |                         |       |
| A       | abort current stim             |                         |       |
| L       | start stim                     |                         |       |
