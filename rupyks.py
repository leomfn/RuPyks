import numpy as np
import matplotlib.pyplot as plt
import random


class Cube:

    def __init__(self):
        self.struc = self.reset()

    def reset(self):

        struc = np.zeros((5, 5, 5))

        struc[0, 1:-1, 1:-1] = 1  # negative x-direction, left, 1 = orange
        struc[-1, 1:-1, 1:-1] = 2  # positive x-direction, right, 2 = red
        struc[1:-1, 0, 1:-1] = 3  # negative y-direction, front, 3 = green
        struc[1:-1, -1, 1:-1] = 4  # positive y-direction, back, 4 = blue
        struc[1:-1, 1:-1, 0] = 5  # negative z-direction, down, 5 = yellow
        struc[1:-1, 1:-1, -1] = 6  # positive z-direction, up, 6 = white

        struc[struc == 0] = np.nan

        return struc

    def rotate(self, axis, side, direction=1):
        """Rotates one side of the cube.

        Keyword arguments:
        axis -- the axis as tuple with length 2
        side -- the side to rotate, 0 = side at minimum of chosen axis, 1 = side at maximum of chosen axis
        direction -- the direction around axis based on left hand rule, 1 = counter clockwise, -1 = clockwise (default 1)
        """
        struc = self.struc

        if side == 0:
            slice_index_start = 0
            slice_index_end = 2
        elif side == 1:
            slice_index_start = -2
            slice_index_end = 5

        # How to unify the following into a single function?
        if axis == 'x':
            ax = (2, 1)
            struc[slice_index_start:slice_index_end, :, :] = np.rot90(
                struc[slice_index_start:slice_index_end, :, :], k=direction, axes=ax)
        elif axis == 'y':
            # face = struc[:, slice_index_start:slice_index_end, :]
            ax = (0, 2)
            struc[:, slice_index_start:slice_index_end, :] = np.rot90(
                struc[:, slice_index_start:slice_index_end, :], k=direction, axes=ax)
        elif axis == 'z':
            ax = (1, 0)
            struc[:, :, slice_index_start:slice_index_end] = np.rot90(
                struc[:, :, slice_index_start:slice_index_end], k=direction, axes=ax)

        # face = np.rot90(face, k = direction, axes = ax)

    def shuffle(self):
        """Shuffles the cube by rotating randomly 1000 times."""
        struc = self.struc
        axes = ['x', 'y', 'z']
        for i in range(1000):
            ax = random.choice(axes)
            side = np.random.randint(2)
            dir = random.choice([-1, 1])

            self.rotate(axis=ax, side=side, direction=dir)


    def check(self):
        """Checks if cube is solved (True) or not (False)."""
        struc = self.struc
        i = 0
        for dim in range(3):
            for side in [0, -1]:
                uniqueValues = np.unique(
                    np.rollaxis(self.struc, dim)[side]
                )
                i += len(uniqueValues[~np.isnan(uniqueValues)])
        if i == 6:
            return True
        else:
            return False
        # np.rollaxis(cube.struc, 0)[-1]
        # np.unique(cube.struc[0,:,:])

    def plot(self):

        colors = {1: 'orange', 2: 'red', 3: 'green',
                  4: 'blue', 5: 'yellow', 6: 'white'}

        x = [0, 0.5, 1.5, 2.5, 3]
        y = [0, 0.5, 1.5, 2.5, 3]
        z = [0, 0.5, 1.5, 2.5, 3]

        X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        for x, y, z, s in zip(X.flatten(), Y.flatten(), Z.flatten(), self.struc.flatten()):
            # print(x, y, z, s)
            if not np.isnan(s):
                # print(colors[s])
                ax.scatter(x, y, z, s=50, c=colors[s])
        # ax.scatter(X, Y, Z, struc)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        # ax.scatter(1, 1, 1, color = 1)
        plt.show()

    def check(self):
        sides = ['up', 'down', 'front', 'back', 'left', 'right']
        i = 0
        for side in sides:
            i += len(np.unique(getattr(self, side)))
        if i > 6:
            print('not solved')
        else:
            print('solved')


cube = Cube()
cube.check()
cube.plot()
cube.shuffle()
cube.check()
cube.plot()
