#!/usr/bin/python
import time
import argparse
import usb.core
import usb.util

import utils

VENDOR_ID = 0x2dc8
PRODUCT_ID = 0x5200

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
    dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

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


def cmd_list_keys(args):
    print("Mappable keys")
    print("-------------")
    print()
    utils.print_usage_keys()
    print()
    # print("Can't find the key you're looking for? Use \"map --hid\".")
    # print()
    print("Hardware keys")
    print("-------------")
    print()
    utils.print_hw_keys()
    print()


def cmd_map(args):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Key mapper for 8BitDo\'s Retro Mechanical Keyboard")
    subparsers = parser.add_subparsers()

    parser_list_keys = subparsers.add_parser(
        "list-keys", help="list the names of keys to be used in maps")
    parser_list_keys.set_defaults(func=cmd_list_keys)

    parser_map = subparsers.add_parser(
        "map",
        formatter_class=argparse.RawTextHelpFormatter,
        help="map hardware keys to other keys")
    parser_map.set_defaults(func=cmd_map)
    parser_map.add_argument(
        "--hid",
        action="store_true",
        help="map directly to a HID Usage, not to a key name")
    parser_map.add_argument(
        "hardware_key",
        type=str,
        help="the name of the hardware key whose mapping will be changed")
    parser_map.add_argument(
        "mapped_key",
        type=str,
        metavar="{mapped_key,hid_usage}",
        help=
        "the name of the key to map to (eg. \"esc\");\nor a HID Usage code hex string, when --hid is specified (eg. 070029);\nuse the \"list-keys\" subcommand for a key name reference"
    )

    args = parser.parse_args()

    args.func(args)
