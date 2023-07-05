import cv2
import numpy as np

def get_filtered_image(image, action):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    filtered = None
    if action == 'NO_FILTER':
        filtered = image
    elif action == 'LOW_LIGHT_ENHANCE':
        filtered = enhance_low_light(image)
    elif action == 'SHARPEN_IMAGE':
        filtered = sharpen_image(image)
    elif action == 'CLAHE':
        filtered = apply_clahe(image)
    elif action == 'DENOISE':
        filtered = denoise_image(image)
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

def sharpen_image(image):
    # Create a sharpening kernel
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    # Apply the sharpening kernel to the image
    sharpened_image = cv2.filter2D(image, -1, kernel)

    return sharpened_image

def apply_clahe(image):
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

def denoise_image(image):
    # Apply Bilateral Filter for denoising
    denoised_image = cv2.bilateralFilter(image, 9, 75, 75)

    return denoised_image