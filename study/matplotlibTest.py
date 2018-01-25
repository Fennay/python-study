#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    c, s = np.cos(x), np.sin(x)
    plt.figure(1)
    plt.plot(x, c, color="green", linewidth=1.5, linestyle='-', label='COS', alpha=0.8)
    plt.plot(x, s, color="red", linestyle='--', label="SIN")
    plt.title('COS & SIN')
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    # ax.xaxis.set_ticks_position('none')
    # ax.yaxis.set_ticks_position('left')
    # plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
    #            [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    plt.xticks(np.linspace(-np.pi, np.pi, 20, endpoint=True))
    plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(12)
        label.set_bbox(dict(facecolor='white', edgecolor='none', alpha=0.2))
    plt.legend(loc='upper left')
    plt.grid()
    plt.fill_between(x, np.abs(x) < 0.5, s, where=s > 0.5, color='blue', alpha=0.25)
    # plt.fill_between(x, np.abs(x) < 0.5, c, where=c > 0.5, color='green', alpha=0.25)
    t = 1
    plt.plot([t, t], [0, np.cos(t)], 'y', linewidth=3, linestyle='--')
    plt.annotate('cos(1)', xy=(t, np.cos(1)), xycoords="data", xytext=(+10, +30),
                 textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

    plt.show()


if __name__ == "__main__":
    main()
