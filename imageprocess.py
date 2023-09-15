import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(file_path):
    return cv2.imread(file_path)

def convert_to_hsv(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def find_max_color_area(hsv_image, color_ranges):
    max_pixels = 0
    max_color = None

    for fruit, (lower, upper) in color_ranges.items():
        mask = cv2.inRange(hsv_image, np.array(lower), np.array(upper))
        num_pixels = cv2.countNonZero(mask)

        if num_pixels > max_pixels:
            max_pixels = num_pixels
            max_color = fruit

    return max_color

def main():
    # Define color ranges for fruits and vegetables
    fruit_ranges = {
        'apple': [(0, 50, 70), (10, 255, 255)],
        'banana': [(20, 100, 100), (30, 255, 255)],
        'orange': [(10, 100, 100), (20, 255, 260)],
        'lemon': [(35, 400, 400), (70, 260, 255)]
    }

    vegetable_ranges = {
        "cucumber": [(44, 234, 114), (121, 236, 86)],
        "eggplant": [(126, 69, 114), (75, 49, 120)],
        "tomato": [(0, 50, 70), (10, 255, 255)],
        "potato": [(178, 94, 9), (227, 160, 115)],
        "lettuce": [(38, 154, 2), (60, 94, 0)],
        "pumpkin": [(255, 103, 0), (255, 90, 0)]
    }

    # Ask the user for input images
    fruit_image_path = input("Enter the path to a fruit image: ")
    vegetable_image_path = input("Enter the path to a vegetable image: ")

    # Load the images and convert to HSV color space
    fruit_img = load_image(fruit_image_path)
    vegetable_img = load_image(vegetable_image_path)

    if fruit_img is None or vegetable_img is None:
        print("Error loading images. Please check the image paths.")
        return

    hsv_fruit_img = convert_to_hsv(fruit_img)
    hsv_vegetable_img = convert_to_hsv(vegetable_img)

    # Find the dominant fruit and vegetable in the respective images
    dominant_fruit = find_max_color_area(hsv_fruit_img, fruit_ranges)
    dominant_vegetable = find_max_color_area(hsv_vegetable_img, vegetable_ranges)

    print("Dominant fruit in the fruit image:", dominant_fruit.upper())

    if dominant_vegetable:
        print("Dominant vegetable in the vegetable image:", dominant_vegetable.upper())
    else:
        print("No dominant vegetable found in the provided vegetable image.")

if __name__ == "__main__":
    main()
