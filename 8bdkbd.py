#!/usr/bin/python
import time
import argparse
import usb.core
import usb.util

parser = argparse.ArgumentParser(
    description="Key mapper for 8BitDo\'s Retro Mechanical Keyboard")
subparsers = parser.add_subparsers()

parser_map = subparsers.add_parser(
    "list-keys", help="list the names of keys to be used in maps")

parser_map = subparsers.add_parser("map",
                                   help="map hardware keys to other keys")
parser_map.add_argument("hadware_key", type=str)
parser_map.add_argument("mapped_key", type=str)
parser_map.add_argument("--hid", type=str)
