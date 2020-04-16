"""
This module changes color of images.
"""

import argparse
import os
import sys

import cv2
import matplotlib.pyplot as plt
import numpy as np


COLOR_BUILDINGS = [70, 70, 70]
COLOR_PEOPLE = [60, 20, 220]
COLOR_SKY = [180, 130, 70]
COLOR_CARS = [142, 0, 0]
COLOR_TREES = [35, 142, 107]

MONO_BUILDINGS = [11, 11, 11]
MONO_TREES = [21, 21, 21]


def change_color(image, _from, _to):
    """
    Change color of an image from specified color to specified color.
    """

    image[np.where((image == _from).all(axis=2))] = _to


def show_image(img):
    """
    Show image using cv2.
    """

    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.imshow('img', img)
    cv2.waitKey() & 0xff
    cv2.destroyAllWindows()


def show_image_array(img):
    """
    Show image using matplotlib.
    """

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    plt.show()


def save_image(path, img):
    """
    Save image.
    """

    cv2.imwrite(path, img)


def main(_from, _to):
    """
    Entry point.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', choices=['show', 'change'],
                        help='"cmd" is "show" or "change".')
    parser.add_argument('img_path', help='Path of the target image.')
    parser.add_argument('-s', '--save', help='Save image.')
    args = parser.parse_args()

    cmd = args.cmd
    img_path = args.img_path
    save_img_path = args.save

    # change color
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    change_color(img, _from, _to)

    if cmd == 'show':
        show_image(img)

    if save_img_path:
        save_image(save_img_path, img)

    print('success!')


if __name__ == '__main__':
    main(MONO_TREES, MONO_BUILDINGS)
