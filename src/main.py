import cv2
import numpy as np
import os
import sys


COLOR_BUILDINGS = [70, 70, 70]
COLOR_PEOPLE = [60, 20, 220]
COLOR_SKY = [180, 130, 70]
COLOR_CARS = [142, 0, 0]
COLOR_TREES = [35, 142, 107]

MONO_BUILDINGS = [11, 11, 11]
MONO_TREES = [21, 21, 21]


def change_color(image, _from, _to):
    image[np.where((image == _from).all(axis=2))] = _to


def main(_from, _to):
    """
    USAGE
    -----
    python src/main.py show data/<input_file>
    python src/main.py save data/<input_file> data/<save_file>
    """

    args = sys.argv[1:]

    # change color
    path = args[1]
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    change_color(img, _from, _to)

    if args[0] == 'show':
        # show image
        cv2.namedWindow('img', cv2.WINDOW_NORMAL)
        cv2.imshow('img', img)
        cv2.waitKey() & 0xff
        cv2.destroyAllWindows()
    elif args[0] == 'save':
        # save image
        fname = args[2]
        cv2.imwrite(fname, img)

    print('success!')


if __name__ == '__main__':
    main(MONO_TREES, MONO_BUILDINGS)