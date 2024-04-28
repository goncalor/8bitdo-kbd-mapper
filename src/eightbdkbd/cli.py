import sys
import argparse
import usb.core

import keys
import utils
import consts
from client import EightBDKdb


def main():
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
    parser_map.set_defaults(func=cmd_map_key)
    parser_map.add_argument(
        "hardware_key",
        type=arg_hw_key,
        help="the name of the hardware key whose mapping will be changed")
    parser_map.add_argument(
        "mapped_key",
        type=arg_mapped_key,
        help=
        "the name of the key to map to (eg. \"esc\");\nuse the \"list-keys\" subcommand for a key name reference"
    )

    parser_map_hid = subparsers.add_parser(
        "map-hid", help="map hardware keys to HID Usage codes")
    parser_map_hid.set_defaults(func=cmd_map_hid)
    parser_map_hid.add_argument(
        "hardware_key",
        type=arg_hw_key,
        help="the name of the hardware key whose mapping will be changed")
    parser_map_hid.add_argument(
        "hid_usage",
        type=arg_hid_usage,
        help="a HID Usage code hex string (eg. 070029 for \"esc\")")

    parser_status = subparsers.add_parser(
        "status", help="check and output current status")
    parser_status.set_defaults(func=cmd_status)

    parser_profile = subparsers.add_parser("profile", help="manage profile")
    parser_profile_sub = parser_profile.add_subparsers(required=True)
    # parser_profile.set_defaults(func=cmd_profile)

    parser_profile_create = parser_profile_sub.add_parser(
        "create", help="create a new profile (or enable current maps)")
    parser_profile_create.set_defaults(func=cmd_profile_create)
    parser_profile_create.add_argument("name",
                                       type=str,
                                       help="a name for the new profile")

    parser_profile_delete = parser_profile_sub.add_parser(
        "delete", help="delete current profile (clears maps)")
    parser_profile_delete.set_defaults(func=cmd_profile_delete)

    args = parser.parse_args()
    if not hasattr(args, "func"):
        parser.print_help()
        sys.exit()
    args.func(args)


def cmd_list_keys(args):
    print("Mappable keys")
    print("-------------")
    print()
    utils.print_usage_keys()
    print()
    # print("Can't find the key you're looking for? Use \"map-hid\".")
    # print()
    print("Hardware keys")
    print("-------------")
    print()
    utils.print_hw_keys()
    print()


# TODO: create Key and Usage classes and store byte value but also name/hex
# Those could be used to write things as "successfully mapped capslock to esc"
def cmd_map(hwkey, usage):
    kbd = EightBDKdb()
    try:
        kbd.map_hid_usage(hwkey, usage)
    except Exception as e:
        print(f"Failed mapping with error: {e}\nMaybe try again?")
        sys.exit(1)


def cmd_map_key(args):
    cmd_map(args.hardware_key, args.mapped_key)


def cmd_map_hid(args):
    cmd_map(args.hardware_key, args.hid_usage)


def cmd_status(args):
    # keyboard connected?
    print("8BitDo connected: ", end="")
    if usb.core.find(idVendor=consts.VENDOR_ID, idProduct=consts.PRODUCT_ID):
        print("yes")
    else:
        print("no")
        return

    # profile name
    kbd = EightBDKdb()
    print("    Profile name:", kbd.get_profile_name())

    # mapped keys
    mapped = kbd.get_mapped_keys()
    print("     Mapped keys:", " ".join(mapped))

    # key mapings
    print()
    for key in mapped:
        print(f"     {key} ->", kbd.get_key_mapping(key))


def cmd_profile(args):
    pass


def cmd_profile_create(args):
    kbd = EightBDKdb()
    kbd.rename_profile(args.name)
    print("Successfully created profile")


def cmd_profile_delete(args):
    kbd = EightBDKdb()
    kbd.delete_profile()
    print("Successfully deleted profile")


def arg_hw_key(key):
    if not key in keys.HWKEY:
        raise argparse.ArgumentTypeError(
            f"unknown value '{key}'.\nUse \"list-keys\" to list known values.")

    return keys.HWKEY[key]


def arg_mapped_key(key):
    if not key in keys.USAGE:
        raise argparse.ArgumentTypeError(
            f"unknown value '{key}'.\nUse \"list-keys\" to list known values.")

    return utils.int_to_bytes(keys.USAGE[key][0])


def arg_hid_usage(usage):
    try:
        usage = bytes.fromhex(usage)
    except ValueError as e:
        raise argparse.ArgumentTypeError(
            f"could not convert '{usage}' to bytes. Maybe a digit is missing?")

    # remaining buffer len, although usages should be shorter
    if len(usage) > 24:
        raise argparse.ArgumentTypeError(f"value '{usage}' is too long.")

    return list(usage)
