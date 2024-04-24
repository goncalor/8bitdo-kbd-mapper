#!/usr/bin/python
import time
import argparse
import usb.core
import usb.util

ATTN = [0x52, 0x76, 0xff]
MAP = [0x52, 0xfa, 0x03, 0x0c, 0x00, 0xaa, 0x09, 0x71]
MAP_DONE = [0x52, 0x76, 0xa5]


class EightBDKdb:

    def __init__(self):
        self.ep_read, self.ep_write = get_8bd_endpoints()
        print(self.ep_read)
        print(self.ep_write)

    def read(self, size=64, timeout=1000):
        return self.ep_read.read(size, timeout).tobytes()

    def write(self, data, size=33):
        return self.ep_write.write(data + [0] * (33 - len(data)))

    def map_hid_usage(self, hwkey, usage):
        #TODO: verify data length
        #TODO: verify key value makes sense
        self.write(ATTN)
        print(self.read().hex())
        self.write(MAP + [hwkey] + usage)
        print(self.read().hex())
        self.write(MAP_DONE)
        print(self.read().hex())

    def map_key(self, hwkey, key):
        pass


def get_8bd_endpoints():
    dev = usb.core.find(idVendor=0x2dc8, idProduct=0x5200)

    if dev is None:
        raise ValueError("Could not find 8BitDo Retro Mechanical Keyboard")

    # detach interface #2 if needed
    if dev.is_kernel_driver_active(2):
        print("detaching kernel driver")
        dev.detach_kernel_driver(2)

    # [config][(interface, alternate)][endpoint]
    endpoint_in = dev[0][(2, 0)][0]
    endpoint_out = dev[0][(2, 0)][1]

    return endpoint_in, endpoint_out


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Key mapper for 8BitDo\'s Retro Mechanical Keyboard")
    subparsers = parser.add_subparsers()

    parser_map = subparsers.add_parser(
        "list-keys", help="list the names of keys to be used in maps")

    #TODO: mutully exclude options
    parser_map = subparsers.add_parser("map",
                                       help="map hardware keys to other keys")
    parser_map.add_argument("hadware_key", type=str)
    parser_map.add_argument("mapped_key", type=str)
    parser_map.add_argument(
        "--hid",
        type=str,
        help="an hex string corresponding to a HID usage ID")

    args = parser.parse_args()

    test = EightBDKdb()
    test.map_hid_usage(0x29, [0x07, 0x00, 0x29])
