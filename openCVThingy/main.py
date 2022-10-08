# %%
# 필요 라이브러리 불러오기.
import cv2
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
import requests
from io import BytesIO

# %%
# 이미지 읽기.
url = 'https://cdn.pixabay.com/photo/2018/10/01/09/21/pets-3715733_960_720.jpg'
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# %%
# 이미지 출력.
img

# %%
# img의 타입 확인.
type(img)

# %%
# PIL 이미지를 array 형태로 변환.
img_arr = np.asarray(img)

# %%
# img_arr의 타입 확인.
type(img_arr)

# %%
img_arr.shape

# %%
# 색상 값을 저장하기 위해 [[R, G, B], [...], ...]의 형태로 저장됨.
img_arr

# %%
# 배열 형태의 이미지 출력.
plt.imshow(img_arr)
plt.show()

# %%
# img를 복사하여 각 색상별 채널 분리. (파이썬 자체 배열 사용)
img_copy = img_arr.copy()

# 각 색상별 채널 분리.
red_channel = [[[img[0] for _ in range(3)] for img in img_] for img_ in img_copy]
green_channel = [[[img[1] for _ in range(3)] for img in img_] for img_ in img_copy]
blue_channel = [[[img[2] for _ in range(3)] for img in img_] for img_ in img_copy]

# %%
# 분리된 색상별 채널 출력.
plt.imshow(red_channel)
plt.show()

plt.imshow(green_channel)
plt.show()

plt.imshow(blue_channel)
plt.show()

# %%
# 각 색상별 채널 분리. (numpy 사용)
# 참고: [:, :, i] -> 배열은 삼차원 배열이며 일차원 배열의 i번 원소만 취할 것.
red_channel = img_copy[:, :, 0]
green_channel = img_copy[:, :, 1]
blue_channel = img_copy[:, :, 2]

# %%
# 분리된 색상별 채널 출력.
plt.imshow(red_channel, cmap='gray')        # 그래이 스케일 적용.
plt.show()

plt.imshow(green_channel, cmap='gray')
plt.show()

plt.imshow(blue_channel, cmap='gray')
plt.show()

# %%
# 각 채널 성분 추출.
red_channel = img_arr.copy()
red_channel[:, :, 1] = 0
red_channel[:, :, 2] = 0

green_channel = img_arr.copy()
green_channel[:, :, 0] = 0
green_channel[:, :, 2] = 0

blue_channel = img_arr.copy()
blue_channel[:, :, 0] = 0
blue_channel[:, :, 1] = 0

# %%
# 추출한 색상 채널 출력.
plt.imshow(red_channel)
plt.show()

plt.imshow(green_channel)
plt.show()

plt.imshow(blue_channel)
plt.show()

# %%
# OpenCV를 통한 이미지 출력.
# from google.colab.patches import cv2_imshow
# 로컬 환경에선 위의 함수 사용 불가.
# 참고: matplotlib의 색상 (R, G, B)
#       OpcnCV의 색상 (B, G, R)
# cv2.cvtColor() 필요.
# 플래그: COLOR_RGB2BGR 등등.

# %%
