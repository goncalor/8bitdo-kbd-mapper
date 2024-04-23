#!/usr/bin/python
import time
import usb.core
import usb.util

dev = usb.core.find(idVendor=0x2dc8, idProduct=0x5200)

if dev is None:
    raise ValueError('Device not found')

# detach interface #2 if needed
if dev.is_kernel_driver_active(2):
    print('detaching kernel driver')
    dev.detach_kernel_driver(2)

# [config][(interface, alternate)][endpoint]
endpoint_in = dev[0][(2,0)][0]
endpoint_out = dev[0][(2,0)][1]

print(endpoint_in)
print(endpoint_out)

data = [0x52, 0x76, 0xff]
endpoint_out.write(bytes(data + [0] * (33 - len(data))))

buffer = dev.read(endpoint_in.bEndpointAddress, 64, 1000).tobytes()
print(buffer.hex())

# time.sleep(0.2)

# map super A (0x6d) to "A" (0x04)
data = [0x52, 0xfa, 0x03, 0x0c, 0x00, 0xaa, 0x09, 0x71, 0x6d, 0x07, 0x00, 0x04]
endpoint_out.write(bytes(data + [0] * (33 - len(data))))

buffer = dev.read(endpoint_in.bEndpointAddress, 64, 1000).tobytes()
print(buffer.hex())

# time.sleep(0.2)

data = [0x52, 0x76, 0xa5]
endpoint_out.write(bytes(data + [0] * (33 - len(data))))

buffer = dev.read(endpoint_in.bEndpointAddress, 64, 1000).tobytes()
print(buffer.hex())
