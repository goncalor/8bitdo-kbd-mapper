import sys
import usb.core

import keys
from consts import *


class EightBDKdb:

    def __init__(self):
        self.ep_read, self.ep_write = get_8bd_endpoints()
        # print(self.ep_read)
        # print(self.ep_write)

    def read(self, size=64, timeout=1000):
        return self.ep_read.read(size, timeout).tobytes()

    def write(self, data, size=33):
        return self.ep_write.write(data + [0] * (33 - len(data)))

    def read_check_start(self, expected, size=64, timeout=1000):
        r = self.read(size, timeout)  # bytes
        if not r.startswith(bytes(expected)):
            raise ValueError(
                f"Read unexpected start value\nExpected: {bytes(expected).hex()}\n    Read: {r.hex()}"
            )

        return r

    def map_hid_usage(self, hwkey, usage):
        assert len(usage) <= 24

        self.write(ATTN)
        self.read()

        self.write(MAP + [hwkey] + usage)
        self.read_check_start(OK)

        self.write(MAP_DONE)
        self.read_check_start(OK)

    def get_profile_name(self):
        self.write(ATTN)
        self.read()

        self.write(PROFILE_GET_NAME)
        r = self.read()

        if r.startswith(bytes(PROFILE_NONE)):
            return None
        if r.startswith(bytes(PROFILE_NAME)):
            # skip 4 bytes, exclude trailing null bytes
            return r.rstrip(bytes([0]))[4:].decode(encoding="utf-16-be")

        raise ValueError(
            f"Read unexpected value\nExpected: {bytes(PROFILE_NONE).hex()} or\n          {bytes(PROFILE_NAME).hex()}\n    Read: {r.hex()}"
        )

    def get_mapped_keys(self):
        self.write(ATTN)
        self.read()

        self.write(PROFILE_GET_MAPPED)

        # loop read until we have received all mapped keys
        r = self.read_check_start(PROFILE_MAPPED)
        keymap = bytes() + r[2:-1]  # last byte is a marker
        while r[-1] == 0x01:  # indicates there are more maps
            r = self.read_check_start(PROFILE_MAPPED)
            keymap += r[2:]

        mapped_keys = []
        for i, kc in enumerate(keymap):
            if i % 2 == 1:  # separator
                continue
            elif kc == 0:  # no more keys mapped
                break
            else:  # key mapped
                for key, val in keys.HWKEY.items():
                    if val == kc:
                        mapped_keys.append(key)
                        break

        return mapped_keys

    def get_key_mapping(self, key):
        self.write(ATTN)
        self.read()

        self.write(MAPPING_GET + [keys.HWKEY[key]])
        r = self.read_check_start(MAPPING)

        hid = r[3:6]
        hid_int = int.from_bytes(hid)
        for name, val in keys.USAGE.items():
            if val[0] == hid_int:
                return name

        # if no name was found, return HID code
        return "HID " + hid.hex()

    def delete_profile(self):
        self.write(PROFILE_DELETE)
        self.read_check_start(OK)

    def rename_profile(self, name):
        #TODO: name length is not well tested
        assert len(name) < 25
        self.write(ATTN)
        self.read()

        self.write(PROFILE_RENAME + list(name.encode(encoding="utf-16-be")))
        self.read_check_start(OK)


def get_8bd_endpoints():
    dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

    if dev is None:
        raise ValueError(
            "Could not find 8BitDo Retro Mechanical Keyboard. Is its cable connected?"
        )

    # detach interface #2 if needed
    if dev.is_kernel_driver_active(2):
        print("detaching kernel driver", file=sys.stderr)
        dev.detach_kernel_driver(2)

    # [config][(interface, alternate)][endpoint]
    endpoint_in = dev[0][(2, 0)][0]
    endpoint_out = dev[0][(2, 0)][1]

    return endpoint_in, endpoint_out
