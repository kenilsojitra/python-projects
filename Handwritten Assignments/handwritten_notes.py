import cv2
import numpy as np

# Create a white image
img = np.ones((400, 800, 3), dtype=np.uint8) * 255

# Text to draw
text = "This is a handwritten-like script"

# Position for the text
position = (50, 100)

# Font options
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX  # Handwritten-style font
font_scale = 1.5
font_color = (0, 0, 0)  # Black text
thickness = 2

# Put the text on the image
cv2.putText(img, text, position, font, font_scale, font_color, thickness, cv2.LINE_AA)

# Save and display the image
cv2.imwrite("script_handwriting_note.png", img)

print("Handwritten-like note created successfully!")
