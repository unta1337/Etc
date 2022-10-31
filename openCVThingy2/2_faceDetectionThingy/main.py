# %%
import numpy as np
import cv2
from matplotlib import pyplot as plt

# %%
image = cv2.imread('sample2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# %%
xml = '../haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(xml)
faces = face_cascade.detectMultiScale(gray, 1.2, 5)

len(faces)

# %%
if len(faces):
    for x, y, w, h in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap='gray')
plt.xticks([]), plt.yticks([])
plt.show()
