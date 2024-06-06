import numpy as np
import numpy.linalg as la


class ColorSpace:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    # TODO(1): Correct the luminance calculations: https://campuswire.com/c/GFE5B3C52/feed/29
    def getLuminanceWithWhite(self, Y=np.array([1, 1, 1])):
        M = makeMatrixForLuminance(self.red, self.green, self.blue)
        return la.solve(M.T, Y)


# TODO(1): Correct the luminance calculations: https://campuswire.com/c/GFE5B3C52/feed/29
def makeMatrixForLuminance(red, green, blue):
    #     M = np.array(
    #     [2.768892, 1.751748, 1.130160,
    #      1, 4.590700, 0.060100,
    #         0, 0.056508, 5.594292]
    # ).reshape((3, 3))
    M = np.array(
        [
            red[0],
            red[1],
            1 - red[1] - red[0],
            green[0],
            green[1],
            1 - green[1] - green[0],
            blue[0],
            blue[1],
            1 - blue[1] - blue[0],
        ]
    ).reshape((3, 3))
    return M


class SRGB(ColorSpace):
    # source https://www.coursera.org/learn/cs-519/lecture/Omhsq/the-srgb-color-space
    xyz_to_srgb_matrix = np.array(
        [
            [3.240970, -1.537383, -0.498611],
            [-0.969244, 1.875968, 0.041555],
            [0.055630, -0.203977, 1.056972],
        ]
    )
    red = (0.64, 0.33)
    green = (0.3, 0.6)
    blue = (0.15, 0.06)


def convert_sRGB_to_XYZ(rgb):
    M = la.inv(SRGB.xyz_to_srgb_matrix)
    return M @ rgb


def convertXYZtoSRGB(xyz):
    return SRGB.xyz_to_srgb_matrix @ xyz


def gammaCorrect(rgb, gamma=1):
    return rgb ** (1 / gamma)


