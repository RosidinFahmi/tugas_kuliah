import os
os.environ["TK_SILENCE_DEPRECATION"] = "1"


import cv2
import numpy as np
from tkinter import Tk, Button, Label, filedialog
from PIL import Image, ImageTk

class ImageProcessor:
    def __init__(self, root):
        self.root = root
        self.root.title("Pengolahan Citra Digital - Rosidin Fahmi Abdillah - 221011402068")
        self.image = None
        self.processed_image = None

        # Buttons for functionalities
        Button(root, text="Load Image", command=self.load_image).grid(row=0, column=0)
        Button(root, text="Binary", command=self.to_binary).grid(row=0, column=1)
        Button(root, text="Dilasi", command=self.dilate_image).grid(row=0, column=2)
        Button(root, text="Erosi", command=self.erode_image).grid(row=0, column=3)
        Button(root, text="Opening", command=self.opening_image).grid(row=0, column=4)
        Button(root, text="Closing", command=self.closing_image).grid(row=0, column=5)
        Button(root, text="Edge Detection", command=self.edge_detection).grid(row=0, column=6)
        Button(root, text="Reset", command=self.reset_image).grid(row=0, column=7)

        # Label to display images
        self.image_label = Label(root)
        self.image_label.grid(row=1, column=0, columnspan=8)

    def load_image(self):
        # Open file dialog to let the user select an image
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpeg",)],
            title="Select an Image"
        )
        if file_path:
            self.image = cv2.imread(file_path)
        if self.image is None:
            print("Failed to load image. Please select a valid image file.")
            return
        print(f"Image shape: {self.image.shape}")
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.processed_image = self.image.copy()
        self.display_image(self.image)


    def display_image(self, image):
      try:
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        self.image_label.configure(image=image)
        self.image_label.image = image 
      except Exception as e:
        print(f"Error displaying image: {e}")

    def to_binary(self):
        if self.image is not None:
            gray = cv2.cvtColor(self.processed_image, cv2.COLOR_RGB2GRAY)
            _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
            self.processed_image = cv2.cvtColor(binary, cv2.COLOR_GRAY2RGB)
            self.display_image(self.processed_image)

    def dilate_image(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            dilated = cv2.dilate(cv2.cvtColor(self.processed_image, cv2.COLOR_RGB2GRAY), kernel, iterations=1)
            self.processed_image = cv2.cvtColor(dilated, cv2.COLOR_GRAY2RGB)
            self.display_image(self.processed_image)

    def erode_image(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            eroded = cv2.erode(cv2.cvtColor(self.processed_image, cv2.COLOR_RGB2GRAY), kernel, iterations=1)
            self.processed_image = cv2.cvtColor(eroded, cv2.COLOR_GRAY2RGB)
            self.display_image(self.processed_image)

    def opening_image(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            opened = cv2.morphologyEx(cv2.cvtColor(self.processed_image, cv2.COLOR_RGB2GRAY), cv2.MORPH_OPEN, kernel)
            self.processed_image = cv2.cvtColor(opened, cv2.COLOR_GRAY2RGB)
            self.display_image(self.processed_image)

    def closing_image(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            closed = cv2.morphologyEx(cv2.cvtColor(self.processed_image, cv2.COLOR_RGB2GRAY), cv2.MORPH_CLOSE, kernel)
            self.processed_image = cv2.cvtColor(closed, cv2.COLOR_GRAY2RGB)
            self.display_image(self.processed_image)

    def edge_detection(self):
        if self.image is not None:
            edges = cv2.Canny(cv2.cvtColor(self.processed_image, cv2.COLOR_RGB2GRAY), 100, 200)
            self.processed_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
            self.display_image(self.processed_image)

    def reset_image(self):
        if self.image is not None:
            self.processed_image = self.image.copy()
            self.display_image(self.image)

if __name__ == "__main__":
    root = Tk()
    app = ImageProcessor(root)
    root.mainloop()