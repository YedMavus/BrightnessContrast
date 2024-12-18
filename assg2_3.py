import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.widgets import Slider
import cv2
from math import log
def brightnessAdjust(img, p):
    # To ensure p is between 0 and 1
    if p < 0 or p > 1:
        raise ValueError("p should be between 0 and 1")


    img_float = img.astype(np.float32)
    p = 2 * (p - 0.5)  
    img_bright = img_float + 255 * p
    # Clip the values to ensure they are within the valid range [0, 255]
    img_bright = np.clip(img_bright, 0, 255)

    # Convert back to uint8
    img_bright = img_bright.astype(np.uint8)

    return img_bright

def contrastAdjust(img, p):
    # Ensure p is between 0 and 1
    if p < 0 or p > 1:
        raise ValueError("p should be between 0 and 1")

    img_float = img.astype(np.float32)
    # p = (p-0.5)
    slope = (np.exp(10 * (p - 0.5)))  # Increase slope as p approaches 1

    # Adjust the image contrast
    img_contrast = 128 + slope * (img_float - 128)
    # Clip the image intensties to within 0 and 255 values
    img_contrast = np.clip(img_contrast, 0, 255)

    # Convert back to uint8
    img_contrast = img_contrast.astype(np.uint8)

    return img_contrast
def assg2_3():
    # Load image
    script_dir = os.path.dirname(__file__)
    image_path = os.path.join(script_dir, 'data', 'brightness_contrast.jpg')
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

    p_brightness_initial = 0.5  # Initial brightness factor
    p_contrast_initial = 0.5  # Initial contrast factor

    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.25, bottom=0.35)

    # Display the image initially
    img_display = contrastAdjust(brightnessAdjust(img_rgb, p_brightness_initial), p_contrast_initial)
    img_plot = ax.imshow(img_display)

    # Sliders
    ax_brightness_slider = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    slider_brightness = Slider(ax_brightness_slider, 'Brightness', 0.0, 1.0, valinit=p_brightness_initial)

    ax_contrast_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    slider_contrast = Slider(ax_contrast_slider, 'Contrast', 0.0, 1.0, valinit=p_contrast_initial)

    # Function to update the image when slider values change
    def update(val):
        p_brightness = slider_brightness.val
        p_contrast = slider_contrast.val
        img_display = contrastAdjust(brightnessAdjust(img_rgb, p_brightness), p_contrast)
        img_plot.set_data(img_display)
        fig.canvas.draw_idle()

    # Call update function when either slider value changes
    slider_brightness.on_changed(update)
    slider_contrast.on_changed(update)

    plt.show()
