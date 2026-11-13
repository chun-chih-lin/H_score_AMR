import numpy as np
import matplotlib.pyplot as plt

def inspect_freq(freq_ret, ret_label, ret_mod, show=False):
    print("Inspecting frequency retults")
    print(f"\t{freq_ret.shape = }")
    if not show:
        return

    cmap = plt.get_cmap('turbo')
    axis_lim = 1.5
    colors = [cmap(i) for i in np.linspace(0, 1, freq_ret.shape[1])]
    num_pkt = freq_ret.shape[0]
    for pkt_i in range(num_pkt):
        label = ret_label[pkt_i]
        mod_name = ret_mod[label]

        fig, ax = plt.subplots()
        ax.matshow(np.abs(freq_ret[pkt_i, :, :]))
        ax.set_axis_off()
        # plt.savefig(f"{mod_name}-freq.png",bbox_inches='tight')

        # plt.figure(pkt_i)
        # fig, axs = plt.subplots(2, 1)
        # axs[0].matshow(np.abs(freq_ret[pkt_i, :, :]))
        # for indent in range(freq_ret.shape[1]):
        #     axs[1].plot(np.real(freq_ret[pkt_i, indent, :]), 
        #                 np.imag(freq_ret[pkt_i, indent, :]), 
        #                 linestyle='None', 
        #                 markersize=4, 
        #                 marker='o', 
        #                 markerfacecolor='none', 
        #                 color=colors[indent])
        # axs[1].set_aspect('equal')
        # axs[1].set_xlim(-axis_lim, axis_lim)
        # axs[1].set_ylim(-axis_lim, axis_lim)
        # plt.title(f"Freq: {mod_name}")
    plt.show()
    pass

def inspect_time(time_ret, ret_label, ret_mod, show=False):
    print(f"Inspecting time retults")
    print(f"\t{time_ret.shape = }")
    if not show:
        return
    num_pkt = time_ret.shape[0]
    for pkt_i in range(num_pkt):
        label = ret_label[pkt_i]
        mod_name = ret_mod[label]

        fig, ax = plt.subplots()
        plt.figure(pkt_i)
        ax.matshow(np.abs(time_ret[pkt_i, :, :]))
        # ax.set_axis_off()
        # plt.savefig(f"{mod_name}-time.png",bbox_inches='tight')
        plt.title(f"Time: {mod_name}")
    plt.show()