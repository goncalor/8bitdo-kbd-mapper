8BitDo Keyboard Mapper
======================

`8bdkbd` is an utility and Python library to configure [8BitDo Retro Mechanical Keyboard][8bitdo-kbd-product-page]. It allows you to map keyboard keys, read mapping status and clear mappings.

[8bitdo-kbd-product-page]: https://www.8bitdo.com/retro-mechanical-keyboard/


Why?
----

I bought an 8BitDo Mechanical Keyboard and wanted to map a specific key to the A and B programmable keys. I couldn't do it with 8BitDo's "Ultimate Software v2". For me this meant I could not type `<` or `>` with my keyboard layout. Since the Ultimate Software is proprietary, I could not change the code to add an option to map to the missing key either. Also, this software is only available for Windows.

In short, I wrote `8bdkbd` so that:
- anyone could map keyboard keys to whichever key they wanted
- the keyboard could be configured from GNU/Linux systems
- a free and open-source (FOSS) software was available for people to modify/study


How to use it
-------------

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


Why not Rust?
-------------

It would have been nice to write this in Rust, but I wanted it to be easy to set up for anyone to use. I picked Python for that reason.
