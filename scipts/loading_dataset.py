import numpy as np
import _pickle as pickle
import itertools
import matplotlib.pyplot as plt
from inspect_feature import inspect_freq as inspect_freq
from inspect_feature import inspect_time as inspect_time

DATASET_DIR="E:/GitHub-E/wireless_transformer/records/Dataset_10mod_0524"
PREFIX=[
    "Dataset_EIB_Outdoor", 
    "Dataset_EIB_room328_to_Hallway", 
    "Dataset_EIB_3F_Hallway_0430"
]

TP=[-10, -5, 0, 5]
D=[5, 10, 15]
SR=[20]
CF=2360
# I=[0, 1]
I=[1]

# ===================================================
# For the Data: (contain 1 sample from each modulation)
# Raw Data:              (10, 2, 128)   (num_mod, 2, 128) dtype=np.float32
# Original Time feature: (10, 16, 16)   (num_mod, 16, 16) dtype=np.complex64
# Original Freq feature: (10, 4, 64)    (num_mod, 4, 64)  dtype=np.complex64
# Both Time and Frequ are reshaped to (10, 2, 128)
# X_real = np.concatenate((raw_data[:, 0, :], time_feature.real, freq_feature.real))
# X_imag = np.concatenate((raw_data[:, 1, :], time_feature.imag, freq_feature.imag))
# (X_real, X_imag): ((10, 5, 128), (10, 5, 128))
# X = np.concatenate(X_real, X_imag) (10, 10, 128)
# ===================================================

def load_data(dir=DATASET_DIR, filename=None):
    if filename is None:
        print(f"{filename}")
        return

    with open(f"{dir}/{filename}", 'rb') as f:
        data = pickle.load(f, encoding='latin1')

    # There are 10 types in this case:
    # It should be the modulated protocol signals:
    #   OFDM-BPSK, OFDM-QPSK, OFDM-16QAM, OFDM-64QAM
    #   OQPSK, BT-LE1M, BT-LE2M, BT-S2, BT-S8, Noise
    print("---")
    print(data.keys())
    print("Data Size: ", data['X'].shape, data['Y'].shape)      # (200_000, 2, 128)

    i = 0
    t = data['Y'][i]
    while True:
        if data['Y'][i] != t:
            t = data['Y'][i]
            break
        i += 1

    print(f"From: {data['Y'][0]} to {data['Y'][-1]}")
    pass


def main():
    prefix = "Dataset_EIB_Outdoor"
    combinations = itertools.product(PREFIX, TP, D, SR, I)

    for c in combinations:
        # filename = f"{c[0]}_TP{c[1]}_D{c[2]}_SR{c[3]}_CF{CF}_I{c[4]}.pkl"
        # load_data(filename=f"{c[0]}/{filename}")
        filename = f"{c[0]}_TP{c[1]}_D{c[2]}_SR{c[3]}_CF{CF}_I{c[4]}-Time-Freq.pkl"
        load_data(filename=f"{c[0]}/{filename}")
        return
    pass

if __name__ == '__main__':
    main()
