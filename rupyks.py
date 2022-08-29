import numpy as np
import matplotlib.pyplot as plt


class Cube:
    struc = np.arange(0, 27).reshape(3, 3, 3)
    up = np.reshape(['w']*9, (3, 3))  # white
    down = np.reshape(['y']*9, (3, 3))  # yellow
    left = np.reshape(['o']*9, (3, 3))  # orange
    right = np.reshape(['r']*9, (3, 3))  # red
    front = np.reshape(['g']*9, (3, 3))  # green
    back = np.reshape(['b']*9, (3, 3))  # blue

    def turn_y_pos(self):
        """Turn the cube's side facing the positive y direction ("Front")
        clockwise"""
        self.struc[0] = np.rot90(self.struc[0], k=-1)
        self.front = np.rot90(self.front, k=-1)
        temp = self.up[2, :].copy()
        self.up[2, :] = self.left[:, 2][::-1]
        self.left[:, 2] = self.down[0, :]
        self.down[0, :] = self.right[:, 0][::-1]
        self.right[:, 0] = temp

    def turn_y_pos_r(self):
        """Turn the cube's side facing the positive y direction ("Front")
        counter clockwise (reverse)"""
        self.struc[0] = np.rot90(self.struc[0], k=1)
        self.front = np.rot90(self.front, k=1)
        temp = self.up[2, :].copy()
        self.up[2, :] = self.right[:, 0]
        self.right[:, 0] = self.down[0, :][::-1]
        self.down[0, :] = self.left[:, 2]
        self.left[:, 2] = temp[::-1]

    def plot(self):
        """Display the current (folded) cube's status using matplotlib's imshow"""
        colors = {'w': [i / 255 for i in [255, 255, 255]],
                  'y': [i / 255 for i in [255, 255, 0]],
                  'o': [i / 255 for i in [255, 128, 0]],
                  'r': [i / 255 for i in [255, 0, 0]],
                  'g': [i / 255 for i in [0, 128, 0]],
                  'b': [i / 255 for i in [0, 0, 255]]}
        sideaxes = {'up': (0, 1), 'down': (2, 1), 'left': (1, 0),
                    'right': (1, 2), 'front': (1, 1), 'back': (1, 3)}
        fig, ax = plt.subplots(3, 4)
        for axis in ax.flatten():
            axis.axis('off')
        for i, side in enumerate(sideaxes.keys()):
            Z = np.zeros((3, 3, 3))
            for color in colors.keys():
                Z[:, :, 0][getattr(self, side) == color] = colors[color][0]
                Z[:, :, 1][getattr(self, side) == color] = colors[color][1]
                Z[:, :, 2][getattr(self, side) == color] = colors[color][2]
            print(Z)
            ax[sideaxes[side]].imshow(Z)
            ax[sideaxes[side]].axis('on')
            ax[sideaxes[side]].tick_params(top=False, bottom=False, left=False, right=False,
                labelleft=False, labelbottom=False)
        plt.show()


cube = Cube()

cube.plot()

cube.turn_y_pos()
cube.turn_y_pos_r()
cube.plot()
