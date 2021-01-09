from tifffile import imread
from pathlib import Path
from struct import unpack
import numpy as np

BYTEORDER = {
    "little":"<",
    "big":">"
}

PRECISION = {
    "int16":"h",
    "uint16":"H",
    "int32":"i",
    "uint32":"I",
    "int64":"q",
    "uint64":"Q",
    "float":"f",
    "double":"d"
}

def load_tiff(filepath):
    return imread(filepath)

def load_binary(filepath, height, width, encoding, byteorder):
    encode_str = f"{BYTEORDER[byteorder]}{height*width}{PRECISION[encoding]}"
    binary_img = Path(filepath).read_bytes()
    decoded_img = unpack(encode_str, binary_img)
    return np.reshape(decoded_img, (height, -1))

def load_ascii(filepath, delimiter):
    return np.loadtxt(filepath, delimiter=delimiter)