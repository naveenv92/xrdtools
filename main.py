import xrdtools.synchrotron as syn
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    file = "AgB.gb"
    binary_info = {
        "height": 1679,
        "width": 1475,
        "encoding": "float",
        "byteorder": "little"
    }

    img = syn.load_binary(file, **binary_info)
    
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(np.log(img))
    plt.show()