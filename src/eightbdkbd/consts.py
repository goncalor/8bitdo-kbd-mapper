VENDOR_ID = 0x2dc8
PRODUCT_ID = 0x5200

ATTN = [0x52, 0x76, 0xff]
MAP = [0x52, 0xfa, 0x03, 0x0c, 0x00, 0xaa, 0x09, 0x71]
MAP_DONE = [0x52, 0x76, 0xa5]

PROFILE_GET_NAME = [0x52, 0x80]
PROFILE_NAME = [0x54, 0x80, 0x10, 0x00]
PROFILE_NONE = [0x54, 0x80, 0x00, 0x00]

PROFILE_GET_MAPPED = [0x52, 0x81]
PROFILE_MAPPED = [0x54, 0x81]

PROFILE_DELETE = [0x52, 0x70]
PROFILE_RENAME = [0x52, 0x70, 0x10, 0x00]

MAPPING_GET = [0x52, 0x83]
MAPPING = [0x54, 0x83]

OK = [0x54, 0xe4, 0x08]
READY = [0x54, 0x8a, 0x07, 0x01]  # nothing to report ?
