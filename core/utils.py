import cv2
import numpy as np

def get_filtered_image(image, action):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    filtered = None
    if action == 'NO_FILTER':
        filtered = image
    elif action == 'IMPROVE_RESOLUTION':
        filtered = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    elif action == 'LOW_LIGHT_ENHANCE':
        filtered = enhance_low_light(image)

    return filtered

def enhance_low_light(image):
    # Convert image to LAB color space
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Split LAB channels
    l, a, b = cv2.split(lab)

    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) to the L channel
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_l = clahe.apply(l)

    # Merge enhanced L channel with original A and B channels
    enhanced_lab = cv2.merge((enhanced_l, a, b))

    # Convert back to BGR color space
    enhanced_image = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)

    return enhanced_image
