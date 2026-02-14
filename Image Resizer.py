import cv2

image_path = "example.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image.")
    exit()

print("Image loaded successfully!")

small = cv2.resize(image, (200, 200))
medium = cv2.resize(image, (400, 400))
large = cv2.resize(image, (600, 600))

cv2.imshow("Small Image (200x200)", small)
cv2.imshow("Medium Image (400x400)", medium)
cv2.imshow("Large Image (600x600)", large)

cv2.imwrite("input_image_small.jpg", small)
cv2.imwrite("input_image_medium.jpg", medium)
cv2.imwrite("input_image_large.jpg", large)

print("Resized images saved successfully!")

cv2.waitKey(0)