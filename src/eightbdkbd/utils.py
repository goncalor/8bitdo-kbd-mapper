import keys


def print_hw_keys():
    prev_key = None
    for key in keys.HWKEY:
        if key in ["grave", "tab", "capslock", "leftshift", "leftctrl"]:
            print()
        # some keys have aliases. print only the first name
        if not keys.HWKEY[key] == keys.HWKEY.get(prev_key):
            print(key, end=" ")
        else:
            pass  #print(f"({key})", end=" ")
        prev_key = key
    print()


def print_usage_keys():
    for key, val in keys.USAGE.items():
        print(f"{key:14}  {val[1]}")


def int_to_bytes(i):
    val = f"{i:x}"
    if len(val) % 2 != 0:
        val = "0" + val
    return list(bytes.fromhex(val))
