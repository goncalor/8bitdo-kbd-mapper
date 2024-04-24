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
    pass
