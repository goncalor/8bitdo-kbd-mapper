8BitDo Keyboard Mapper
======================

`8bdkbd` is an utility and Python library to configure [8BitDo Retro Mechanical Keyboard][8bitdo-kbd-product-page]. It allows you to map keyboard keys, read mapping status and clear mappings.

[8bitdo-kbd-product-page]: https://www.8bitdo.com/retro-mechanical-keyboard/


Why?
----

I bought an 8BitDo Mechanical Keyboard and wanted to map a specific key to the A and B programmable keys. I couldn't do it with 8BitDo's "Ultimate Software v2". For me this meant I could not type `<` or `>` with my keyboard layout. Since the Ultimate Software is proprietary, I could not change the code to add an option to map to the missing key either. Also, this software is only available for Windows.

In short, I wrote `8bdkbd` so that:
- anyone can map keyboard keys to whichever key they wanted
- the keyboard can be configured from GNU/Linux systems
- a free and open-source (FOSS) software is available for people to modify/study


Installation
------------

Clone the repository, `cd` into it and run

    pip install .

Copy `50-8bitdo-kdb.rules` to `/etc/udev/rules.d/`:

    sudo cp 50-8bitdo-kdb.rules /etc/udev/rules.d/
    sudo chmod 644 /etc/udev/rules.d/50-8bitdo-kdb.rules

These `udev` rules are meant to ensure that `8bdkbd` will be able to bind and use the USB interface used to configure the keyboard, without needing to be installed and ran as root.


How to use it
-------------

If you run `8bdkbd` without any other arguments it will print available options:

    usage: 8bdkbd [-h] {list-keys,map,map-hid,status,profile} ...

    Key mapper for 8BitDo's Retro Mechanical Keyboard

    positional arguments:
      {list-keys,map,map-hid,status,profile}
        list-keys           list the names of keys to be used in maps
        map                 map hardware keys to other keys
        map-hid             map hardware keys to HID Usage codes
        status              check and output current status
        profile             manage profile

    options:
      -h, --help            show this help message and exit


### Prerequisites

- You need to connect your 8BitDo keyboard to your computer through USB and ensure its power switch is set to "off" (otherwise it does not communicate over USB)
- Install the `udev` rule in the Installation step, or you'll have to run `8bdkbd` as root


### Checking the status

Status can be checked with `8bdkbd status`. With no profile created it should output:

    8BitDo connected: yes
        Profile name: None
         Mapped keys:


### Creating a profile

To create a profile called "awesome":

    $ 8bdkbd profile create awesome
    Successfully created profile

    $ 8bdkbd status
    8BitDo connected: yes
        Profile name: awesome
         Mapped keys:

`create` can also be used to rename the current profile.


### Mapping keys

Keys can be mapped through their names.

    $ 8bdkbd map capslock esc

Or they can be mapped through [HID usage codes][hid-usage-codes] if you can't find the key you want.

    $ 8bdkbd map-hid capslock 070029

The result in both cases, starting with an empty map would be:

    $ 8bdkbd status
    8BitDo connected: yes
        Profile name: awesome
         Mapped keys: capslock

         capslock -> esc


### Listing key names

Okay, but "how do I know the names for the keys?" You can use `list-keys`:

    $ 8bdkbd list-keys
    Mappable keys
    -------------

    none            (no key pressed)
    a               Keyboard a and A
    b               Keyboard b and B
    c               Keyboard c and C

    ...

    Hardware keys
    -------------

    esc f1 f2 f3 f4 f5 f6 f7 f8 f9 f10 f11 f12 prtsc scrlk pause
    grave 1 2 3 4 5 6 7 8 9 0 minus equal backspace insert home pageup
    tab q w e r t y u i o p leftbrace rightbrace backslash delete end pagedown
    capslock a s d f g h j k l semicolon apostrophe enter
    leftshift z x c v b n m comma dot slash rightshift up
    leftctrl windows leftalt space rightalt superb supera rightctrl left down right


### Unmapping a key

Just map it back to itself:

    $ 8bdkbd map esc esc


### Making a key not work

Map it to "none":

    $ 8bdkbd map capslock none


### Deleting a profile

You can delete a profile to clear all of the mappings at once:

    $ 8bdkbd profile delete
    Successfully deleted profile

    $ 8bdkbd status
    8BitDo connected: yes
        Profile name: None
         Mapped keys:


[hid-usage-codes]: https://www.usb.org/sites/default/files/hut1_5.pdf


Disclaimer
----------

Please note that the keyboard's firmware and configuration protocol are proprietary and undocumented. I have tried my best to understand the protocol and ensure correct configuration commands are issued. However, I cannot guarantee correct operation. I will not be responsible if you damage your keyboard. Use this software at your own risk.


Improvements
------------

- [x] write udev rule to avoid running as root
- [ ] add support for macros
- [ ] add support for external Super Buttons
  - for now, depending on the mappings you need, you may be able to configure them using the steps under "Fast Key Mapping" seen in [the manual](https://download.8bitdo.com/Manual/PC-Peripherals/retro-mechanical-keyboard.pdf)


Why not Rust?
-------------

It would have been nice to write this in Rust, but I wanted it to be easy to set up for anyone to use. I picked Python for that reason.
