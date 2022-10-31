# %%
# 필요 라이브러리 불러오기.
import cv2
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
import requests
from io import BytesIO

# %%
# Resize
img = cv2.imread('images/moon.jpg')

shrinked = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
zoomed_manual = cv2.resize(img, [i * 2 for i in list(reversed(img.shape))[1:]], interpolation=cv2.INTER_CUBIC)
zoomed_ratio = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

shrinked = cv2.cvtColor(shrinked, cv2.COLOR_BGR2RGB)
plt.imshow(shrinked)
plt.show()
shrinked = cv2.cvtColor(shrinked, cv2.COLOR_RGB2BGR)

zoomed_manual = cv2.cvtColor(zoomed_manual, cv2.COLOR_BGR2RGB)
plt.imshow(zoomed_manual)
plt.show()
zoomed_manual = cv2.cvtColor(zoomed_manual, cv2.COLOR_RGB2BGR)

zoomed_ratio = cv2.cvtColor(zoomed_ratio, cv2.COLOR_BGR2RGB)
plt.imshow(zoomed_ratio)
plt.show()
zoomed_ratio = cv2.cvtColor(zoomed_ratio, cv2.COLOR_RGB2BGR)

# %%
# Translation
rows, cols = img.shape[:2]

M = np.float32([[1, 0, 20], [0, 1, 40]])
dst = cv2.warpAffine(img, M, (cols, rows))

dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
plt.imshow(dst)
plt.show()
dst = cv2.cvtColor(dst, cv2.COLOR_RGB2BGR)

# %%
# Rotation
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 60, 0.5)
dst = cv2.warpAffine(img, M, (cols, rows))

dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
plt.imshow(dst)
plt.show()
dst = cv2.cvtColor(dst, cv2.COLOR_RGB2BGR)
