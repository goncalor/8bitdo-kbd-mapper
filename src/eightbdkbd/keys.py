HWKEY = {
    "esc": 0x29,
    "f1": 0x3a,
    "f2": 0x3b,
    "f3": 0x3c,
    "f4": 0x3d,
    "f5": 0x3e,
    "f6": 0x3f,
    "f7": 0x40,
    "f8": 0x41,
    "f9": 0x42,
    "f10": 0x43,
    "f11": 0x44,
    "f12": 0x45,
    "prtsc": 0x46,
    "scrlk": 0x47,
    "pause": 0x48,
    # numbers row
    "grave": 0x35,
    "1": 0x1e,
    "2": 0x1f,
    "3": 0x20,
    "4": 0x21,
    "5": 0x22,
    "6": 0x23,
    "7": 0x24,
    "8": 0x25,
    "9": 0x26,
    "0": 0x27,
    "minus": 0x2d,
    "equal": 0x2e,
    "backspace": 0x2a,
    "insert": 0x49,
    "home": 0x4a,
    "pageup": 0x4b,
    # top row
    "tab": 0x2b,
    "q": 0x14,
    "w": 0x1a,
    "e": 0x08,
    "r": 0x15,
    "t": 0x17,
    "y": 0x1c,
    "u": 0x18,
    "i": 0x0c,
    "o": 0x12,
    "p": 0x13,
    "leftbrace": 0x2f,
    "rightbrace": 0x30,
    "backslash": 0x31,
    "delete": 0x4c,
    "end": 0x4d,
    "pagedown": 0x4e,
    # home row
    "capslock": 0x39,
    "a": 0x04,
    "s": 0x16,
    "d": 0x07,
    "f": 0x09,
    "g": 0x0a,
    "h": 0x0b,
    "j": 0x0d,
    "k": 0x0e,
    "l": 0x0f,
    "semicolon": 0x33,
    "apostrophe": 0x34,
    "enter": 0x28,
    # bottom row
    "leftshift": 0x65,
    "z": 0x1d,
    "x": 0x1b,
    "c": 0x06,
    "v": 0x19,
    "b": 0x05,
    "n": 0x11,
    "m": 0x10,
    "comma": 0x36,
    "dot": 0x37,
    "slash": 0x38,
    "rightshift": 0x69,
    "up": 0x52,
    # spacebar row
    "leftctrl": 0x64,
    "windows": 0x67,
    "leftmeta": 0x67,  # Windows key
    "leftalt": 0x66,
    "space": 0x2c,
    "rightalt": 0x6a,
    "superb": 0x6c,
    "rightmeta": 0x6c,  # super B
    "supera": 0x6d,
    "compose": 0x6d,  # super A
    "menu": 0x6d,  # super A
    "rightctrl": 0x68,
    "left": 0x50,
    "down": 0x51,
    "right": 0x4f,
}

# HID Usages
# https://www.usb.org/document-library/hid-usage-tables-15
#
# Key names match from Linux's event codes.
# Key descriptions are from HID.
#
# A way to test/debug is to use `evtest [--grab] /dev/input/by-id/...`
#
USAGE = {
    "none": (0x070000, "(no key pressed)"),
    #
    "a": (0x070004, "Keyboard a and A"),
    "b": (0x070005, "Keyboard b and B"),
    "c": (0x070006, "Keyboard c and C"),
    "d": (0x070007, "Keyboard d and D"),
    "e": (0x070008, "Keyboard e and E"),
    "f": (0x070009, "Keyboard f and F"),
    "g": (0x07000a, "Keyboard g and G"),
    "h": (0x07000b, "Keyboard h and H"),
    "i": (0x07000c, "Keyboard i and I"),
    "j": (0x07000d, "Keyboard j and J"),
    "k": (0x07000e, "Keyboard k and K"),
    "l": (0x07000f, "Keyboard l and L"),
    "m": (0x070010, "Keyboard m and M"),
    "n": (0x070011, "Keyboard n and N"),
    "o": (0x070012, "Keyboard o and O"),
    "p": (0x070013, "Keyboard p and P"),
    "q": (0x070014, "Keyboard q and Q"),
    "r": (0x070015, "Keyboard r and R"),
    "s": (0x070016, "Keyboard s and S"),
    "t": (0x070017, "Keyboard t and T"),
    "u": (0x070018, "Keyboard u and U"),
    "v": (0x070019, "Keyboard v and V"),
    "w": (0x07001a, "Keyboard w and W"),
    "x": (0x07001b, "Keyboard x and X"),
    "y": (0x07001c, "Keyboard y and Y"),
    "z": (0x07001d, "Keyboard z and Z"),
    #
    "1": (0x07001e, "Keyboard 1 and !"),
    "2": (0x07001f, "Keyboard 2 and @"),
    "3": (0x070020, "Keyboard 3 and #"),
    "4": (0x070021, "Keyboard 4 and $"),
    "5": (0x070022, "Keyboard 5 and %"),
    "6": (0x070023, "Keyboard 6 and ^"),
    "7": (0x070024, "Keyboard 7 and &"),
    "8": (0x070025, "Keyboard 8 and *"),
    "9": (0x070026, "Keyboard 9 and ("),
    "0": (0x070027, "Keyboard 0 and )"),
    #
    "enter": (0x070028, "Keyboard Return (ENTER)"),
    "esc": (0x070029, "Keyboard ESCAPE"),
    "backspace": (0x07002a, "Keyboard DELETE (Backspace)"),
    "tab": (0x07002b, "Keyboard Tab"),
    "space": (0x07002c, "Keyboard Spacebar"),
    "minus": (0x07002d, "Keyboard - and _"),
    "equal": (0x07002e, "Keyboard = and +"),
    "leftbrace": (0x07002f, "Keyboard [ and {"),
    "rightbrace": (0x070030, "Keyboard ] and }"),
    "backslash": (0x070031, "Keyboard \\ and |"),
    "hashtilde": (0x070032, "Keyboard Non-US # and ~"),
    "semicolon": (0x070033, "Keyboard ; and :"),
    "apostrophe": (0x070034, "Keyboard ' and \""),
    "grave": (0x070035, "Keyboard ` and ~"),
    "comma": (0x070036, "Keyboard , and <"),
    "dot": (0x070037, "Keyboard . and >"),
    "slash": (0x070038, "Keyboard / and ?"),
    "capslock": (0x070039, "Keyboard Caps Lock"),
    #
    "f1": (0x07003a, "Keyboard F1"),
    "f2": (0x07003b, "Keyboard F2"),
    "f3": (0x07003c, "Keyboard F3"),
    "f4": (0x07003d, "Keyboard F4"),
    "f5": (0x07003e, "Keyboard F5"),
    "f6": (0x07003f, "Keyboard F6"),
    "f7": (0x070040, "Keyboard F7"),
    "f8": (0x070041, "Keyboard F8"),
    "f9": (0x070042, "Keyboard F9"),
    "f10": (0x070043, "Keyboard F10"),
    "f11": (0x070044, "Keyboard F11"),
    "f12": (0x070045, "Keyboard F12"),
    #
    "sysrq": (0x070046, "Keyboard PrintScreen"),
    "prtsc": (0x070046, "Keyboard PrintScreen"),  # alias for sysrq
    "scrolllock": (0x070047, "Keyboard Scroll Lock"),
    "scrlk": (0x070047, "Keyboard Scroll Lock"),  # alias for scrolllock
    "pause": (0x070048, "Keyboard Pause"),
    "insert": (0x070049, "Keyboard Insert"),
    "home": (0x07004a, "Keyboard Home"),
    "pageup": (0x07004b, "Keyboard Page Up"),
    "delete": (0x07004c, "Keyboard Delete Forward"),
    "end": (0x07004d, "Keyboard End"),
    "pagedown": (0x07004e, "Keyboard Page Down"),
    "right": (0x07004f, "Keyboard Right Arrow"),
    "left": (0x070050, "Keyboard Left Arrow"),
    "down": (0x070051, "Keyboard Down Arrow"),
    "up": (0x070052, "Keyboard Up Arrow"),
    #
    "numlock": (0x070053, "Keyboard Num Lock and Clear"),
    "kpslash": (0x070054, "Keypad /"),
    "kpasterisk": (0x070055, "Keypad *"),
    "kpminus": (0x070056, "Keypad -"),
    "kpplus": (0x070057, "Keypad +"),
    "kpenter": (0x070058, "Keypad ENTER"),
    "kp1": (0x070059, "Keypad 1 and End"),
    "kp2": (0x07005a, "Keypad 2 and Down Arrow"),
    "kp3": (0x07005b, "Keypad 3 and PageDn"),
    "kp4": (0x07005c, "Keypad 4 and Left Arrow"),
    "kp5": (0x07005d, "Keypad 5"),
    "kp6": (0x07005e, "Keypad 6 and Right Arrow"),
    "kp7": (0x07005f, "Keypad 7 and Home"),
    "kp8": (0x070060, "Keypad 8 and Up Arrow"),
    "kp9": (0x070061, "Keypad 9 and Page Up"),
    "kp0": (0x070062, "Keypad 0 and Insert"),
    "kpdot": (0x070063, "Keypad . and Delete"),
    #
    "102nd": (0x070064, "Keyboard Non-US \\ and |"),
    "compose": (0x070065, "Keyboard Application"),
    "supera": (0x070065, "Keyboard Application"),  # alias for compose
    "menu": (0x070065, "Keyboard Application"),  # alias for compose
    #
    # Lower two bytes here seem swapped from the HID spec, unsure why.
    "leftctrl": (0x07e000, "Keyboard Left Control"),
    "leftshift": (0x07e100, "Keyboard Left Shift"),
    "leftalt": (0x07e200, "Keyboard Left Alt"),
    "leftmeta": (0x07e300, "Keyboard Left GUI"),
    "windows": (0x07e300, "Keyboard Left GUI"),  # alias for leftmeta
    "rightctrl": (0x07e400, "Keyboard Right Control"),
    "rightshift": (0x07e500, "Keyboard Right Shift"),
    "rightalt": (0x07e600, "Keyboard Right Alt"),
    "rightmeta": (0x07e700, "Keyboard Right GUI"),
    "superb": (0x07e700, "Keyboard Right GUI"),  # alias for rightmeta
    #
    # Lower two bytes here seem swapped from the HID spec, unsure why.
    "playpause": (0x0ccd00, "Play/Pause"),
    "previoussong": (0x0cb500, "Scan Next Track"),
    "nextsong": (0x0cb600, "Scan Previous Track"),
    "mute": (0x0ce200, "Mute"),
    "volumeup": (0x0ce900, "Volume Increment"),
    "volumedown": (0x0cea00, "Volume Decrement"),
    #
    "calc": (0x0c9201, "AL Calculator"),
    #
    # Not sure where these are on the HID spec.
    "btn_left": (0x010100000000, "left click"),
    "btn_right": (0x010200000000, "right click"),
    "btn_middle": (0x010400000000, "scroll click"),
    "btn_extra": (0x010800000000, "mouse button 4"),  # these may be swapped
    "btn_side": (0x011000000000, "mouse button 5"),  # these may be swapped
    # "": (0x018000000000, "double click")
    # "": (0x010000000200, "scroll up")
    # "": (0x01000000fe00, "scroll down")
    # "": (0x0100000000fe, "scroll left")
    # "": (0x010000000002, "scroll right")
}
