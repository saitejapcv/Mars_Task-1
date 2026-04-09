import cv2
import numpy as np
import math


def find_distance(perceived_width):
    """
    Calculate distance using pinhole camera model
    """
    REAL_WIDTH = 17.0   # cm (given)
    IMAGE_WIDTH = 1280  # pixels (given)
    FOV = 55            # degrees (given)

    # Convert FOV to radians
    fov_rad = math.radians(FOV)

    # Calculate focal length
    focal_length = IMAGE_WIDTH / (2 * math.tan(fov_rad / 2))

    # Distance formula
    distance = (REAL_WIDTH * focal_length) / perceived_width

    return distance


def detect_arrow(image_path):
    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found!")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    found = False

    for cnt in contours:
        # Approximate shape
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)

        # Arrow typically has ~7 sides
        if len(approx) == 7:
            found = True

            # Draw contour
            cv2.drawContours(image, [approx], 0, (0, 255, 0), 3)
            print("Arrow detected!")

            # Bounding box
            x, y, w, h = cv2.boundingRect(approx)

            # Use width (better than max(w,h))
            perceived_width = w

            # Avoid division by zero
            if perceived_width == 0:
                print("Invalid width detected!")
                return

            # Calculate distance
            distance = find_distance(perceived_width)

            print(f"Estimated Distance: {distance:.2f} cm")

            # Draw bounding box
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

            break

    if not found:
        print("No arrow detected!")

    # Show result
    cv2.imshow('Detected Arrow', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Provide image path
image_path = 'arrow.jpg'
detect_arrow(image_path)
