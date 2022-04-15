import colorsys

import numpy as np

ZO_WIND_NORM = 1
ZO_WIND_VECTORS = 2
ZO_TRAJS = 3
ZO_RFF = 4
ZO_ANNOT = 5

my_red = np.array([0.8, 0., 0., 1.])
my_red_t = np.diag((1., 1., 1., 0.2)).dot(my_red)
my_orange = np.array([1., 0.5, 0., 1.])
my_orange2 = np.array([105 / 255, 63 / 255, 0., 1.0])
my_orange_t = np.diag((1., 1., 1., 0.5)).dot(my_orange)
my_blue = np.array([0., 0., 0.8, 1.])
my_blue_t = np.diag((1., 1., 1., 0.5)).dot(my_blue)
my_dark_blue = np.array([28 / 255, 25 / 255, 117 / 255, 1.])
my_black = np.array([0., 0., 0., 1.])
my_grey1 = np.array([0.75, 0.75, 0.75, 0.6])
my_grey2 = np.array([0.7, 0.7, 0.7, 1.0])
my_grey3 = np.array([0.5, 0.5, 0.5, 1.0])
my_green = np.array([0., 0.8, 0., 1.])
my_green_t = np.diag((1., 1., 1., 0.5)).dot(my_green)

reachability_colors = {
    'pmp': {
        "steps": my_grey3,
        "time-tick": my_orange2,
        "last": my_red
        # "steps": my_grey2,
        # "time-tick": my_orange,
        # "last": my_red
    },
    'integral': {
        "steps": my_dark_blue,
        "time-tick": my_orange2,
        "last": my_blue
    },
    "approx": {
        "steps": my_grey1,
        "time-tick": my_orange_t,
        "last": my_orange
    },
    "point": {
        "steps": my_grey1,
        "time-tick": my_orange,
        "last": my_orange
    },
    "optimal": {
        "steps": my_red,
        "time-tick": my_red,
        "last": my_red
    },
}

markers = ['o', "1", "2", "3", "4"]

# linestyle = ['solid', 'dotted', 'dashed', 'dashdot', (0, (1, 10)), (0, (5, 10)), (0, (3, 5, 1, 5))]

linestyle = ['solid']

monocolor_colors = {
    'pmp': my_red_t,
    'approx': my_orange_t,
    'point': my_blue,
    'integral': my_black
}

EARTH_RADIUS = 6378.137e3  # [m] Earth equatorial radius

# Windy default cm
CM_WINDY = [[0, [98, 113, 183, 255]],
            [1, [57, 97, 159, 255]],
            [3, [74, 148, 169, 255]],
            [5, [77, 141, 123, 255]],
            [7, [83, 165, 83, 255]],
            [9, [53, 159, 53, 255]],
            [11, [167, 157, 81, 255]],
            [13, [159, 127, 58, 255]],
            [15, [161, 108, 92, 255]],
            [17, [129, 58, 78, 255]],
            [19, [175, 80, 136, 255]],
            [21, [117, 74, 147, 255]],
            [24, [109, 97, 163, 255]],
            [27, [68, 105, 141, 255]],
            [29, [92, 144, 152, 255]],
            [36, [125, 68, 165, 255]],
            [46, [231, 215, 215, 256]],
            [51, [219, 212, 135, 256]],
            [77, [205, 202, 112, 256]],
            [104, [128, 128, 128, 255]]]

# Truncated Windy cm
CM_WINDY_TRUNCATED = [[0, [98, 113, 183, 255]],
                      [1, [57, 97, 159, 255]],
                      [3, [74, 148, 169, 255]],
                      [5, [77, 141, 123, 255]],
                      [7, [83, 165, 83, 255]],
                      [9, [53, 159, 53, 255]],
                      [11, [167, 157, 81, 255]],
                      [13, [159, 127, 58, 255]],
                      [15, [161, 108, 92, 255]],
                      [17, [129, 58, 78, 255]],
                      [19, [175, 80, 136, 255]],
                      [21, [117, 74, 147, 255]],
                      [24, [109, 97, 163, 255]],
                      [27, [68, 105, 141, 255]],
                      [29, [92, 144, 152, 255]],
                      [36, [int(1.1 * 125), int(1.1 * 68), int(1.1 * 165), 255]]]
                      #[36, [125, 68, 165, 255]]]

# Define windy cm
import matplotlib.colors as mpl_colors

cm_values = CM_WINDY_TRUNCATED


def lighten(c):
    hls = colorsys.rgb_to_hls(*(np.array(c[:3]) / 256.))
    hls = (hls[0], 0.5 + 0.5 * hls[1], 0.6 + 0.4 * hls[2])
    res = list(colorsys.hls_to_rgb(*hls)) + [c[3] / 256.]
    return res


newcolors = np.array(lighten(cm_values[0][1]))
for ii in range(len(cm_values) - 1):
    j_min = 10 * cm_values[ii - 1][0]
    j_max = 10 * cm_values[ii][0]
    for j in range(j_min, j_max):
        c1 = np.array(lighten(cm_values[ii - 1][1]))
        c2 = np.array(lighten(cm_values[ii][1]))
        t = (j - j_min) / (j_max - j_min)
        newcolors = np.vstack((newcolors, (1 - t) * c1 + t * c2))

windy_cm = mpl_colors.ListedColormap(newcolors, name='Windy')
windy_cm.norm_min = 0.
windy_cm.norm_max = 36.
