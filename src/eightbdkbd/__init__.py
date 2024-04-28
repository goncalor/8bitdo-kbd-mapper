import os, sys

# Not sure if this is a bad idea, but it's the way I could figure such that
# everything would work both by calling __main__.py directly and by running
# installed 8bdkbd script.
# If you have a better way to do this... Let me know.
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
