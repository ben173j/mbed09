import serial
import time
serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 9600)

s.write(bytes("\r", 'UTF-8'))
line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
print(line)
line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
print(line)
time.sleep(1)

s.write(bytes("/UI/run  \r\n", 'UTF-8'))
line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
print(line)
line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
print(line)
time.sleep(1)

#int_selected = "SUCCESS"
#s.write(bytes("From python "+int_selected + " \r\n", 'UTF-8'))
while 1>0:
    line=s.readline()
    line = str(line)
    if(any(c.isnumeric() for c in line)):
        line=s.readline()
        s.write(bytes("/Angle/run \r\n",'UTF-8'))
        break

    
line=s.readline()
s.write(bytes("\r", 'UTF-8'))
line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
print(line)
#s.write(bytes("/UI/delete \r\n",'UTF-8'))
#s.write(bytes("/Angle/run \r\n",'UTF-8'))
line=s.readline()
line=s.readline()
print(line)
s.write(bytes("\r", 'UTF-8'))
#s.write(bytes("/Angle/run \r\n",'UTF-8'))
#time.sleep(1)
s.write(bytes("\r", 'UTF-8'))
line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
print(line)
s.write(bytes("/Angle/delete \r\n",'UTF-8'))
line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
print(line)
line=s.readline()
print(line)

"""
s.write(bytes("/doLocate/run 8 0\r", 'UTF-8'))
line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
print(line)
line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
print(line)
time.sleep(1)

s.write(bytes("/doDisplay/run WELL\r", 'UTF-8'))
line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
print(line)
line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
print(line)
time.sleep(1)

s.write(bytes("\r", 'UTF-8'))
line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
print(line)
line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
print(line)
time.sleep(1)
"""